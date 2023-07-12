import dotenv
from pydantic import BaseSettings


class _Env(BaseSettings):
    class Config:
        env_file = dotenv.find_dotenv(raise_error_if_not_found=False)
        env_file_encoding = "utf-8"

    XTB_USER_ID: str
    XTB_PASSWORD: str


Env = _Env()
