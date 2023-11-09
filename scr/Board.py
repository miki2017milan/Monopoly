import pygame as py

from StreetField import StreetField

class Board:
    def __init__(self):
        self.board_img = py.image.load("./imgs/Test.jpg")
        self.fields = [StreetField(1355, 936, 140, 140, ((27, 27), (84, 27), (27, 84), (84, 84)))]
        self.selected_field = -1

        self.fields[0].add_player(1)
        self.fields[0].add_player(2)
        self.fields[0].add_player(3)
        self.fields[0].add_player(4)

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