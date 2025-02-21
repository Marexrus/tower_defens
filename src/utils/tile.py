#tile types
#0 - empty tile (tile for building towers)
#1 - way
#2 - obstacle
#3 - start
#4 - finish

class Tile:
    def __init__(self,pos,type):
        self.pos=pos
        self.type=type