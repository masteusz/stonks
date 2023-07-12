import structlog

from xtbengine.commands import login_command, margin_level_command, logout_command
from xtbengine.xAPIConnector import JsonSocket
from utils.env import Env

logger = structlog.stdlib.get_logger()

DEFAULT_XAPI_ADDRESS = "xapi.xtb.com"
DEMO_XAPI_PORT = 5124
DEMO_XAPI_STREAMING_PORT = 5125
REAL_XAPI_PORT = 5112
REAL_XAPI_STREAMING_PORT = 5113
API_MAX_CONN_TRIES = 3


class XtbApi(JsonSocket):
    def __init__(self, user: int, password: str, demo=True, encrypt=True):
        self.user = user
        self.password = password
        self.addr = DEFAULT_XAPI_ADDRESS
        if demo:
            self.app_port = DEMO_XAPI_PORT
            self.app_streaming_port = DEMO_XAPI_STREAMING_PORT
        else:
            self.app_port = REAL_XAPI_PORT
            self.app_streaming_port = REAL_XAPI_STREAMING_PORT

        super(XtbApi, self).__init__(self.addr, self.app_port, encrypt)
        if not self.connect():
            raise Exception(f"Cannot connect to {self.address}:{self.port} after {API_MAX_CONN_TRIES} retries")

    def execute(self, command):
        self._send_obj(command)
        return self._read_obj()

    def login(self) -> str:
        logger.info("Logging in")
        res = self.execute(login_command(user_id=self.user, password=self.password))
        if res["status"]:
            return res["streamSessionId"]
        return ""

    def logout(self) -> bool:
        logger.info("Logging out")
        res = self.execute(logout_command())
        return res.get("status", None)

    def get_margins(self) -> dict:
        logger.info("Getting margin info")
        res = self.execute(margin_level_command())
        if res["status"]:
            return res["returnData"]
        return {}


if __name__ == "__main__":
    api = XtbApi(user=Env.XTB_USER_ID, password=Env.XTB_PASSWORD, demo=True)
    api.login()
    api.get_margins()
    api.logout()
