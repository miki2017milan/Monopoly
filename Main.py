import pygame as py

from scr.GameState import GameState
from scr.MenuState import MenuState
from scr.Assets import Assets
from scr.State import State

py.init()

class Main:
    def __init__(self):
        # Window
        self.WIDTH = 1920
        self.HEIGHT = 1080

        self.win = py.display.set_mode((self.WIDTH, self.HEIGHT))
        py.display.set_caption("Monopoly")

        # Tick
        self.clock = py.time.Clock()
        self.FPS = 60
        self.running = True

        Assets.load()

        # States
        self.game_state = GameState()
        self.menu_state = MenuState()

        State.switch_state(self.game_state)

    def tick(self):
        for e in py.event.get():
            if e.type == py.QUIT:
                self.running = False
            if e.type == py.KEYDOWN:
                if e.key == py.K_ESCAPE:
                    State.switch_state(self.menu_state)
                    # self.game_state.board.fields[0].remove_player(3)

        State.get_state().tick()

        self.clock.tick(self.FPS)

    def render(self):
        # Filling Background
        self.win.fill((200, 200, 200))
            
        State.get_state().render(self.win)
        
        py.display.update()

    def run(self):
        while self.running:
            self.render()
            self.tick()

        py.quit()
        exit()

if __name__ == "__main__":
    main = Main()
    main.run()