import pygame
import config


class Boxer:
    def __init__(self):
        self.x, self.y = 0, 0
        self.sprite = None
        self.punched_count = 0
        self.punching = False
        self.action = "idle"
        self.delay = 0

    def idle(self):
        if self.delay == 0:
            self.action = "idle"
            self.set_sprite()

    def prep_punch_left(self):
        if self.delay == 0:
            self.action = "prep-punch-left"
            self.punching = True
            self.delay = 40
            self.set_sprite()

    def punch_left(self, other):
        self.action = "punch-left"
        self.delay = 40
        self.punching = False
        self.set_sprite()
        if not other.punched_left():
            self.delay = 80
        else:
            self.delay = 40

    def prep_punch_right(self):
        if self.delay == 0:
            self.action = "prep-punch-right"
            self.punching = True
            self.delay = 40
            self.set_sprite()

    def punch_right(self, other):
        self.action = "punch-right"
        self.punching = False
        self.set_sprite()
        if not other.punched_right():
            self.delay = 80
        else:
            self.delay = 40

    def block(self):
        if self.delay == 0:
            self.action = "block"
            self.delay = 50
            self.set_sprite()

    def dodge_left(self):
        if self.delay == 0:
            self.action = "dodge-left"
            self.delay = 30
            self.set_sprite()

    def dodge_right(self):
        if self.delay == 0:
            self.action = "dodge-right"
            self.delay = 30
            self.set_sprite()

    def punched_left(self):
        if self.action == "dodge-right":
            return False
        elif self.action == "block":
            self.punched_count += 0.25
            self.delay = 20
        else:
            self.punched_count += 1
            self.action = "punched-left"
            self.delay = 50
            self.punching = False
            self.set_sprite()
        return True

    def punched_right(self):
        if self.action == "dodge-left":
            return False
        elif self.action == "block":
            self.punched_count += 0.25
            self.delay = 20
        else:
            self.punched_count += 1
            self.action = "punched-right"
            self.delay = 50
            self.punching = False
            self.set_sprite()
        return True

    def update_action(self, other):
        self.delay = max(0, self.delay - 1)
        if self.delay != 0:
            return
        if self.punching:
            if self.action == "prep-punch-left":
                self.punch_left(other)
            elif self.action == "prep-punch-right":
                self.punch_right(other)
        else:
            self.idle()

    def render(self):
        raise NotImplementedError("Abstract instance used.")

    def set_sprite(self):
        raise NotImplementedError("Abstract instance used")
