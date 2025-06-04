from src.Command import Command
from src.DrawState import DrawState


class WidthCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        ds.borderWidth = self.args[0] if self.args else ds.borderWidth
