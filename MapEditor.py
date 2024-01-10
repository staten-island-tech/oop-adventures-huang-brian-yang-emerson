import json, os

os.system("cls")

blocks = ["🌲 ","🧱║", ".🪨.","┳━┳"]

## Create Class for creating new dictionaries here
class MapEditor():
    def __init__(self,name,map,StartX,StartY):
        self.name = name
        self.map = map,
        self.StartX = StartX
        self.StartY = StartY

    def PrintMap(self):
            os.system("cls")
            e = 0
            for i in self.map:
                print(i)
                Row = i
                if e == self.StartY:
                    Row[self.StartX] = "[P]"
                
                Row = ''.join(Row)
                print(Row)
                e += 1

def MapNum(Name):
    for i in range(len(data)):
        if Name == data[i]['name']:
            Num = i
            return Num


with open("Maps.json", "r", encoding= 'utf-8') as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

Name = "END"
Num = MapNum(Name)
Map = data[Num]['map']
StartX = data[Num]['StartX']
StartY = data[Num]['StartY']
EditedMap = MapEditor(Name,Map,StartX,StartY)

Action = None

while Action != 0:
    EditedMap.PrintMap()
    input()

