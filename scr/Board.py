class Board:
    def __init__(self):
        self.field = []

    def tick(self):
        pass

    def render(self, win):
        for f in self.field:
            f.render(win)