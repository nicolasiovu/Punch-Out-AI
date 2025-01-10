import torch
from random import randint
from opponent import Opponent
from player import Player
from boxerai import BoxerAI


class Fighters:
    def __init__(self):
        self.player = Player()
        self.opponent = Opponent()
        self.ai_model = BoxerAI()

    def update_fighters(self):
        self.opponent.update_action(self.player)
        self.player.update_action(self.opponent)
        self.opponent.render()
        self.player.render()

    def get_player_score(self):
        return self.opponent.punched_count

    def get_opponent_score(self):
        return self.player.punched_count

    def next_round(self):
        self.player.punched_count = 0
        self.opponent.punched_count = 0

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
        state = self.encode_game_state()

        with torch.no_grad():
            action_prob = self.ai_model(state)

    def encode_game_state(self):
        player_movement = int(self.player.delay == 0)
        opponent_movement = int(self.opponent.delay == 0)

