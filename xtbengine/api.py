import structlog

from xtbengine.commands import base_command
from xtbengine.xAPIConnector import JsonSocket

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
            raise Exception(
                f"Cannot connect to {self.address}:{self.port} after {API_MAX_CONN_TRIES} retries"
            )

    def execute(self, dictionary):
        self._sendObj(dictionary)
        return self._read_obj()

    def execute_command(self, command_name, arguments=None):
        return self.execute(base_command(command_name, arguments))


if __name__ == "__main__":
    api = XtbApi(user=12345, password="abcde", demo=True)
