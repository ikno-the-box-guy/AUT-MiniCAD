import pygame as pg


class DrawState:
    def __init__(self, draw_surface: pg.Surface):
        self.borderColor = pg.Color('white')
        self.backgroundColor = pg.Color('black')
        self.borderWidth = 2
        self.draw_surface = draw_surface

    def save_state(self):
        return {
            'borderColor': self.borderColor,
            'backgroundColor': self.backgroundColor,
            'borderWidth': self.borderWidth
        }

    def restore_state(self, state):
        self.borderColor = state['borderColor']
        self.backgroundColor = state['backgroundColor']
        self.borderWidth = state['borderWidth']
