import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class RectangleCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        rect = pg.Rect(self.args[0], self.args[1])

        ds.draw_surface.fill(ds.borderColor, rect)
        ds.draw_surface.fill(ds.backgroundColor, rect.inflate(-ds.borderWidth * 2, -ds.borderWidth * 2))
