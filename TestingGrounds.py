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

print(enumerate(List))

current = 1

yes = [f"Save {i}: {save['Name']}" + (' <--' if i == current else '') for i, save in enumerate(List)]

print(yes)