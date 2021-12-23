from control.commands.commands import Command

# INVOKER for Command Pattern


class UserControl:
    def __init__(self):
        self.on_start = None
        self.on_finish = None

    def set_on_start(self, command: Command):
        self.on_start = command

    def set_on_finish(self, command: Command):
        self.on_finish = command

    def execute(self) -> None:

        if isinstance(self.on_start, Command):
            self.on_start.execute()

        if isinstance(self.on_finish, Command):
            self.on_finish.execute()

