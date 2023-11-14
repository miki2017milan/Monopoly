from scr.fields.Field import Field

class EmptyField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placement_offset: tuple):
        super().__init__(x, y, width, height, player_placement_offset)
    
    def tick(self):
        self.reset_click()

    def on_land(self, player):
        print("landed on empty field")

    def render_extra_information(self, win):
        pass
