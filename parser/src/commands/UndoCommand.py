from src.Command import Command
from src.DrawState import DrawState


class UndoCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        pass
