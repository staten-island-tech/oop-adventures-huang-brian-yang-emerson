import json, DialogueService, os

def NewSaveSlot():
    DialogueService.Dialogue("", "Creating New Save Slot...", 0.05)

    Confirm = False
    
    while Confirm == False:
        os.system("cls")
        Name = input("\nPlease Choose A Name (Psst! This CANNOT be changed later in the game!): ")

        AConfirm = input(f"You Chose: {Name}. Are You Sure? (Y/N): ").lower()

        while AConfirm != "y" and AConfirm != "n":
            AConfirm = input(f"Y/N Only: ").lower()
            
        if AConfirm == "y":
            Confirm = True


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