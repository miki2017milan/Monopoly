import pygame as py
import sys

from fields.StreetField import StreetField
from fields.StartField import StartField
from fields.TreasureField import TreasureField

class Board:
    def __init__(self):
        self.board_img = py.image.load(sys.path[0].replace("\\scr", "\\imgs\\Test.jpg"))

        self.fields = [StartField(1354, 935, 140, 140, (0, 0)),
                       StreetField(1266, 936, 83, 140, (0, 30)),
                       TreasureField(1180, 936, 83, 140, (0, 0)),
                       StreetField(1093, 936, 84, 140, (0, 30))]

        self.fields[1].add_information("Mediterranean Avenue", 60, 50, (2, 10, 30, 90, 160, 250), "\\Streets\\Mediterranean Avenue.PNG", "top", "brown")
        self.fields[3].add_information("Baltic Avenue", 60, 50, (4, 20, 60, 180, 320, 450), "\\Streets\\Baltic Avenue.PNG", "top", "brown")

        self.selected_field = -1

        self.fields[0].add_player(1)
        self.fields[0].add_player(2)

        self.fields[1].add_player(1)
        self.fields[1].add_player(2)

        self.fields[2].add_player(1)
        self.fields[2].add_player(2)
        self.fields[2].add_player(3)
        self.fields[2].add_player(4)

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