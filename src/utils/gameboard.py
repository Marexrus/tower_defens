import pygame
from src.utils.constants import *
from src.utils.tile import *

gameboard=[]

def gameboard_init():
        global gameboard
        for y in range(0,window_size[1],tile_size[1]):
            for x in range(0,window_size[0],tile_size[0]):
                    gameboard.append(Tile([x,y],0))
    
def gameboard_draw(screen):
    global gameboard
    for el in gameboard:
        if el.type == 0:
            pygame.draw.rect(screen,[255,255,255],[el.pos[0],el.pos[1],tile_size[0],tile_size[1]],2)
