import torch
from random import randint
from opponent import Opponent
from player import Player
from boxerai import BoxerAI
from boxerai import State
from actions import Actions


class Fighters:
    def __init__(self):
        self.player = Player()
        self.opponent = Opponent()
        self.boxer_ai = BoxerAI()
        self.scoreboard = None

    def set_scoreboard(self, scoreboard):
        self.scoreboard = scoreboard

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
        if self.opponent.delay != 0:
            return
        state = State(Actions.str_to_action.get(self.player.action),
                      Actions.str_to_action.get(self.opponent.action),
                      self.player.delay,
                      self.opponent.delay,
                      self.opponent.punched_count - self.player.punched_count
                      )
        action = self.boxer_ai.get_action(state)
        move = Actions.action_to_str.get(action)
        if move == "block":
            self.opponent.block()
        elif move == "dodge-left":
            self.opponent.dodge_left()
        elif move == "dodge-right":
            self.opponent.dodge_right()
        elif move == "punch-left":
            self.opponent.prep_punch_left()
        elif move == "punch-right":
            self.opponent.prep_punch_right()
        elif move == "idle":
            self.opponent.idle()

    def record_ai_experience(self):
        state = State(Actions.str_to_action.get(self.player.action),
                      Actions.str_to_action.get(self.opponent.action),
                      self.player.delay,
                      self.opponent.delay,
                      self.player.punched_count - self.opponent.punched_count
                      )
        self.boxer_ai.record_experience(state)

    def train_ai(self):
        self.boxer_ai.train()
