import pygame as py

from fields.Field import Field

HOUSE_SIZE = 20

class StreetField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placment_offset: int):
        super().__init__(x, y, width, height, player_placment_offset)

        self.name = ""
        self.price = 0
        self.house_cost = 0
        self.rent_costs = []
        self.img = None
        self.houses = 3
        self.facing_dir = ""

        self.house_img = py.image.load("././imgs/House.png")
        self.hotel_img = py.image.load("././imgs/Hotel.png")

        self.font = py.font.SysFont("Bahnschrift", 30, bold=True)

    def tick(self):
        # if self.is_clicked():
        #     print("Wurde gecklicked")

        self.reset_click()

    def add_information(self, name, price, house_cost, rent_costs, img, facing_dir):
        self.name = name
        self.price = price
        self.house_cost = house_cost
        self.rent_costs = rent_costs
        self.img = py.image.load(img)
        self.facing_dir = facing_dir

    def on_land(self, player):
        pass

    def render_extra_information(self, win):
        # py.draw.rect(win, (255, 0, 0), (self.x, self.y, self.width, self.height), 1)

        if self.is_selected:
            win.blit(self.font.render(self.name, False, (0, 0, 0)), (1520, 20))
            win.blit(self.img, (1520, 50))
            win.blit(self.font.render(str(self.price) + "$", False, (0, 0, 0)), (1650, 440))

            if self.owner == 0:
                win.blit(self.font.render("Owner: Noone", False, (0, 0, 0)), (1520, 500))
            else:
                win.blit(self.font.render(f"Owner: Player {self.owner}", False, (0, 0, 0)), (1520, 500))

            # Mark current rent with houses
            if self.houses == 0:
                py.draw.rect(win, (250, 0, 0), (1640, 115, 80, 30), 3)
            elif self.houses == 1:
                py.draw.rect(win, (250, 0, 0), (1755, 147, 60, 30), 3)
            elif self.houses == 2:
                py.draw.rect(win, (250, 0, 0), (1755, 179, 60, 30), 3)
            elif self.houses == 3:
                py.draw.rect(win, (250, 0, 0), (1755, 211, 60, 30), 3)
            elif self.houses == 4:
                py.draw.rect(win, (250, 0, 0), (1755, 243, 60, 30), 3)
            elif self.houses == 5:
                py.draw.rect(win, (250, 0, 0), (1590, 275, 180, 30), 3)

        # # Draw houses
        if 0 < self.houses < 5:
            if self.facing_dir == "top":
                space_x = int((self.width - HOUSE_SIZE * self.houses) / (self.houses + 1)) + 1

                for i in range(self.houses):
                    win.blit(self.house_img, (self.x + space_x + (i * (space_x + HOUSE_SIZE)), self.y + 5))
        elif self.houses == 5:
            space_x = (self.width - 20) / 2
            win.blit(self.hotel_img, (self.x + space_x, self.y + 5))
            
