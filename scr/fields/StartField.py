from fields.Field import Field

class StartField(Field):
    def __init__(self, x: int, y: int, width: int, height: int, player_placment_offset: int):
        super().__init__(x, y, width, height, player_placment_offset)

    def on_land(self, player):
        player.add_money(400)

    def render_extra_information(self, win):
        pass

    def tick(self):
        self.reset_click()