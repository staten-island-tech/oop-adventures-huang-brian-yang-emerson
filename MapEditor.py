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
    print("Start Position = ("+str(StartX)+","+str(StartY)+")")

    print("1 ==> Change a unit")
    print("2 ==> Change Player Start Position")
    print("0 ==> Done")
    try:
        Action = int(input())
        if Action != 0:
            x = None
            y = None
            while x == None:
                try:
                    x = int(input("x? "))
                except:
                    x = None
            while y == None:
                try:
                    y = int(input("y? "))
                except:
                    y = None

        try:
            print(Map[y][x])
        except:
            Action = None

        if Action == 1:
            os.system("cls")
            PrintMap()
            print('1: "[ ]"')
            print('2: "   "')
            print("3: Change Block")
            print("4: Add NPC")
            e = None

            while e == None:
                try:
                    e = int(input())
                    if e == 1:
                        Map[y][x] = "[ ]"
                    if e == 2:
                        Map[y][x] = "   "
                    if e == 3:
                        os.system("cls")
                        print(blocks)
                        print("0~"+str(len(blocks)-1))
                        e = int(input())
                        Map[y][x] = blocks[e]
                
                except:
                    os.system("cls")
                    e = None


        elif Action == 2:
            if Map[y][x] == "[ ]":
                StartX = x
                StartY = y


    except:
        Action = None

newdungeon = MapEditor(Name,Map,StartX,StartY)

data[Num]['map'] = newdungeon.map
data[Num]['StartX'] = newdungeon.StartX
data[Num]['StartY'] = newdungeon.StartY

with open('Saves.json', mode='w') as outfile:
    json.dump(data, outfile, indent=4)

exit()
