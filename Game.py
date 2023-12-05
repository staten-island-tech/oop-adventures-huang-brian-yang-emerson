import time, os
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

    def Information(self):
        print("Information: Clean Up On Isle 9 Please".center(80))
        print("Press any key to return to the main menu.".center(80))
        input()
        self.MainMenu() 
    
    def FuturePlans(self):
        print("Future Plans As Of Currently:".center(80))
        print("1. Finish The Game".center(80))
        print("Press any key to return to the main menu.".center(80))
        input()
        self.MainMenu()

    def MainMenu(self):
        if not self.loading_done:
            LoadingSprites = ['|', '/', '-', '\\', '|', '/', '-', '\\']
            LT = 0
            for i in cycle(LoadingSprites):
                if LT != 25:
                    print(f"{i} Loading Game... {i}\n Please Feel Free To Close The Program During This Process.".center(80), end="")
                    time.sleep(0.5)
                    os.system('cls')
                    LT += 1
                elif LT == 25:
                    self.loading_done = True
                    break
        
        os.system("cls")

        print("""
        ╔══════════════════════════════════════════════════════════════════════════════════════╗
        ║                                                                                      ║
        ║     Welcome To Possibly The Worst Game You'll Ever Play                              ║
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
            pass

        elif MainMenuChoice == 1:
            self.Information()

        elif MainMenuChoice == 2:
            self.FuturePlans()

        else:
            print("Good choice! See you next time (or hopefully not)!".center(80))
            time.sleep(2)
            os.system('cls')
    
    def PlayGame(self):
        pass
