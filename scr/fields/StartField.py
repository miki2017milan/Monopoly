from scr.fields.Field import Field

class StartField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placement_offset: tuple):
        super().__init__(x, y, width, height, player_placement_offset)

    def tick(self):
        self.reset_click()

    def on_land(self, player):
        player.add_money(400)

    def render_extra_information(self, win):
        pass