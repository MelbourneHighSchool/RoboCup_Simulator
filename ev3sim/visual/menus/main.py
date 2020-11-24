import pygame
import pygame_gui
from ev3sim.file_helper import find_abs
from ev3sim.visual.menus.base_menu import BaseMenu
from ev3sim.visual.settings.main_settings import main_settings


def on_button_simulate(*args, **kwargs):
    from ev3sim.visual.manager import ScreenObjectManager

    ScreenObjectManager.instance.pushScreen(ScreenObjectManager.instance.SCREEN_BATCH)


class MainMenu(BaseMenu):
    def sizeObjects(self):
        self.bg.set_dimensions(self._size)
        self.bg.set_position((0, 0))
        self.title.set_dimensions((self._size[0] - 60, 50))
        self.title.set_position((30, 30))
        button_size = self._size[0] / 4, self._size[1] / 6
        self.simulate_button.set_dimensions(button_size)
        self.simulate_button.set_position(
            ((self._size[0] - button_size[0]) / 2, (self._size[1] - button_size[1]) / 2 - button_size[1] * 1.5)
        )
        self.bot_button.set_dimensions(button_size)
        self.bot_button.set_position(((self._size[0] - button_size[0]) / 2, (self._size[1] - button_size[1]) / 2))
        self.settings_button.set_dimensions(button_size)
        self.settings_button.set_position(
            ((self._size[0] - button_size[0]) / 2, (self._size[1] - button_size[1]) / 2 + button_size[1] * 1.5)
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
        self.title = pygame_gui.elements.UILabel(
            relative_rect=dummy_rect, text="EV3Sim", manager=self, object_id=pygame_gui.core.ObjectID("title")
        )
        self._all_objs.append(self.title)
        self.simulate_button = pygame_gui.elements.UIButton(
            relative_rect=dummy_rect,
            text="Simulate",
            manager=self,
            object_id=pygame_gui.core.ObjectID("simulate_button"),
        )
        self._all_objs.append(self.simulate_button)
        self.bot_button = pygame_gui.elements.UIButton(
            relative_rect=dummy_rect,
            text="Bots",
            manager=self,
            object_id=pygame_gui.core.ObjectID("bots_button"),
        )
        self._all_objs.append(self.bot_button)
        self.settings_button = pygame_gui.elements.UIButton(
            relative_rect=dummy_rect,
            text="Settings",
            manager=self,
            object_id=pygame_gui.core.ObjectID("main_settings_button"),
        )
        self._all_objs.append(self.settings_button)

    def handleEvent(self, event):
        if event.type == pygame.USEREVENT and event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            from ev3sim.visual.manager import ScreenObjectManager

            if event.ui_object_id.startswith("simulate_button"):
                ScreenObjectManager.instance.pushScreen(ScreenObjectManager.SCREEN_BATCH)
            if event.ui_object_id.startswith("bots_button"):
                ScreenObjectManager.instance.pushScreen(ScreenObjectManager.SCREEN_BOTS)
            if event.ui_object_id.startswith("main_settings_button"):
                ScreenObjectManager.instance.pushScreen(
                    ScreenObjectManager.SCREEN_SETTINGS,
                    file=find_abs("user_config.yaml", ["package"]),
                    settings=main_settings,
                )

    def onPop(self):
        pass