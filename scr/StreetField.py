import pygame as py

from Field import Field

class StreetField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_spots_pos: tuple):
        super().__init__(x, y, width, height, player_spots_pos)

    def tick(self):
        if self.is_clicked():
            print("Wurde gecklicked")

        self.reset_click()

    def render(self, win):
        self.render_players(win)

        py.draw.rect(win, (200, 50, 50), (self.x, self.y, self.width, self.height), 2)