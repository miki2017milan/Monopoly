import pygame as py
import sys

from scr.fields.StreetField import StreetField
from scr.fields.StartField import StartField
from scr.fields.TreasureField import TreasureField
from scr.fields.EmptyField import EmptyField
from scr.fields.TrainField import TrainField
from scr.Assets import Assets

class Board:
    def __init__(self):
        self.board_img = Assets.board_img

        self.fields = [StartField(1354, 935, 140, 140, (0, 0)),
                       StreetField(1266, 936, 83, 140, (0, 30), "Mediterranean Avenue"),
                       TreasureField(1180, 936, 83, 140, (0, 0)),
                       StreetField(1093, 936, 84, 140, (0, 30), "Baltic Avenue"),
                       EmptyField(1006, 936, 84, 140, (0, 0)),
                       TrainField(916, 936, 87, 140, (0, 0), "Reading Railroad")]

        self.fields[0].add_player(1)
        self.fields[0].add_player(2)
        self.fields[0].add_player(3)
        self.fields[0].add_player(4)

        self.selected_field = -1

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