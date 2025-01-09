import pygame

win_height = 720
win_width = 1280
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Punch Out AI")

background = pygame.image.load("assets/background.png")

opponent_idle = pygame.image.load("assets/opponent_idle.png")
player_idle = pygame.image.load("assets/player_ide.png")
