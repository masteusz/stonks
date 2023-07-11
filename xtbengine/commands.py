def base_command(command_name, arguments=None):
    if arguments is None:
        arguments = dict()
    return dict([("command", command_name), ("arguments", arguments)])


def login_command(user_id, password, app_name=""):
    return base_command("login", dict(userId=user_id, password=password, appName=app_name))
