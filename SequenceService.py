import DialogueService, SaveService

def MainMenu():
    SaveSlotsData: list[dict] = SaveService.GetAllSave()

    if len(SaveSlotsData) == 0:
        DialogueService.Dialogue("", "You Dont Have A Previous Save Session. Would You Like To Make A New Save Slot?", 0.05)
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


        