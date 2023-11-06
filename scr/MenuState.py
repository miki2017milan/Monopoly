from State import State

class MenuState(State):
    def __init__(self):
        pass

    def tick(self):
        print("MenuState")

    def render(self, win):
        win.fill((50, 200, 50))