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

    with open('saves.json', mode='r') as infile:
        data: list[dict] = json.load(infile)
    
    data.append(
        {
            "Name": Name,
            "Day": 0,
            "Happiness": 50,
            "Luck": 0,
            "Population": 50,
            "Gold": 50, 
        }
    )

    with open('saves.json', mode='w') as outfile:
        json.dump(data, outfile, indent=4)

    print("New Slot Saved!")

    return len(data)

def SaveSlot(SaveSlot, Dictionary):

    with open('saves.json', mode='r') as infile:
        data = json.load(infile) 

    data[SaveSlot] = Dictionary

    with open('saves.json', mode='w') as outfile:
        json.dump(data, outfile, indent=4)

def GetSave(SaveID):
    
    with open('saves.json', mode='r') as infile:
        data = json.load(infile)
    
    return data[SaveID - 1]

def GetAllSave():
    
    with open('saves.json', mode='r') as infile:
        data = json.load(infile)
    
    return data

def DeleteSlot(SlotID):
    Data: list[dict] = GetAllSave()
    Data.pop(SlotID)

    with open('saves.json', mode='w') as outfile:
        json.dump(Data, outfile, indent=4)