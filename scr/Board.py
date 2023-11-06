import pygame as py

from StreetField import StreetField

class Board:
    def __init__(self):
        self.board_img = py.image.load("./imgs/Test.jpg")
        self.board = [StreetField(100, 100, 75, 200)]

    def tick(self):
        for f in self.board:
            f.tick()

    def render(self, win):
        win.blit(self.board_img, (420, 0))
        
        for f in self.board:
            f.render(win)