import time, os, random, json
from itertools import cycle

# Outside Functions For Each Class To Use # 
def Dialogue(Author, Text, Time):
	print(f"{Author}: ", end="", flush=True)

	for char in Text:
		print(char, end="", flush=True)
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

def GenerateTip():
	Tips = [
		"Please Try To Exit The Game As Soon As Possible",
		"Don't chew Double Trouble Gum while running! Unless you've had years of didgeridoo lessons.",
		"The Red Square Quits The Game",
		"Rainbows Make Me Cry",
		"Drink It In Pal, That's How Failure Tastes",
	]

	return "Tip: " + random.choice(Tips)

def Inventory(SaveID):
    current_selection = 0
    current_page = 0

    with open('Saves.json', mode='r') as infile:
        Inventory = json.load(infile)[SaveID]['Inventory']

    while True:
        start_index = current_page * 10
        end_index = start_index + 10

        current_page_items = Inventory[start_index:end_index]

        dialogue_list = [f'Item {i}: {item["Name"]}' + (' <---' if i == current_selection else '') for i, item in enumerate(current_page_items)]
        
        Choicer = CoolBoxDialogue(dialogue_list, ['W - Move Up', 'S - Move down', 'A - Previous Page', 'D - Next Page'], ['W', 'S', 'A', 'D'], 88)

        if Choicer == 0:  
            current_selection = max(0, current_selection - 1) 

        elif Choicer == 1:
            current_selection = min(len(current_page_items) - 1, current_selection + 1) 

        elif Choicer == 2:
            current_page = max(0, current_page - 1)
            current_selection = 0

        elif Choicer == 3:
            # Next page
            current_page = min(len(Inventory) // 10, current_page + 1)
            current_selection = 0

Inventory(0)