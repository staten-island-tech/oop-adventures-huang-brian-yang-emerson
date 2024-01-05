import os, json

class Map:
    def __init__(self,map):
        self.map = map
    def PrintMap(self):
        os.system("cls")
        for i in self.map:
            print(str(i))
    def Move(self):
        movement = input()
        movement = movement.upper()
        x = xy[0]
        y = xy[1]
        if movement == "W":
            y -= 1
            if y < 0:
                y += 1
        if movement == "S":
            y += 1
            if y > len(self.map)-1:
                y -= 1            
        if movement == "D":
            x += 1
            if x > len(self.map[y])-1:
                x -= 1
        if movement == "A":
            x -= 1
            if x < 0:
                x += 1
        if not self.map[y][x] == "[#]":
            xy[0] = x
            xy[1] = y

        return xy
        
    def PrintRow(Text):
        print(f"", end="", flush=True) 
        for char in Text:
            print(char, end="", flush=True)

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

for i in range(100):
    x = xy[0]
    y = xy[1]
    Name = "Desert Pyramid"
    Num = Map.DetermineMapNum(Name)
    dungeon = data[Num]['map']
    dungeon[y][x] = "[P]"

    e = Map(dungeon)
    e.PrintMap()
    xy = e.Move()