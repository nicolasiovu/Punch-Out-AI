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


def main():
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
        scoreboard.render()

        clock.tick(60)
        pygame.display.flip()


main()
