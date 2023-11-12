from fields.Field import Field

class TreasureField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placement_offset: tuple):
        super().__init__(x, y, width, height, player_placement_offset)

    def on_land(self, player):
        print("landed on treasure field")

    def render_extra_information(self, win):
        pass

    def tick(self):
        self.reset_click()