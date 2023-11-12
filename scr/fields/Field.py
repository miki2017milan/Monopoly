import pygame as py

from abc import ABC, abstractmethod

PLAYER_COLORS = [(200, 50, 50), (50, 200, 50), (50, 50, 200), (200, 50, 200)]
PLAYER_SIZE = 30

class Field(ABC):
    def __init__(self, x: int, y: int, width: int, height: int, player_placment_offset: int):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.player_spots = [0, 0, 0, 0]

        # Calculate player spots
        space_x = int((width - PLAYER_SIZE * 2) / 3)
        space_y = int(((height - player_placment_offset) - PLAYER_SIZE * 2) / 3)
        self.player_spots_pos = ((space_x, space_y + player_placment_offset), # Top-left
                                 (space_x * 2 + PLAYER_SIZE, space_y + player_placment_offset), # Top-right
                                 (space_x, space_y * 2 + PLAYER_SIZE + player_placment_offset), # Bottom-left
                                 (space_x * 2 + PLAYER_SIZE, space_y * 2 + PLAYER_SIZE + player_placment_offset)) # Bottom-right

        self.can_click = True
        self.is_selected = False
        self.owner = 0

        # Transperent overlay when selected
        self.overlay = py.Surface((self.width, self.height))
        self.overlay.set_alpha(128)
        self.overlay.fill((30, 30, 30))

    def is_clicked(self) -> bool:
        mx, my = py.mouse.get_pos()

        if self.x + self.width > mx > self.x and self.y + self.height > my > self.y and self.can_click and py.mouse.get_pressed()[0]:
            self.can_click = False
            return True
        return False
        
    def reset_click(self):
        if not py.mouse.get_pressed()[0]:
            self.can_click = True

    def add_player(self, player: int):
        for i, s in enumerate(self.player_spots):
            if s == 0:
                self.player_spots[i] = player
                return
            
        raise Exception("Could't add another player to the field.")
    
    def remove_player(self, player):
        if player in self.player_spots:
            self.player_spots.pop(self.player_spots.index(player))
            self.player_spots.append(0)
    
    def render(self, win):
        if self.is_selected:
            win.blit(self.overlay, (self.x, self.y))

        # Draw players
        for i, p in enumerate(self.player_spots):
            if not p == 0:
                py.draw.ellipse(win, PLAYER_COLORS[p - 1], (self.x + self.player_spots_pos[i][0], self.y + self.player_spots_pos[i][1], PLAYER_SIZE, PLAYER_SIZE)) 

        self.render_extra_information(win)

    @abstractmethod
    def on_land(self, player):
        pass

    @abstractmethod
    def render_extra_information(self, win):
        pass
        
    @abstractmethod
    def tick(self):
        pass

    