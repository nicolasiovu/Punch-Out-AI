import config
from boxer import Boxer


class Player(Boxer):
    def __init__(self):
        super().__init__()
        self.x, self.y = 525, 300
        self.set_sprite()

    def set_sprite(self):
        if self.action == "idle":
            self.sprite = config.player_idle
        else:
            pass

    def render(self):
        config.window.blit(self.sprite, (self.x, self.y))
