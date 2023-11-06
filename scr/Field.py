import pygame as py

from abc import ABC, abstractmethod

class Field(ABC):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.can_click = True

    def is_clicked(self):
        mx, my = py.mouse.get_pos()
        if self.x + self.width > mx > self.x and self.y + self.height > my > self.y and self.can_click and py.mouse.get_pressed()[0]:
            self.can_click = False
            return True
        
    def reset_click(self):
        if not py.mouse.get_pressed()[0]:
            self.can_click = True
        
    @abstractmethod
    def tick(self):
        pass

    @abstractmethod
    def render(self, win):
        pass