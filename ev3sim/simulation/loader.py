from ev3sim.settings import ObjectSetting, SettingsManager
from queue import Empty
import time
from typing import List

from luddite import get_version_pypi
from ev3sim.objects.base import objectFactory
from ev3sim.simulation.bot_comms import BotCommService
from ev3sim.simulation.interactor import IInteractor, fromOptions
from ev3sim.simulation.world import World, stop_on_pause
from ev3sim.visual.manager import ScreenObjectManager, screen_settings
from ev3sim.visual.objects import visualFactory
import ev3sim.visual.utils
from ev3sim.constants import *


class ScriptLoader:

    SEND = 0
    RECV = 1

    active_scripts: List[IInteractor]

    # TIME_SCALE simply affects the speed at which the simulation runs
    # (TIME_SCALE = 2, GAME_TICK_RATE = 30 implies 60 ticks of per actual seconds)
    GAME_TICK_RATE = 30
    VISUAL_TICK_RATE = 30
    TIME_SCALE = 1

    RANDOMISE_SENSORS = False

    instance: "ScriptLoader" = None
    running = True

    def __init__(self, **kwargs):
        ScriptLoader.instance = self
        self.robots = {}
        self.queues = {}
        self.outstanding_events = {}
        self.comms = BotCommService()
        self.active_scripts = []
        self.all_scripts = []

    def reset(self):
        for script in self.all_scripts:
            if hasattr(script, "_settings_name"):
                SettingsManager.instance.removeSetting(script._settings_name)
        self.active_scripts = []
        self.all_scripts = []

    def addActiveScript(self, script: IInteractor):
        idx = len(self.active_scripts)
        for x in range(len(self.active_scripts)):
            if self.active_scripts[x].SORT_ORDER > script.SORT_ORDER:
                idx = x
                break
        self.active_scripts.insert(idx, script)
        self.all_scripts.insert(idx, script)

    def sendEvent(self, botID, eventName, eventData):
        self.outstanding_events[botID].append((eventName, eventData))

    def setRobotQueues(self, botID, sendQ, recvQ):
        self.queues[botID] = (sendQ, recvQ)

    def startUp(self):
        self.object_map = {}
        self.physics_tick = 0

    def loadElements(self, items):
        # Handle any programmatic color references.
        elements = []
        from ev3sim.devices.base import initialise_device

        for item in items:
            assert "key" in item and "type" in item, f"Each item requires a key and type. {item}"
            if item["type"] == "visual":
                vis = visualFactory(**item)
                vis.key = item["key"]
                ScreenObjectManager.instance.registerVisual(vis, vis.key)
                self.object_map[item["key"]] = vis
                elements.append(vis)
            elif item["type"] == "object":
                devices = []
                to_remove = []
                for x in range(len(item.get("children", []))):
                    if item["children"][x]["type"] == "device":
                        devices.append(item["children"][x])
                        to_remove.append(x)
                for x in to_remove[::-1]:
                    del item["children"][x]
                obj = objectFactory(**item)
                obj.key = item["key"]
                for index, device in enumerate(devices):
                    # Instantiate the devices.
                    initialise_device(device, obj, index)
                if item.get("physics", False):
                    World.instance.registerObject(obj)
                ScreenObjectManager.instance.registerObject(obj, obj.key)
                self.object_map[obj.key] = obj
                elements.append(obj)
        return elements

    @stop_on_pause
    def incrementPhysicsTick(self):
        self.physics_tick += 1

    def handleWrites(self):
        for rob_id in self.robots:
            r_queue = self.queues[rob_id][self.RECV]
            while True:
                try:
                    write_type, data = r_queue.get_nowait()
                    if write_type == DEVICE_WRITE:
                        attribute_path, value = data
                        sensor_type, specific_sensor, attribute = attribute_path.split()
                        self.robots[rob_id].getDeviceFromPath(sensor_type, specific_sensor).applyWrite(attribute, value)
                    elif write_type == START_SERVER:
                        self.comms.startServer(data["connection_string"], data["robot_id"])
                    elif write_type == CLOSE_SERVER:
                        self.comms.closeServer(data["connection_string"], data["robot_id"])
                    elif write_type == JOIN_CLIENT:
                        self.comms.attemptConnectToServer(data["robot_id"], data["connection_string"])
                    elif write_type == CLOSE_CLIENT:
                        self.comms.closeClient(data["connection_string"], data["robot_id"])
                    elif write_type == SEND_DATA:
                        self.comms.handleSend(
                            data["robot_id"], data["send_to"], data["connection_string"], data["data"]
                        )
                except Empty:
                    break

    # Maximum amount of times simulation will push data without it being handled.
    MAX_DEAD_SENDS = 10

    def setValues(self):
        for key, robot in self.robots.items():
            s_queue = self.queues[key][self.SEND]
            good = True
            if s_queue.qsize() > self.MAX_DEAD_SENDS:
                good = False
            if (not good) or (not robot.spawned):
                continue
            info = {
                "tick": self.physics_tick,
                "tick_rate": self.GAME_TICK_RATE,
                "events": self.outstanding_events[key],
                "data": robot._interactor.collectDeviceData(),
            }
            self.outstanding_events[key] = []
            s_queue.put((SIM_DATA, info))

    def handleEvents(self, events):
        for event in events:
            for interactor in self.active_scripts:
                interactor.handleEvent(event)

    def simulation_tick(self):
        self.handleWrites()
        self.setValues()
        to_remove = []
        for i, interactor in enumerate(self.active_scripts):
            if interactor.tick(self.physics_tick):
                to_remove.append(i)
        for i in to_remove[::-1]:
            self.active_scripts[i].tearDown()
            del self.active_scripts[i]
        World.instance.tick(1 / self.GAME_TICK_RATE)
        for interactor in self.active_scripts:
            interactor.afterPhysics()
        self.incrementPhysicsTick()


