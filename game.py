import time
import pygame
import pygame.freetype
from sys import exit
import config
from fighters import Fighters
from scoreboard import Scoreboard

pygame.init()
config.init_font()
clock = pygame.time.Clock()
fighters = Fighters()
scoreboard = Scoreboard(fighters)
fighters.set_scoreboard(scoreboard)


def run():
    last_time = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            move = "dodge-left"
        elif keys[pygame.K_d]:
            move = "dodge-right"
        elif keys[pygame.K_SPACE]:
            move = "block"
        elif keys[pygame.K_q]:
            move = "punch-left"
        elif keys[pygame.K_e]:
            move = "punch-right"
        else:
            move = "idle"
        fighters.set_player_move(move)
        fighters.set_opponent_move()

        config.window.fill((0, 0, 0))

        config.window.blit(config.background, (0, 0))
        fighters.update_fighters()
        fighters.record_ai_experience()
        scoreboard.render()

        current_time = time.time()
        if current_time - last_time >= 1:
            scoreboard.tick_timer()
            if scoreboard.timer == 0:
                return
            last_time = current_time

        clock.tick(60)
        pygame.display.flip()


def between_round():
    trained = False

    countdown = 10
    last_time = time.time()
    BIG_FONT = pygame.font.SysFont("impact", 72)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        config.window.fill((0, 0, 0))
        config.window.blit(config.background, (0, 0))

        config.window.blit(config.next_round, (294, 340))
        start_time = BIG_FONT.render(str(countdown), False, (74, 107, 189))
        config.window.blit(start_time, (996, 334))

        if not trained:
            fighters.train_ai()
            trained = True

        current_time = time.time()
        if current_time - last_time >= 1:
            countdown -= 1
            last_time = current_time
            if countdown == 0:
                scoreboard.next_round()
                return

        clock.tick(60)
        pygame.display.flip()


while True:
    run()
    if scoreboard.round < 4:
        between_round()
    else:
        break
