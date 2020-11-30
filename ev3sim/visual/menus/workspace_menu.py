import pygame
import pygame_gui
from ev3sim.file_helper import find_abs
from ev3sim.visual.menus.base_menu import BaseMenu
from ev3sim.visual.settings.main_settings import main_settings


class WorkspaceMenu(BaseMenu):
    def sizeObjects(self):
        self.bg.set_dimensions(self._size)
        self.bg.set_position((0, 0))
        text_size = (self._size[0] / 2, self._size[1] / 2)
        self.text_panel.set_dimensions(text_size)
        self.text_panel.set_position((text_size[0] / 2, text_size[1] / 2))
        button_ratio = 2
        button_size = (self._size[0] / 6, self._size[1] / 4)
        button_size = (
            min(button_size[0], button_size[1] * button_ratio),
            min(button_size[1], button_size[0] / button_ratio),
        )
        self.text.set_dimensions((text_size[0] - 60, text_size[1] - button_size[1] - 90))
        self.text.set_position((text_size[0] / 2 + 30, text_size[1] / 2 + 30))
        self.skip.set_dimensions(button_size)
        self.skip.set_position((text_size[0] / 2 + 30, 3 * text_size[1] / 2 - button_size[1] - 30))
        self.select.set_dimensions(button_size)
        self.select.set_position(
            (3 * text_size[0] / 2 - 30 - button_size[0], 3 * text_size[1] / 2 - button_size[1] - 30)
        )

    def generateObjects(self):
        dummy_rect = pygame.Rect(0, 0, *self._size)
        # In order to respect theme changes, objects must be built in initWithKwargs
        self.bg = pygame_gui.elements.UIPanel(
            relative_rect=dummy_rect,
            starting_layer_height=-1,
            manager=self,
            object_id=pygame_gui.core.ObjectID("background"),
        )
        self._all_objs.append(self.bg)
        self.text_panel = pygame_gui.elements.UIPanel(
            relative_rect=dummy_rect,
            starting_layer_height=-0.5,
            manager=self,
            object_id=pygame_gui.core.ObjectID("text_background"),
        )
        self._all_objs.append(self.text_panel)
        self.text = pygame_gui.elements.UITextBox(
            html_text="""\
In order to use ev3sim, you need to specify a <font color="#06d6a0">workspace folder</font>.<br><br>\
<font color="#4cc9f0">Bots</font> and <font color="#4cc9f0">presets</font> you create will be stored in this folder.\
""",
            relative_rect=dummy_rect,
            manager=self,
            object_id=pygame_gui.core.ObjectID("text_dialog_workspace", "text_dialog"),
        )
        self._all_objs.append(self.text)
        self.skip = pygame_gui.elements.UIButton(
            relative_rect=dummy_rect,
            text="Skip",
            manager=self,
            object_id=pygame_gui.core.ObjectID("skip_button", "menu_button"),
        )
        self._all_objs.append(self.skip)
        self.select = pygame_gui.elements.UIButton(
            relative_rect=dummy_rect,
            text="Select",
            manager=self,
            object_id=pygame_gui.core.ObjectID("select_button", "menu_button"),
        )
        self._all_objs.append(self.select)

    def handleEvent(self, event):
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            from ev3sim.visual.manager import ScreenObjectManager

            if event.ui_object_id.startswith("skip_button"):
                ScreenObjectManager.instance.popScreen()
                ScreenObjectManager.instance.pushScreen(ScreenObjectManager.SCREEN_MENU)
            if event.ui_object_id.startswith("select_button"):
                # Open file dialog.
                import yaml
                from tkinter import Tk
                from tkinter.filedialog import askdirectory
                from ev3sim.simulation.loader import StateHandler

                Tk().withdraw()
                directory = askdirectory()
                if not directory:
                    return
                conf_file = find_abs("user_config.yaml", allowed_areas=["package"])
                with open(conf_file, "r") as f:
                    conf = yaml.safe_load(f)
                conf["app"]["workspace_folder"] = directory
                with open(conf_file, "w") as f:
                    f.write(yaml.dump(conf))
                StateHandler.WORKSPACE_FOLDER = directory
                ScreenObjectManager.instance.popScreen()
                ScreenObjectManager.instance.pushScreen(ScreenObjectManager.SCREEN_MENU)

    def onPop(self):
        pass