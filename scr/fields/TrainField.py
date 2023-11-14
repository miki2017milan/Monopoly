import sys
import pygame as py

from scr.fields.Field import Field
from scr.Assets import Assets

class TrainField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placement_offset: tuple, name: str):
        super().__init__(x, y, width, height, player_placement_offset)
        self.count_owned = 0

        self.data = Assets.railroad_information[name]

        self.name = name
        self.price = self.data[0]
        self.rent_costs = self.data[1]
        self.img = self.data[2]
    
    def add_owned(self):
        self.count_owned += 1

    def tick(self):
        self.reset_click()

    def on_land(self, player):
        print("landed on train field")

    def render_extra_information(self, win):
        if self.is_selected:
            win.blit(self.text_font.render(self.name, False, (0, 0, 0)), (1520, 20))
            win.blit(self.img, (1520, 50))
            win.blit(self.text_font.render(str(self.price) + "$", False, (0, 0, 0)), (1650, 335))

            if self.owner == 0:
                win.blit(self.text_font.render("Owner: Noone", False, (0, 0, 0)), (1520, 410))
            else:
                win.blit(self.text_font.render(f"Owner: Player {self.owner}", False, (0, 0, 0)), (1520, 410))

            # Mark current rent with houses
            if self.count_owned == 1:
                py.draw.rect(win, (250, 0, 0), (1775, 203, 60, 30), 3)
            elif self.count_owned == 2:
                py.draw.rect(win, (250, 0, 0), (1775, 236, 60, 30), 3)
            elif self.count_owned == 3:
                py.draw.rect(win, (250, 0, 0), (1775, 269, 60, 30), 3)
            elif self.count_owned == 4:
                py.draw.rect(win, (250, 0, 0), (1775, 301, 60, 30), 3)
