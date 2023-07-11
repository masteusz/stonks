from typing import Optional


def base_command(command_name: str, arguments: Optional[dict] = None):
    if arguments is None:
        arguments = dict()
    return dict([("command", command_name), ("arguments", arguments)])


def login_command(user_id: int, password: str, app_name: str = ""):
    return base_command("login", dict(userId=user_id, password=password, appName=app_name))


def logout_command():
    return base_command("logout")


def margin_level_command():
    return base_command('getMarginLevel')
