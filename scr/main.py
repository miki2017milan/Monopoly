import pygame as py

from GameState import GameState
from MenuState import MenuState
from State import State

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