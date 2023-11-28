import DialogueService, SaveService, time

def MainMenu():
    SaveSlotsData: list[dict] = SaveService.GetAllSave()

    if len(SaveSlotsData) == 0:
        print("No Slots Available. Creating New Save Slot...")
        time.sleep(3)
        data = SaveService.NewSaveSlot()

    else:
        DialogueService.Dialogue("", "You Have Previous Save Sessions, Would You Like To Display Them?", 0.05)
        Answer = input("\nY/N: ").lower()

        while Answer != 'y' and Answer != 'n':
            Answer = input("Y/N (only): ").lower()

        if Answer == 'y':
            list = []
            for n in SaveSlotsData:
                list.append(
                    {
                        'Name': n['Name'],
                        'Day': n['Day'],
                        'Population': n['Population'],
                        'Happiness': n['Happiness'],
                        'Gold': n['Gold']
                    }
                )
                
            for entry in list:
                print(entry)

            DialogueService.Dialogue("", f"Exit Or Choose Save Slot? (E / 1 - {len(SaveSlotsData)})", 0.05)
            Answer = input("Input: ").lower()

        else:
            data = SaveService.NewSaveSlot()

    return data

def tutorial():
    pass