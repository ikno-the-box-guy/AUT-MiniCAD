import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class PolygonCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        pg.draw.polygon(ds.draw_surface, ds.backgroundColor, self.args, 0)
        pg.draw.polygon(ds.draw_surface, ds.borderColor, self.args, ds.borderWidth)
