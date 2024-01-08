import os, json

class Map:
    def __init__(self,map,x,y):
        self.map = map
        self.x = x
        self.y = y
    def PrintMap(self):
        os.system("cls")
        e = 0
        for i in self.map:
            Row = i
            if e == self.y:
                Row[self.x] = "[P]"
            Row = ''.join(Row)
            print(Row)
            e += 1
    def Move(self):
        movement = input()
        movement = movement.upper()
        x = self.x
        y = self.y
        if movement == "W":
            y -= 1
        if movement == "S":
            y += 1    
        if movement == "D":
            x += 1
        if movement == "A":
            x -= 1
        
        if not self.map[y][x] == "   " and not self.map[y][x] == "[#]":
            self.x = x
            self.y = y

        return xy
    def DetermineMapNum(Name):
        for i in range(len(data)):
            if Name == data[i]['name']:
                Num = i
                return Num

with open("Maps.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

xy = [0,0]                
Name = "Dark Purgatory"
Num = Map.DetermineMapNum(Name)
dungeon = data[Num]['map']
x = xy[0]
y = xy[1]
e = Map(dungeon,x,y)

for i in range(100):
    e.PrintMap()
    e.Move()