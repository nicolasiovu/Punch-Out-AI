import pygame
from sys import exit
import config
from fighters import Fighters

pygame.init()
clock = pygame.time.Clock()
fighters = Fighters()


def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        config.window.fill((0, 0, 0))

        config.window.blit(config.background, (0, 0))
        fighters.update_fighters()

        clock.tick(60)
        pygame.display.flip()


main()
