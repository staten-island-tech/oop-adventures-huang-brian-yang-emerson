import time, os, random, json
from itertools import cycle

def Dialogue(Author, Text, Time):
    for char in Text:
        print(f"{Author}: " + char)
        time.sleep(time)

def Answer(Options: list):
    Confirmaton = input(f"{'/'.join(Options)}: ").upper()

    while Confirmaton not in Options:
        Confirmaton = input(f"{'/'.join(Options)}: ").upper()
    
    return Options.index(Confirmaton)

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
    
    # << Playing Functions >> # 
    def GetAllSave(self):
        with open('Saves.json', mode='r') as infile:
            AllSaveData: list[dict] = json.load(infile)
        return AllSaveData
    
    def GetSave(self, SaveID):
        return self.GetAllSaves()[SaveID]

    def MainMenu(self):
        if not self.loading_done:
            self.Load("Loading Game...", 25, "Please Feel Free To Close The Program During This Process.")
        
        os.system("cls")

        print("""
        ╔══════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                      ║
        ║     Welcome To --> Genric text dengen gme                                            ║
        ║     Possibly The Worst Game You'll Ever Play                                         ║
        ║     Please Feel Free To Exit The Game Anytime And Anywhere                           ║
        ║                                                                                      ║
        ║     Options For The Main Menu:                                                       ║
        ║     P - Play                                                                         ║
        ║     I - Info                                                                         ║
        ║     F - Future Plans                                                                 ║
        ║     E - Exit The Game <--- (Psst. This One)                                          ║
        ║                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════╝
        """.center(80), end="")

        MainMenuChoice = Answer(["P", "I", "F", "E"])

        if MainMenuChoice == 0:
            Tips = [
                "Please Try To Exit The Game As Soon As Possible",
                "Don't chew Double Trouble Gum while running! Unless you've had years of didgeridoo lessons.",
                ]
            
            self.Load("Pretending To Load The Game...", 10, f"Tip: {random.choice(Tips)}")
            self.PlayGame()

        elif MainMenuChoice == 1:
            self.Information()

        elif MainMenuChoice == 2:
            self.FuturePlans()

        else:
            print("Good choice! See you next time (or hopefully not)!".center(80))
            time.sleep(2)
            os.system('cls')
    
    def PlayGame(self):
        Data = self.GetAllSave()

        print("""
        ╔══════════════════════════════════════════════════════════════════════════════════════╗
        ║ Current Detected Saves:                                                              ║
        ║                                                                                      ║
        ║ Available Actions:                                                                   ║
        ║ N - New Save                                                                         ║
        ║ S - Select Save                                                                      ║
        ║ R - Return To The Main Menu                                                          ║
        ║                                                                                      ║
        ╚══════════════════════════════════════════════════════════════════════════════════════╝
        """.center(80), end="")

        SavesMenuChoice = Answer(['N', 'S', 'R'])

        if SavesMenuChoice == 0:
            pass
        elif SavesMenuChoice == 1:
            pass
        else:
            self.MainMenu()
