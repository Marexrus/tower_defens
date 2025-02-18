import pygame
from src.utils.constants import *
from src.utils.rect import *
from src.ui.widgets import *

FPS=144

class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 600),pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.button=Button(self.screen,lambda:print(1),Rect(200,200,100,100),"hello")
        self.mrect=None

    def run(self):
        running = True
        while running:
            self.mrect=None
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mrect=Rect(pygame.mouse.get_pos()[0],pygame.mouse.get_pos()[1],1,1)


            self.screen.fill((58, 58, 58))

            label(self.screen,"Helo world",[100,100])
            self.button.draw()

            if self.mrect:
                self.button.check(self.mrect)
                
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()