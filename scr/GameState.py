import pygame as py

from scr.State import State
from scr.Board import Board
from scr.Player import Player

class GameState(State):
    def __init__(self):
        self.board = Board()
        self.players = [Player(0, 1)]

        self.cur_player = self.players[0]

        self.money_font = py.font.SysFont("Bahnschrift", 50, bold=True)

    def tick(self):
        self.board.tick()

        # if py.mouse.get_pressed()[0]:
        #     print(f"X: {py.mouse.get_pos()[0]}, Y: {py.mouse.get_pos()[1]}")

    def render(self, win):
        win.fill((220, 244, 222))

        # Render player information
        win.blit(self.money_font.render(f"Money: {self.cur_player.money}$", False, (0, 0, 0)), (0, 0))

        self.board.render(win)