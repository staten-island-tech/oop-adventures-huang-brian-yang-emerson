import os

class Map:
    def __init__(self,map):
        self.map = map
    def PrintMap(self,map):
        os.system("cls")

        for i in range(map):
            for e in range(map[i]):
                print(map[i][e])
    
e = Map([[0,0,0,0,0]])