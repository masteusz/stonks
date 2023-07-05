import structlog

from gui.mainwindow import MainWindow
from utils import configure_logging

logger = structlog.stdlib.get_logger()
if __name__ == "__main__":
    configure_logging()
    logger.info("Starting app")
    gui = MainWindow()
