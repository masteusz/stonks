import structlog

from xtbengine.xAPIConnector import APIClient, loginCommand

logger = structlog.stdlib.get_logger()


class XtbApi:
    def __init__(self):
        self.apiclient = APIClient()
        print(self.apiclient.execute(loginCommand(userId="12345", password="pass")))


if __name__ == "__main__":
    api = XtbApi()