loader_settings = {
    "FPS": ObjectSetting(ScriptLoader, "VISUAL_TICK_RATE"),
    "tick_rate": ObjectSetting(ScriptLoader, "GAME_TICK_RATE"),
    "timescale": ObjectSetting(ScriptLoader, "TIME_SCALE"),
}


class StateHandler:
    """
    Handles the current sim state, and passes information to the simulator, or other menus where appropriate.
    """

    instance: "StateHandler" = None

    is_simulating = False
    is_running = True

    shared_info: dict

    def __init__(self):
        StateHandler.instance = self
        sl = ScriptLoader()
        world = World()
        settings = SettingsManager()
        settings.addSettingGroup("app", loader_settings)
        settings.addSettingGroup("screen", screen_settings)
        self.shared_info = {}

    def closeProcesses(self):
        for process in self.shared_info.get("processes", []):
            process.terminate()
            process.join()
            process.close()
        self.shared_info["processes"] = []
        # Clear the result queue.
        while True:
            try:
                self.shared_info["result_queue"].get_nowait()
            except Empty:
                break
        # Clear all the robot queues.
        for rob_id in ScriptLoader.instance.queues:
            for key in (ScriptLoader.instance.SEND, ScriptLoader.instance.RECV):
                while True:
                    try:
                        ScriptLoader.instance.queues[rob_id][key].get_nowait()
                    except Empty:
                        break

    def startUp(self, **kwargs):
        SettingsManager.instance.setMany(kwargs)
        man = ScreenObjectManager()
        # Check for a new version of the simulator.
        latest_version = get_version_pypi("ev3sim")
        ScreenObjectManager.NEW_VERSION = latest_version != ev3sim.__version__
        man.startScreen()

    def beginSimulation(self, **kwargs):
        self.is_simulating = True
        from ev3sim.sim import main

        kwargs["command_line"] = False
        main(passed_args=kwargs)

    def mainLoop(self):
        last_vis_update = time.time() - 1.1 / ScriptLoader.instance.VISUAL_TICK_RATE
        last_game_update = time.time() - 1.1 / ScriptLoader.instance.GAME_TICK_RATE / ScriptLoader.instance.TIME_SCALE
        total_lag_ticks = 0
        lag_printed = False
        while self.is_running:
            new_time = time.time()
            if self.is_simulating:
                if (
                    new_time - last_game_update
                    > 1 / ScriptLoader.instance.GAME_TICK_RATE / ScriptLoader.instance.TIME_SCALE
                ):
                    ScriptLoader.instance.simulation_tick()
                    if (
                        new_time - last_game_update
                        > 2 / ScriptLoader.instance.GAME_TICK_RATE / ScriptLoader.instance.TIME_SCALE
                    ):
                        total_lag_ticks += 1
                    last_game_update = new_time
                    if (
                        ScriptLoader.instance.physics_tick > 10
                        and total_lag_ticks / ScriptLoader.instance.physics_tick > 0.5
                    ) and not lag_printed:
                        lag_printed = True
                        print("The simulation is currently lagging, you may want to turn down the game tick rate.")
                try:
                    r = self.shared_info["result_queue"].get_nowait()
                    self.closeProcesses()
                    if r is not True:
                        print(f"An error occurred in the {r[0]} process. Printing the error now...")
                        print(r[1])
                        # TODO: Just pop the screen and print the error.
                        self.is_running = False
                        self.is_simulating = False
                        return
                except Empty:
                    pass
            if new_time - last_vis_update > 1 / ScriptLoader.instance.VISUAL_TICK_RATE:
                last_vis_update = new_time
                events = ScreenObjectManager.instance.handleEvents()
                if self.is_running:
                    # We might've closed with those events.
                    if self.is_simulating:
                        ScriptLoader.instance.handleEvents(events)
                    ScreenObjectManager.instance.applyToScreen()


def initialiseFromConfig(config, send_queues, recv_queues):
    from collections import defaultdict
    from ev3sim.robot import initialise_bot, RobotInteractor
    from ev3sim.file_helper import find_abs

    ev3sim.visual.utils.GLOBAL_COLOURS = config.get("colours", {})
    # Keep track of index w.r.t. filename.
    robot_paths = defaultdict(lambda: 0)
    for index, robot in enumerate(config.get("robots", [])):
        robot_path = find_abs(robot, allowed_areas=["local", "local/robots/", "package", "package/robots/"])
        initialise_bot(config, robot_path, f"Robot-{index}", robot_paths[robot_path])
        robot_paths[robot_path] += 1
        ScriptLoader.instance.setRobotQueues(f"Robot-{index}", send_queues[index], recv_queues[index])
    for opt in config.get("interactors", []):
        try:
            ScriptLoader.instance.addActiveScript(fromOptions(opt))
        except Exception as exc:
            print(f"Failed to load interactor with the following options: {opt}. Got error: {exc}")
    SettingsManager.instance.setMany(config["settings"])
    if ScriptLoader.instance.active_scripts:
        ScriptLoader.instance.startUp()
        ScriptLoader.instance.loadElements(config.get("elements", []))
        for interactor in ScriptLoader.instance.active_scripts:
            if isinstance(interactor, RobotInteractor):
                interactor.connectDevices()
        for interactor in ScriptLoader.instance.active_scripts:
            interactor.startUp()
    else:
        print("No interactors successfully loaded. Quitting...")
