import pygame

win_height = 720
win_width = 1280
window = pygame.display.set_mode((win_width, win_height))
FONT = None
pygame.display.set_caption("Punch Out AI")


def init_font():
    global FONT
    FONT = pygame.font.SysFont("impact", 24)


background = pygame.image.load("assets/background.png")

opponent_sprites = \
    {"idle": pygame.image.load("assets/opponent_idle.png"),
     "block": pygame.image.load("assets/opponent_block.png"),
     "prep-punch-left": pygame.image.load("assets/opponent_prep_left.png"),
     "prep-punch-right": pygame.image.load("assets/opponent_prep_right.png"),
     "punch-left": pygame.image.load("assets/opponent_punch_left.png"),
     "punch-right": pygame.image.load("assets/opponent_punch_right.png"),
     "dodge-left": pygame.image.load("assets/opponent_dodge_left.png"),
     "dodge-right": pygame.image.load("assets/opponent_dodge_right.png"),
     "punched-left": pygame.image.load("assets/opponent_punched_left.png"),
     "punched-right": pygame.image.load("assets/opponent_punched_right.png")
     }

player_sprites = \
    {"idle": pygame.image.load("assets/player_idle.png"),
     "block": pygame.image.load("assets/player_block.png"),
     "prep-punch-left": pygame.image.load("assets/player_prep_left.png"),
     "prep-punch-right": pygame.image.load("assets/player_prep_right.png"),
     "punch-left": pygame.image.load("assets/player_punch_left.png"),
     "punch-right": pygame.image.load("assets/player_punch_right.png"),
     "dodge-left": pygame.image.load("assets/player_dodge_left.png"),
     "dodge-right": pygame.image.load("assets/player_dodge_right.png"),
     "punched-left": pygame.image.load("assets/player_punched_left.png"),
     "punched-right": pygame.image.load("assets/player_punched_right.png")
     }

player_score = pygame.image.load("assets/player_score.png")
opponent_score = pygame.image.load("assets/opponent_score.png")
