import config
from boxer import Boxer


class Opponent(Boxer):
    def __init__(self):
        super().__init__()
        self.x, self.y = 650, 50
        self.set_sprite()

    def set_sprite(self):
        self.sprite = config.opponent_sprites.get(self.action)

    def render(self):
        config.window.blit(self.sprite, (self.x, self.y))
