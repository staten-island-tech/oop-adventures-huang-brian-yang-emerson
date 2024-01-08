import json, os

os.system("cls")

## Create Class for creating new dictionaries here
class MapMaker():
    def __init__(self,name,map):
        self.name = name
        self.map = map

def MakeMap():
    Map = [[]]
    Action = None
    RowNum = 0
    while Action != 0:
        PrintMap(Map)
    
        print("1 = Add a path")
        print("2 = Add a gap")
        print("3 = Add a wall")
        print("8 = Delete Row")
        print("9 = Next Row")
        print("0 = Done")
        print()

        try:
            Action = int(input())

            if Action == 1:
                Map[RowNum].append("[ ]")
            if Action == 2:
                Map[RowNum].append("   ")
            if Action == 3:
                Map[RowNum].append("[#]")
            if Action == 8:
                Map[RowNum] = []
            if Action == 9:
                Map.append([])
                RowNum += 1

        except:
            print("ERROR")
            input()
    
    return Map

def PrintMap(Map):
    os.system("cls")
    for i in range(len(Map)):
        Row = ''.join(Map[i])
        Row = Row+"\n"
        print(f"", end="", flush=True)
        for char in Row:
            print(char, end="", flush=True)


def Fix():
    Longest = DetermineLongest()
    for i in range(len(Map)):
        for e in range(Longest - len(Map[i])):
            Map[i].append("   ")
            print(Map[i])
    
    return Map

def DetermineLongest():
    Longest = 0

    for i in range(len(Map)):
        if len(Map[i]) > Longest:
            print("True")
            Longest = len(Map[i])
    
    return Longest

#print(f"{Author}: ", end="", flush=True)
#	for char in Text:
#		print(char, end="", flush=True)
#		time.sleep(Time)

with open("Maps.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

os.system("cls")

Name = input("Give a name... ")
Map = MakeMap()
Map = Fix()
PrintMap(Map)


Dungeon = MapMaker(Name,Map)
data.append(Dungeon.__dict__)
print(Dungeon.__dict__)

#No code needed below this line
# Creates a new JSON file with the updated data
new_file = "updated.json"
with open(new_file, "w") as f:
    # Serialize the updated Python list to a JSON string
    json_string = json.dumps(data, indent=4)
    # Write the JSON string to the new JSON file
    f.write(json_string)


# Overwrite the old JSON file with the new one
os.remove("Maps.json")
os.rename(new_file, "Maps.json")