import pygame
import config


class Boxer:
    def __init__(self):
        self.x, self.y = 0, 0
        self.sprite = None
        self.punched_count = 0
        self.action = "idle"
        self.delay = 0

    def punch_left(self, other):
        if self.delay == 0:
            other.punched_left()
            self.action = "punch"
            self.delay = 100

    def punch_right(self, other):
        if self.delay == 0:
            other.punched_right()
            self.action = "punch"
            self.delay = 100

    def block(self):
        if self.delay == 0:
            self.action = "block"

    def dodge_left(self):
        if self.delay == 0:
            self.action = "dodge-left"
            self.delay = 75

    def dodge_right(self):
        if self.delay == 0:
            self.action = "dodge-right"
            self.delay = 75

    def punched_left(self):
        if self.action == "dodge-right":
            return
        elif self.action == "block":
            self.punched_count += 0.25
            self.delay = 50
        else:
            self.punched_count += 1
            self.delay = 100

    def punched_right(self):
        if self.action == "dodge-left":
            return
        elif self.action == "block":
            self.punched_count += 0.25
            self.delay = 50
        else:
            self.punched_count += 1
            self.delay = 100

    def render(self):
        raise NotImplementedError("Abstract instance used.")

    def set_sprite(self):
        raise NotImplementedError("Abstract instance used")
