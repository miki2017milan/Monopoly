from State import State
from Board import Board

class GameState(State):
    def __init__(self):
        self.board = Board()

    def tick(self):
        self.board.tick()

    def render(self, win):
        win.fill((220, 244, 222))

        self.board.render(win)