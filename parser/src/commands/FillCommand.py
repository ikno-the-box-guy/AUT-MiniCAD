from src.Command import Command


class FillCommand(Command):
    def __init__(self, name: str, description: str, args: list = None):
        super().__init__(name, description, args)

    def exec(self):
        # This method should be implemented in subclasses
        raise NotImplementedError("The exec method must be implemented in subclasses.")