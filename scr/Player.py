import pygame as py

START_MONEY = 5000

class Player:
    def __init__(self, pos, index):
        self.pos = pos
        self.index = index

        self.money = START_MONEY
        self.streets = []

    def tick(self):
        pass