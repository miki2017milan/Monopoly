import pygame as py

from State import State
from Board import Board
from Player import Player

class GameState(State):
    def __init__(self):
        self.board = Board()
        self.players = [Player(0, 1)]

        self.cur_player = self.players[0]

    def tick(self):
        self.board.tick()

        # print(f"X: {py.mouse.get_pos()[0]}, Y: {py.mouse.get_pos()[1]}")

    def render(self, win):
        win.fill((220, 244, 222))

        self.board.render(win)