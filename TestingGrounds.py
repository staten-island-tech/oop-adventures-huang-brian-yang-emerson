import os, time

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

List = [
    {
        'Name': "yes"
    },
    {
        "Name": "yes"
    }
]


current = 1

yes = [f"Save {i}: {save['Name']}" + (' <--' if i == current else '') for i, save in enumerate(List)]


dict = {'self': 'yes', 'no': 'l', 'sss': 'ssss'}


Map  = [["#" for i in range(5)] for i in range(5)]

Map[2][2] = "P"


import time

def slow_print(author, text, delay):
    print(f"{author}: ", end='', flush=True)
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def Dialogue(Author, Text, Time):
	print(f"{Author}: ", end="", flush=True)
	for char in Text:
		print(char, end="", flush=True)
		time.sleep(Time)

Dialogue("Sans", "Do you want to have a bad time?\n", 0.1)
Dialogue("Sans", "Because if you take one more step forward...you are REALLY not going to like what happens next.", 0.05)