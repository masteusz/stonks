import dearpygui.dearpygui as dpg
import structlog

from xtbengine.api import XtbApi

logger = structlog.stdlib.get_logger()


class MainWindow:
    def __init__(self):
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 1250, 950
        self.api = XtbApi()

        logger.info("Starting GUI")
        self._init_window()

    def _init_window(self):
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()
        dpg.set_viewport_title("Stonks")
        dpg.set_viewport_width(self.WINDOW_WIDTH)
        dpg.set_viewport_height(self.WINDOW_HEIGHT)

        with dpg.window(label="Main View"):
            dpg.add_text("Hello world")
            dpg.add_button(label="Save")
            dpg.add_input_text(label="string")
            dpg.add_slider_float(label="float")

        dpg.show_viewport()
        dpg.start_dearpygui()
