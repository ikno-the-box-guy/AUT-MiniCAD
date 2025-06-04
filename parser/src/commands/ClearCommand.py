import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class ClearCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        color = pg.Color(self.args[0]) if self.args else pg.Color('black')
        ds.draw_surface.fill(color)
