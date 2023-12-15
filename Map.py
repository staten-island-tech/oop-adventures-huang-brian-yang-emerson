import os

class Map:
    def __init__(self,map):
        self.map = map
    def PrintMap(self):
        os.system("cls")
        for i in self.map:
            print(''.join(i))
    def Move(self):
        movement = input()
        movement = movement.upper()
        x = xy[0]
        y = xy[1]
        if movement == "W":
            y -= 1
        if movement == "S":
            y += 1
        if movement == "D":
            x += 1
        if movement == "A":
            x -= 1
        if not self.map[y]:
            a == "#":
                xy[0] = x
                xy[1] = y

        return xy
        
        

xy = [0,0]                

for i in range(100):
    x = xy[0]
    y = xy[1]

    Template = [["." for i in range(10)] for i in range(5)]
    Template[4] = ["#" for i in range(10)]
    Template[3][3] = "#"
    Template[y][x] = "P"

    e = Map(Template)
    e.PrintMap()
    xy = e.Move()