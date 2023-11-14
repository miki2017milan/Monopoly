import random as r
import pygame as py

from scr.states.State import State
from scr.Assets import Assets

class RollingSubState(State):
    def __init__(self):
        self.dices = [r.randint(1, 6), r.randint(1, 6)]

        self.roll_times = r.randint(5, 8)
        self.roll_btw_time = r.randint(5, 10)
        self.roll_btw_time_counter = self.roll_btw_time

        self.wait_time = 120

        # Dice overlay
        self.blackoverlay = py.Surface((1920, 1080))
        self.blackoverlay.set_alpha(128)
        self.blackoverlay.fill((0, 0, 0))

    def tick(self):
        self.roll_btw_time_counter -= 1

        if self.roll_times <= 0:
            if self.wait_time <= 0:
                return self.dices
            self.wait_time -= 1
        else:
            if self.roll_btw_time_counter <= 0:
                self.roll_btw_time += r.randint(5, 10)
                self.roll_btw_time_counter = self.roll_btw_time
                self.roll_times -= 1
                self.dices = [r.randint(1, 6), r.randint(1, 6)]

    def reset(self):
        self.roll_times = r.randint(5, 8)
        self.roll_btw_time = r.randint(5, 10)
        self.roll_btw_time_counter = self.roll_btw_time

        self.wait_time = 60

    def render(self, win):
        win.blit(self.blackoverlay, (0, 0))

        win.blit(Assets.dices_imgs[self.dices[0] - 1], (410, 315))
        win.blit(Assets.dices_imgs[self.dices[1] - 1], (1060, 315))