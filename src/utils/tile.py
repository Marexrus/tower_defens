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