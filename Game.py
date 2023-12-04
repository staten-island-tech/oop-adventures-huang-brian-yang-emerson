import time

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
    def __init__(self) -> None:
        pass

    def MainMenu(self):


        print("""Welcome To Possibly The Worst Game You'll Ever Play
Please Feel Free To Exit The Game Anytime And Anywhere 
Options For The Main Menu:
P - Play
I - Info
F - Future Plans
E - Exit The Game <--
^ ^ ^ ^ ^ ^ ^ ^ ^ 
              """
            )
        MainMenuChoice = Answer(["P", "I", "F", "E"])

        if MainMenuChoice == 0:
            pass
        elif MainMenuChoice == 1:
            pass
        else:
            pass