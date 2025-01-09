from opponent import Opponent
from player import Player


class Fighters:
    def __init__(self):
        self.player = Player()
        self.opponent = Opponent()

    def update_fighters(self):
        self.opponent.render()
        self.player.render()
