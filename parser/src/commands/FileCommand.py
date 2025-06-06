from src.Command import Command
from src.DrawState import DrawState


class FileCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

        from src.processing.Interpreter import interpret_file
        self.commands = []
        new_commands = interpret_file(args[0])

        for command in new_commands:
            if command.name == 'UNDO':
                if self.commands:
                    self.commands.pop()
            else:
                self.commands.append(command)

    def exec(self, ds: DrawState):
        # Save ds state before executing commands
        state = ds.save_state()

        for command in self.commands:
            command.exec(ds)

        # Restore ds state after executing commands
        ds.restore_state(state)
