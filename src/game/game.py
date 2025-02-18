import pygame
from src.utils.constants import *

FPS=144

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600),pygame.NOFRAME)
        self.clock = pygame.time.Clock()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill((58, 58, 58))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()