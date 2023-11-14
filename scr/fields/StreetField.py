from tokenize import String
import pygame as py
import sys

from scr.fields.Field import Field
from scr.Assets import Assets

HOUSE_SIZE = 20

class StreetField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placment_offset: tuple, name: str):
        super().__init__(x, y, width, height, player_placment_offset)

        self.data = Assets.street_information[name]

        self.name = name
        self.price = self.data[0]
        self.house_cost = self.data[1]
        self.rent_costs = self.data[2]
        self.img = self.data[3]
        self.facing_dir = self.data[4]
        self.color = self.data[5]

        self.houses = 0

    def tick(self):
        self.reset_click()

    def on_land(self, player):
        pass

    def render_extra_information(self, win):
        # py.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)

        if self.is_selected:
            win.blit(self.text_font.render(self.name, False, (0, 0, 0)), (1520, 20))
            win.blit(self.img, (1520, 50))
            win.blit(self.text_font.render(str(self.price) + "$", False, (0, 0, 0)), (1650, 440))

            if self.owner == 0:
                win.blit(self.text_font.render("Owner: Noone", False, (0, 0, 0)), (1520, 500))
            else:
                win.blit(self.text_font.render(f"Owner: Player {self.owner}", False, (0, 0, 0)), (1520, 500))

            # Mark current rent with houses
            if self.houses == 0:
                py.draw.rect(win, (250, 0, 0), (1640, 115, 80, 30), 3)
            elif self.houses == 1:
                py.draw.rect(win, (250, 0, 0), (1740, 147, 60, 30), 3)
            elif self.houses == 2:
                py.draw.rect(win, (250, 0, 0), (1740, 179, 60, 30), 3)
            elif self.houses == 3:
                py.draw.rect(win, (250, 0, 0), (1740, 211, 60, 30), 3)
            elif self.houses == 4:
                py.draw.rect(win, (250, 0, 0), (1740, 243, 60, 30), 3)
            elif self.houses == 5:
                py.draw.rect(win, (250, 0, 0), (1590, 275, 180, 30), 3)

        # # Draw houses
        if 0 < self.houses < 5:
            if self.facing_dir == "top":
                space_x = int((self.width - HOUSE_SIZE * self.houses) / (self.houses + 1)) + 1

                for i in range(self.houses):
                    win.blit(Assets.house_img, (self.x + space_x + (i * (space_x + HOUSE_SIZE)), self.y + 5))
        elif self.houses == 5:
            space_x = (self.width - 20) / 2
            win.blit(Assets.hotel_img, (self.x + space_x, self.y + 5))
            
