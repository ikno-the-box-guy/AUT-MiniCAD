import pygame as pg


class DrawState:
    def __init__(self, draw_surface: pg.Surface):
        self.borderColor = pg.Color('white')
        self.backgroundColor = pg.Color('black')
        self.borderWidth = 2
        self.draw_surface = draw_surface
