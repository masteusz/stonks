import structlog

from gui.guiapp import GuiApp
from utils.log import configure_logging

logger = structlog.stdlib.get_logger()
if __name__ == "__main__":
    configure_logging()
    logger.info("Starting app")
    gui = GuiApp()
