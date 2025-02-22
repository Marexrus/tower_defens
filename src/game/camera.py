from src.utils.constants import *

class Camera:
    def __init__(self,pos,scale):
        self.pos=pos
        self.scale=scale
    
    def update(self,move_coords):
        self.pos[0]+=move_coords[0]
        self.pos[1]+=move_coords[1]

        for el in camera_objects:
            el.abspos[0]-=move_coords[0]
            el.abspos[1]-=move_coords[1]