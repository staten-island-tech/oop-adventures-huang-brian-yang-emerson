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

def TerminalFlood(columns, rows):
    for i in range(columns):
        for i in range(rows):
            pass

class Game:
    def __init__(self) -> None:
        pass

    def MainMenu(self):

        LoadingSprites = ['|', '/', '-', '\\', '|', '/', '-', '\\']
        
        LT = 0

        for i in cycle(LoadingSprites):
            if LT != 25:
                print(f"{i} Loading Game... {i}\n Please Feel Free To Close The Program During This Process.", end="")
                time.sleep(0.5)
                os.system('cls')
                LT += 1
            elif LT == 25:
                break

        print("""Welcome To Possibly The Worst Game You'll Ever Play
Please Feel Free To Exit The Game Anytime And Anywhere 
Options For The Main Menu:
P - Play
I - Info
F - Future Plans
E - Exit The Game <--
^ ^ ^ ^ ^ ^ ^ ^ ^ 
""", end=""
            )
        MainMenuChoice = Answer(["P", "I", "F", "E"])

        if MainMenuChoice == 0:
            pass
        elif MainMenuChoice == 1:
            pass
        elif MainMenuChoice == 2:
            pass
        else:
            pass