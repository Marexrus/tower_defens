import pygame
from src.utils.constants import *
from src.utils.rect import *
#from src.game.game import camera

#tile types
#0 - empty tile (tile for building towers)
#1 - way
#2 - obstacle
#3 - start
#4 - finish

class Tile:
    def __init__(self,abspos,relpos,type):
        self.abspos=abspos
        self.relpos=relpos
        self.type=type
        self.rect=Rect(self.abspos[0],self.abspos[1],tile_size[0],tile_size[1])

        camera_objects.append(self)
    
    def draw(self,screen):
        pygame.draw.rect(screen,[255,255,255],[self.abspos[0],self.abspos[1],tile_size[0],tile_size[1]])
        pygame.draw.rect(screen,[0,0,255],[self.abspos[0],self.abspos[1],tile_size[0],tile_size[1]],1)

def gameboard_init():
        global gameboard
        size=[-1000,-1000]
        rx,ry=size[0],size[1]
        for y in range(size[0],window_size[1],tile_size[1]):
            for x in range(size[1],window_size[0],tile_size[0]):
                relpos=[rx,ry]
                gameboard.append(Tile([x,y],relpos,0))
                rx+=1
            rx=0
            ry+=1
