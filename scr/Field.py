import pygame as py

from abc import ABC, abstractmethod

PLAYER_COLORS = [(200, 50, 50), (50, 200, 50), (50, 50, 200), (200, 50, 200)]
PLAYER_SIZE = 50

class Field(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, player_spots_pos: tuple):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_spots_pos = player_spots_pos
        self.player_spots = [0, 0, 0, 0]

        self.can_click = True

    def is_clicked(self):
        mx, my = py.mouse.get_pos()
        # print(self.x, self.width, self.y, self.height)
        if self.x + self.width > mx > self.x and self.y + self.height > my > self.y and self.can_click and py.mouse.get_pressed()[0]:
            self.can_click = False
            return True
        
    def reset_click(self):
        if not py.mouse.get_pressed()[0]:
            self.can_click = True

    def add_player(self, player: int):
        for s in range(self.player_spots):
            if self.player_spots[s] == 0:
                self.player_spots[s] = player
                return
            
        raise Exception("Could't add another player to the field.")
    
    def render_players(self, win):
        for i, p in enumerate(self.player_spots):
            if not p == 0:
                py.draw.ellipse(win, PLAYER_COLORS[p - 1], (self.x + self.player_spots_pos[i][0], self.y + self.player_spots_pos[i][1], PLAYER_SIZE, PLAYER_SIZE))
        
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, win):
        pass