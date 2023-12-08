import os

class Map:
    def __init__(self,map):
        self.map = map
    def PrintMap(self):
        os.system("cls")
        for i in self.map:
            print(''.join(i))
    def Move(self):
        movement = input().upper
        if movement == "W":
            y = xy[1]
            xy[1] = y - 1
        if movement == "S":
            y = xy[1]
            xy[1] = y + 1
        if movement == "D":
            xy[0] += 1
        if movement == "A":
            xy[0] -= 1
        return xy
        

xy = [0,0]                

for i in range(5):
    x = xy[0]
    y = xy[1]

    Template = [["#" for i in range(5)] for i in range(5)]
    Template[x][y] = "P"

    e = Map(Template)
    e.PrintMap()
    xy = e.Move()