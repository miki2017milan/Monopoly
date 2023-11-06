import pygame as py

from Field import Field

class StreetField(Field):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def tick(self):
        if self.is_clicked():
            print("Wurde gecklicked")

        self.reset_click()

    def render(self, win):
        py.draw.rect(win, (200, 50, 50), (self.x, self.y, self.width, self.height))
        pass