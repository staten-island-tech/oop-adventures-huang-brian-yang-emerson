import json

def SaveSlot(SaveSlot, Dictionary):

    with open('saves.json', mode='r') as infile:
        data = json.load(infile) 

    data[SaveSlot] = Dictionary

    with open('saves.json', mode='w') as outfile:
        json.dump(data, outfile, indent=4)

def GetSave(SaveSlot):
    
    with open('saves.json', mode='r') as infile:
        data = json.load(infile)
    
    return data[SaveSlot]

def GetAllSave():
    
    with open('saves.json', mode='r') as infile:
        data = json.load(infile)
    
    return data