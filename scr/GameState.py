import pygame as py

from State import State
from Board import Board
from Player import Player

class GameState(State):
    def __init__(self):
        self.board = Board()

    def tick(self):
        self.board.tick()

        # print(f"X: {py.mouse.get_pos()[0]}, Y: {py.mouse.get_pos()[1]}")

    def render(self, win):
        win.fill((220, 244, 222))

        self.board.render(win)