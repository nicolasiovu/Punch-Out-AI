from random import randint
from opponent import Opponent
from player import Player


class Fighters:
    def __init__(self):
        self.player = Player()
        self.opponent = Opponent()

    def update_fighters(self):
        self.opponent.update_action(self.player)
        self.player.update_action(self.opponent)
        self.opponent.render()
        self.player.render()
        print("SCORE: OPPONENT: " + str(self.player.punched_count) + " | PLAYER: " + str(self.opponent.punched_count))

    def get_player_score(self):
        return self.opponent.punched_count

    def get_opponent_score(self):
        return self.player.punched_count

    def set_player_move(self, move):
        if move == "block":
            self.player.block()
        elif move == "dodge-left":
            self.player.dodge_left()
        elif move == "dodge-right":
            self.player.dodge_right()
        elif move == "punch-left":
            self.player.prep_punch_left()
        elif move == "punch-right":
            self.player.prep_punch_right()
        elif move == "idle":
            self.player.idle()

    def set_opponent_move(self):
        move = randint(0, 6)
        if move == 0:
            self.opponent.block()
        elif move == 1:
            self.opponent.dodge_left()
        elif move == 2:
            self.opponent.dodge_right()
        elif move == 3:
            self.opponent.prep_punch_left()
        elif move == 4:
            self.opponent.prep_punch_right()
        elif move == 5:
            self.opponent.idle()
