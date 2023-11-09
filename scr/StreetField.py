import pygame as py

from Field import Field

class StreetField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_spots_pos: tuple):
        super().__init__(x, y, width, height, player_spots_pos)

    def tick(self):
        # if self.is_clicked():
        #     print("Wurde gecklicked")

        self.reset_click()

    def render_extra_information(self, win):
        pass
