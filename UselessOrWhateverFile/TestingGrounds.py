import os, time, json

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


import math

def distance(point1, point2):
    distance1 = (point2[0] - point1[0]) ** 2
    distance2 = (point2[1] - point1[1]) ** 2

    return math.sqrt(distance1 + distance2)

import json

def slope(coord1, coord2):
    Rise = coord2[1] - coord1[1]
    Run = coord2[0] - coord1[0]

    print(f'{Rise}/{Run}')

def InaccurateLength(coord1, coord2):
    Var1 = (coord2[0] - coord1[0]) ** 2
    Var2 = (coord2[1] - coord1[1]) ** 2
    Var3 = Var1 + Var2
    print(f'sqr({Var3})')

slope((6, 8), (-3, 7))