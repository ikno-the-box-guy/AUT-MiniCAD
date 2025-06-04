import pygame as pg

from src.Command import Command
from src.DrawState import DrawState


class BorderCommand(Command):
    def __init__(self, name: str, args: list = None):
        super().__init__(name, args)

    def exec(self, ds: DrawState):
        new_color = pg.Color(self.args[0]) if self.args else pg.Color('black')
        ds.borderColor = new_color
