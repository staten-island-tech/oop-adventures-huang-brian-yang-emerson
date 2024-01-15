import os, json, time

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


def Guard():
	os.system('cls')
	current_selection = 0
	PlayerLevel = 1  # This will be replaced with the actual player level
	
	with open('DData.json', mode='r') as infile:
		Dungeons: list[dict] = json.load(infile)
		
	while True:
		os.system('cls')
		dialogues = ["Select Dungeon:"]
		for i, dungeon in enumerate(Dungeons):
			if PlayerLevel >= dungeon['LevelReq']:
				dialogue = f"Dungeon {i}: {dungeon['Dungeon']}"
			else:
				print("Not Enough Level")
				dialogue = f"Dungeon {i}: {dungeon['Dungeon']} (Locked!)"
			if i == current_selection and PlayerLevel >= dungeon['LevelReq']:
				dialogue += ' <--'
			dialogues.append(dialogue)
		actions = ["W/S - Move Up/Down Respectively", "P - Select Dungeon", "R - Return"]
		answers = ["W", "S", "P", "R"]
		DungeonChoice = CoolBoxDialogue(dialogues, actions, answers, 80)
		if DungeonChoice == 0 and current_selection > 0:
			if PlayerLevel >= Dungeons[current_selection - 1]['LevelReq']:
				current_selection -= 1
		elif DungeonChoice == 1 and current_selection < len(Dungeons) - 1:
			if PlayerLevel >= Dungeons[current_selection + 1]['LevelReq']:
				current_selection += 1
		
		elif DungeonChoice == 2:
			pass
		else:
			print("Exiting!!")
			time.sleep(5)
			return "GET OUT OF MY SKIN"

Guard()