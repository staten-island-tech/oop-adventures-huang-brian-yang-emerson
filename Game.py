import time, os, random, json
from itertools import cycle

def Dialogue(Author, Text, Time):
    for char in Text:
        print(f"{Author}: " + char)
        time.sleep(Time)

def Answer(Options: list):
    Confirmaton = input(f"{'/'.join(Options)}: ").upper()

    while Confirmaton not in Options:
        Confirmaton = input(f"{'/'.join(Options)}: ").upper()
    
    return Options.index(Confirmaton)

def CoolBoxDialogue(ListOfDialogue: list[str], AvailableActions: list[str], ActionOAnswer, MaxLength):
    print("╔" + "═"*(MaxLength-1) + "╗")

    for dialogue in ListOfDialogue:
        NeededLine = (MaxLength - len(dialogue) - 1) * " " + "║"
        print(f"║{dialogue}" + NeededLine)

    print(f"║" + " "*(MaxLength-1) + "║")
    print("║Available Actions:" + " "*(MaxLength - 19) + "║")

    for Action in AvailableActions:
        print(f"║{Action}" + " "*(MaxLength - len(Action) - 1) + "║" )

    print(f"║" + " "*(MaxLength-1) + "║")
    print(f"╚" + "═"*(MaxLength-1) + "╝")

    return Answer(ActionOAnswer)
    
