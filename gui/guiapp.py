import dearpygui.dearpygui as dpg
import structlog

from utils.env import Env
from xtbengine.api import XtbApi

logger = structlog.stdlib.get_logger()


class GuiApp:
    def __init__(self):
        self.WINDOW_WIDTH, self.WINDOW_HEIGHT = 1250, 950
        self.api = XtbApi(user=Env.XTB_USER_ID, password=Env.XTB_PASSWORD, demo=True)
        self.api.login()
        logger.info("Starting GUI")
        dpg.create_context()
        dpg.create_viewport()
        dpg.setup_dearpygui()
        dpg.set_viewport_title("Stonks")
        dpg.set_viewport_width(self.WINDOW_WIDTH)
        dpg.set_viewport_height(self.WINDOW_HEIGHT)
        self._create_windows()
        dpg.show_viewport()
        dpg.start_dearpygui()

    def get_example_data(self):
        data = self.api.get_margins()
        try:
            dpg.get_item_type("margintable")
            dpg.delete_item("margintable")
        except SystemError:
            logger.debug("No previous margintable found")

        with dpg.table(header_row=False, parent="mainview", tag="margintable"):
            dpg.add_table_column()
            dpg.add_table_column()
            for k, v in data.items():
                with dpg.table_row():
                    dpg.add_text(k)
                    dpg.add_text(v)

    def _create_windows(self):
        self._create_main_window()

    def _create_main_window(self):
        with dpg.window(label="Main View", tag="mainview", autosize=True):
            dpg.add_button(label="Get Data", callback=self.get_example_data)
