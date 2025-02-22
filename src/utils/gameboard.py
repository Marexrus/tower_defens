import pygame
from src.utils.constants import *
from src.utils.rect import *

gameboard=[]

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

def gameboard_init():
        global gameboard
        rx,ry=0,0
        for y in range(0,window_size[1],tile_size[1]):
            for x in range(0,window_size[0],tile_size[0]):
                relpos=[rx,ry]
                gameboard.append(Tile([x,y],relpos,0))
                rx+=1
            rx=0
            ry+=1
    
def gameboard_draw(screen):
    global gameboard
    for el in gameboard:
        if el.type == 0:
            pygame.draw.rect(screen,[255,255,255],[el.abspos[0],el.abspos[1],tile_size[0],tile_size[1]],2)