class Game:
    def __init__(self):
        self.loading_done = False
        pass

    # << Main Menu Functions >> #
    def Information(self):
        print("Information: Clean Up On Isle 9 Please".center(80))
        print("Press enter to return to the main menu.".center(80))
        input()
        self.MainMenu() 
    
    def FuturePlans(self):
        print("Future Plans As Of Currently:".center(80))
        print("1. Finish The Game".center(80))
        print("Press enter to return to the main menu.".center(80))
        input()
        self.MainMenu()
    
    def Load(self, Message, LTS, tip):
            LoadingSprites = ['|', '/', '-', '\\', '|', '/', '-', '\\']
            LT = 0
            for i in cycle(LoadingSprites):
                if LT != LTS:
                    os.system('cls')
                    print(f"{i} {Message} {i}\n {tip}".center(80), end="")
                    time.sleep(0.5)
                    LT += 1
                elif LT == LTS:
                    os.system('cls')
                    self.loading_done = True
                    break

    def MainMenu(self):
        if not self.loading_done:
            self.Load("Loading Game...", 25, "Please Feel Free To Close The Program During This Process.")
        
        os.system("cls")

        dialogues = [
            "Welcome To --> Genric text dengen gme",
            "Possibly The Worst Game You'll Ever Play",
            "Please Feel Free To Exit The Game Anytime And Anywhere",
            "Options For The Main Menu:"
        ]

        actions = [
            "P - Play",
            "I - Info",
            "F - Future Plans",
            "E - Exit The Game <--- (Psst. This One)"
        ]

        answers = ["P", "I", "F", "E"]

        MainMenuChoice = CoolBoxDialogue(dialogues, actions, answers, 80)

        if MainMenuChoice == 0:
            Tips = [
                "Please Try To Exit The Game As Soon As Possible",
                "Don't chew Double Trouble Gum while running! Unless you've had years of didgeridoo lessons.",
            ]
            
            self.Load("Pretending To Load The Game...", 10, f"Tip: {random.choice(Tips)}")

        elif MainMenuChoice == 1:
            self.Information()

        elif MainMenuChoice == 2:
            self.FuturePlans()

        else:
            print("Good choice! See you next time (or hopefully not)!".center(80))
            time.sleep(2)
            os.system('cls')
            os.abort()



    # << Playing Functions >> # 
    def GetAllSave(self):
        with open('Saves.json', mode='r') as infile:
            AllSaveData: list[dict] = json.load(infile)
        return AllSaveData
    
    def GetSave(self, SaveID):
        return self.GetAllSave()[SaveID]

    def DeleteSave(self, SaveID):
        os.system('cls')
        DeleteChoice = CoolBoxDialogue(['Are You Sure You Want To Delete This Save?', "You Won't Be Able To Recover This File Once Delete"], ['Y - Yes', 'N - No'], ['Y', 'N'], 88)
       
        if DeleteChoice == 0:
            Data = self.GetAllSave()
            Data.pop(SaveID)

            with open('Saves.json', mode='w') as outfile:
                json.dump(Data, outfile, indent=4)

        self.SaveMenu(self.GetAllSave())

    def GetSave(self, SaveID):
        return self.GetAllSave()[SaveID]

    def NewSave(self):
        os.system('cls')
        dialogues = ["Are You Sure You Want To Start A New Save?"]
        actions = ["Y - Yes", "N - No"]
        answers = ["Y", "N"]

        Choice = CoolBoxDialogue(dialogues, actions, answers, 80)

        if Choice == 0:
            os.system('cls')
            print("╔═════════════════════╗")
            print("║Please Select A Name.║")
            print(f"╚═════════════════════╝")

            Name = input("Name: ")
            print(f"You chose: {Name}, Are You Sure? (Name cannot be the same as any other save name.)")

            while Answer(["Y", "N"]) == 1 or Name in [i['Name'] for i in self.GetAllSave()]:
                os.system('cls')
                print("╔═════════════════════╗")
                print("║Please Select A Name.║")
                print(f"╚═════════════════════╝")

                Name = input("Name: ")
                print(f"You chose: {Name}, Are You Sure? (Name cannot be the same as any other save name.)")
            
            NewData = {
                "Name": Name,

                "Stats": {
                    "HP": 100,
                    "Strength": 0,
                    "Vitality": 0,
                    "Luck": 0,
                    "Gold": 0
                },

                "Misc": {

                },

                "Inventory": [

                ]
            }

            Data = self.GetAllSave()
            Data.append(NewData)

            with open('Saves.json', mode='w') as outfile:
                json.dump(Data, outfile, indent=4)

            return len(Data) - 1, NewData
        
        else:
            self.PlayGame()

    def SelectedSave(self, SaveID):
        os.system('cls')
        Data = self.GetSave(SaveID=SaveID)

        dialogues = [f"Selected Save: {Data['Name']}"]
        actions = ["U - Use Save", "D - Delete Save", "R - Return To Save Menu"]
        answers = ["U", "D", "R"]

        SelectedSaveOption = CoolBoxDialogue(dialogues, actions, answers, 80)

        if SelectedSaveOption == 0:
            self.Load("Loading Save", 5, "Please Leave The Game".center(80))
            return SaveID, Data
        
        elif SelectedSaveOption == 1:
            self.DeleteSave(SaveID)
        else:
            self.PlayGame()

    def SaveMenu(self, Data):
        os.system('cls')         
        current_selection = 0 

        while True:
            dialogues = ["Select Saves:"]
                
            dialogues += [f"Save {i}: {save['Name']}" + (' <--' if i == current_selection else '') for i, save in enumerate(Data)]

            actions = ["W/S - Move Up/Down Respectfully", "P - Select Save", "R - Return Saves Screen"]
            answers = ["W", "S", "P", "R"]

            SavesChoice = CoolBoxDialogue(dialogues, actions, answers, 80)
                
            if SavesChoice == 0:
                os.system('cls')
                current_selection = max(0, current_selection - 1)

            elif SavesChoice == 1:
                os.system('cls')
                current_selection = min(len(Data) - 1, current_selection + 1)

            elif SavesChoice == 2:
                return self.SelectedSave(current_selection)
                
            elif SavesChoice == 3:
                self.PlayGame()
                break        

    def PlayGame(self):
        print('yes')
        os.system('cls')
        Data = self.GetAllSave()

        dialogues = ["Current Detected Saves:"]
        dialogues += [f"Save {i}: {save['Name']}" for i, save in enumerate(Data)]

        actions = ["N - New Save", "S - Select Save", "R - Return To The Main Menu"]
        answers = ["N", "S", "R"]

        SavesMenuChoice = CoolBoxDialogue(dialogues, actions, answers, 80)

        if SavesMenuChoice == 0:
            return self.NewSave()
                    
        elif SavesMenuChoice == 1:
            self.SaveMenu(Data)

        else:
            self.MainMenu()
    
    # Tavern (The Starting Place Of The Game) #