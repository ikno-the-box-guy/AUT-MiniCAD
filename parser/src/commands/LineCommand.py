import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class LineCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        pg.draw.line(
            ds.draw_surface,
            ds.borderColor,
            self.args[0],
            self.args[1],
            ds.borderWidth
        )
