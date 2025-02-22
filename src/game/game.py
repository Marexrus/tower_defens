import pygame
from src.utils.constants import *
from src.utils.rect import *
from src.ui.widgets import *
from src.objects.towers import *
from src.game.camera import *
from src.utils.gameboard import *


class Game:
    def __init__(self):
        self.screen = pygame.display.set_mode(window_size,pygame.NOFRAME)
        self.clock = pygame.time.Clock()
        self.button=Button(self.screen,lambda:print(1),Rect(200,200,100,100),"hello")
        self.mrect=None

    def run(self):
        gameboard_init()
        camera=Camera([0,0],1)
        camera.move([-200,-200])
        Tower('archecrs',1,[0,0])

        running = True
        while running:
            mpos=pygame.mouse.get_pos()
            self.mrect=Rect(10000,10000,1,1)
            scale=1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.mrect=Rect(mpos[0],mpos[1],1,1)
                if event.type == pygame.MOUSEWHEEL:
                    # Обработка прокрутки колесика мыши
                    if event.y > 0:
                        scale+=0.1
                        camera.update_scale(scale,mpos,True)
                    elif event.y < 0:
                        scale-=0.1
                        camera.update_scale(scale,mpos,False)
            keys = pygame.key.get_pressed()
            camera.control(keys)

            self.screen.fill((58, 58, 58))

            for el in gameboard:
                el.draw(self.screen)
                if el.rect.colliderect(self.mrect):
                    print(f"{el.relpos}---{el.abspos}")
            for el in towers:
                el.update(self.screen)

            """label(self.screen,"Helo world",[100,100])
            self.button.draw()

            if self.mrect:
                self.button.check(self.mrect)"""
                
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()