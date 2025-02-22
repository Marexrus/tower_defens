from src.utils.constants import *
from src.objects.towers import *
from src.utils.gameboard import *

class Camera:
    def __init__(self,pos,scale):
        self.pos=pos
        self.scale=scale
        self.camera_speed=4
        self.full_move=[0,0]
    
    def move(self,move_coords):
        self.pos[0]+=move_coords[0]
        self.pos[1]+=move_coords[1]

        for el in camera_objects:
            el.abspos[0]-=move_coords[0]
            el.abspos[1]-=move_coords[1]
    
    def control(self,keys):
        if keys[pygame.K_w]:  # Движение вверх
            self.full_move[1] -= self.camera_speed
        if keys[pygame.K_s]:  # Движение вниз
            self.full_move[1] += self.camera_speed
        if keys[pygame.K_a]:  # Движение влево
            self.full_move[0] -= self.camera_speed
        if keys[pygame.K_d]:  # Движение вправо
            self.full_move[0] += self.camera_speed
        
        self.move(self.full_move)
        self.full_move=[0,0]
    
    def update_scale(self,scale,mpos,increase):
        tile_size[0]*=scale
        tile_size[1]*=scale
        for el in camera_objects:
            if type(el) == Tower:
                el.size[0]*=scale
                el.size[1]*=scale
                el.abspos[0]*=scale
                el.abspos[1]*=scale
            elif type(el) == Tile:
                el.abspos[0]*=scale
                el.abspos[1]*=scale
        if increase:
            self.move([mpos[0]/10,mpos[1]/10])
        else:
            self.move([-mpos[0]/10,-mpos[1]/10])