import pygame as py
from scr.Assets import Assets
from scr.states.RollingSubState import RollingSubState

from scr.states.State import State
from scr.Board import Board

class GameState(State):
    def __init__(self):
        self.board = Board()

        self.rolling_sub_state = RollingSubState()

        self.sub_state = self.rolling_sub_state

    def tick(self):
        if self.sub_state is None:
            self.board.tick()
        else:
            temp = self.sub_state.tick()
            if temp:
                self.board.roll = temp
                self.sub_state.reset()
                self.sub_state = None

        # if py.mouse.get_pressed()[0]:
        #     print(f"X: {py.mouse.get_pos()[0]}, Y: {py.mouse.get_pos()[1]}")

    def render(self, win):
        win.fill((220, 244, 222))

        self.board.render(win)

        if self.sub_state:
            self.sub_state.render(win)
        else:
            win.blit(Assets.dices_imgs_small[self.board.roll[0] - 1], (1680, 960))
            win.blit(Assets.dices_imgs_small[self.board.roll[1] - 1], (1800, 960))