import pygame as py

from StreetField import StreetField

class Board:
    def __init__(self):
        self.board_img = py.image.load("./imgs/Test.jpg")
        self.fields = [StreetField(1355, 936, 140, 140, ((10, 80), (70, 80)))]
        self.fields[0].player_spots[0] = 1
        self.fields[0].player_spots[1] = 2

    def tick(self):
        for f in self.fields:
            f.tick()

    def render(self, win):
        win.blit(self.board_img, (420, 0))
        
        for f in self.fields:
            f.render(win)