from src.utils.constants import *
from src.utils.rect import *
import pygame

class Tower:
    def __init__(self,type,level,relpos):
        self.type=type
        self.level=level
        self.relpos=relpos
        self.size=[40,40]

        self.abspos=[self.relpos[0]*tile_size[0],self.relpos[1]*tile_size[1]]

        towers.append(self)
        camera_objects.append(self)

        if self.type == 'archers':
            self.hp=100
            self.damage=10
            self.fire_rate=1
    def update(self,screen):
        #self.abspos[0]=gameboard
        self.rect=Rect(self.abspos[0],self.abspos[1],self.size[0],self.size[1])
        pygame.draw.rect(screen,[255,0,0],self.rect.prect)