import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class EllipseCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        ellipse_rect = pg.Rect(self.args[0], self.args[1])

        pg.draw.ellipse(ds.draw_surface, ds.backgroundColor, ellipse_rect, 0)
        pg.draw.ellipse(ds.draw_surface, ds.borderColor, ellipse_rect, ds.borderWidth)
