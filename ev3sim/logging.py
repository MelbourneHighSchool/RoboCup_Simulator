import os
from ev3sim.file_helper import find_abs_directory
from ev3sim.visual.manager import ScreenObjectManager


class Logger:

    LOG_CONSOLE = True

    instance: "Logger"

    def __init__(self):
        Logger.instance = self

    def getFilename(self, robot_id):
        from ev3sim.simulation.loader import StateHandler

        if StateHandler.WORKSPACE_FOLDER:
            log_dir = find_abs_directory("workspace/logs/", create=True)
        else:
            log_dir = find_abs_directory("package/logs/", create=True)
        return os.path.join(log_dir, f"{robot_id}_log.txt")

    def beginLog(self, robot_id):
        with open(self.getFilename(robot_id), "w") as _:
            # Don't write anything
            pass

    def writeMessage(self, robot_id, msg):
        if Logger.LOG_CONSOLE:
            ScreenObjectManager.instance.screens[ScreenObjectManager.SCREEN_SIM].printStyledMessage(msg)
        with open(self.getFilename(robot_id), "a") as f:
            f.write(msg)

    def reportError(self, robot_id, traceback):
        if Logger.LOG_CONSOLE:
            robot_index = int(robot_id.split("-")[1])
            ScreenObjectManager.instance.screens[ScreenObjectManager.SCREEN_SIM].printError(robot_index)
        with open(self.getFilename(robot_id), "a") as f:
            f.write(traceback)

    def openLog(self, robot_id):
        import platform
        import subprocess

        if platform.system() == "Windows":
            subprocess.Popen(["explorer", "/select,", self.getFilename(robot_id)])
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", self.getFilename(robot_id)])
        else:
            subprocess.Popen(["xdg-open", self.getFilename(robot_id)])
