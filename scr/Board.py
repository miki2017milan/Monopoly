import pygame as py
import sys

from fields.StreetField import StreetField
from fields.StartField import StartField

class Board:
    def __init__(self):
        self.board_img = py.image.load(sys.path[0].replace("\\scr", "\\imgs\\Test.jpg"))

        self.fields = [StartField(1355, 936, 140, 140, 0),
                       StreetField(1266, 936, 83, 140, 30)]

        self.fields[1].add_information("Mediterranean Avenue", 60, 50, (2, 10, 30, 90, 160, 250), "\\Streets\\Mediterranean Avenue.PNG", "top")

        self.selected_field = -1

        self.fields[0].add_player(1)
        self.fields[0].add_player(2)

        self.fields[1].add_player(1)
        self.fields[1].add_player(2)

    def tick(self):
        for i, f in enumerate(self.fields):
            f.tick()

            if f.is_clicked():
                if self.selected_field == -1:
                    f.is_selected = True
                    self.selected_field = i
                elif self.selected_field == i:
                    f.is_selected = False
                    self.selected_field = -1

    def render(self, win):
        win.blit(self.board_img, (420, 0))
        
        for f in self.fields:
            f.render(win)