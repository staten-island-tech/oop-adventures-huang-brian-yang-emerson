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

def PrintMap():
        os.system("cls")
        e = 0
        for i in range(len(Map)):
            Row = Map[i]
            if e == StartY:
                Row[StartX] = "[P]"
            
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

Name = "Lobby"
Num = MapNum(Name)
Map = data[Num]['map']
StartX = data[Num]['StartX']
StartY = data[Num]['StartY']


Action = None

while Action != 0:
    PrintMap()
    print("1 ==> Change a unit")
    print("2 ==> Change Player Start Position")
    print("0 ==> Done")
    try:
        Action = int(input())
        if Action == 1:
            os.system("cls")
            PrintMap()
            print()
        elif Action == 2:
            x = None
            y = None

            while x == None:
                try:
                    x = int(input("New start x? "))
                except:
                    x = None
            while y == None:
                try:
                    y = int(input("New start x? "))
                except:
                    y = None


    except:
        Action = None

