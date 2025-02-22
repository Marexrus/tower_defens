import pygame
from src.utils.constants import *
from src.utils.rect import *
from src.utils.gameboard import *
from src.ui.widgets import *

FPS=144

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(window_size,pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.button=Button(self.screen,lambda:print(1),Rect(200,200,100,100),"hello")
        self.mrect=None

    def run(self):
        gameboard_init()

        running = True
        while running:
            self.mrect=Rect(10000,10000,1,1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mrect=Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)


            self.screen.fill((58, 58, 58))
            gameboard_draw(self.screen)

            for el in gameboard:
                if el.rect.colliderect(self.mrect):
                    print(el.relpos)

            """label(self.screen,"Helo world",[100,100])
            self.button.draw()

            if self.mrect:
                self.button.check(self.mrect)"""
                
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()