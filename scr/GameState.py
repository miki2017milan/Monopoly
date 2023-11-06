from State import State
from Board import Board

class GameState(State):
    def __init__(self):
        self.board = Board()

    def tick(self):
        self.board.tick()
        print("GameState")

    def render(self, win):
        win.fill((200, 50, 50))

        self.board.render(win)