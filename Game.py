import time, os, random, json
from itertools import cycle

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

class PreGame:
	def __init__(self):
		self.loading_done = False
		self.SaveID = 0
		self.SaveData = {}

	# << Main Menu Functions >> #
	def Information(self):
		print("Information: Clean Up On Isle 9 Please".center(80))
		print("Press enter to return to the main menu.".center(80))
		input()
		return self.MainMenu()

	def FuturePlans(self):
		print("Future Plans As Of Currently:".center(80))
		print("1. Finish The Game".center(80))
		print("Press enter to return to the main menu.".center(80))
		input()
		return self.MainMenu()

	def Load(self, Message, LTS):
			LoadingSprites = ['|', '/', '-', '\\', '|', '/', '-', '\\']
			LT = 0
			LTT = 0

			Tip = GenerateTip()

			for i in cycle(LoadingSprites):
				if LTT == 5:
					Tip = GenerateTip()
					LTT = 0

				if LT != LTS:
					os.system('cls')
					print(f"{i} {Message} {i}\n {Tip}", end="")
					time.sleep(0.5)
					LT += 1
					LTT += 1
					
				elif LT == LTS:
					os.system('cls')
					self.loading_done = True
					break

	def MainMenu(self):
		if not self.loading_done:
			self.Load("Loading Game...", 25)

		os.system("cls")

		dialogues = [
			"Welcome To --> Genric text dengen gme",
			"Possibly The Worst Game You'll Ever Play",
			"Please Feel Free To Exit The Game Anytime And Anywhere",
			"Options For The Main Menu:"
		]

		actions = [
			"E - Exit The Game <--- (Psst. This One)",
			"P - Play",
			"I - Info",
			"F - Future Plans",
		]

		answers = ["E", "P", "I", "F",]

		MainMenuChoice = CoolBoxDialogue(dialogues, actions, answers, 80)

		if MainMenuChoice == 0:
			print("Good choice! See you next time (or hopefully not)!".center(80))
			time.sleep(2)
			os.system('cls')
			os.abort()

		elif MainMenuChoice == 1:

			self.Load("Pretending To Load The Game...", 10)
			return self.PlayGame()

		elif MainMenuChoice == 2:
			return self.Information()

		else:
			return self.FuturePlans()

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

		return self.SaveMenu(self.GetAllSave())

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
					"Gold": 0,
					"HP": 100,
					"Strength": 0,
					"Luck": 0,
					"Level": 1,
					"Vitality": 0
				},

				"Misc": {
					'TutorialDone': False
				},

				"Inventory": [

				],

				"Armor": {
					"Name": "None",
					"Durability": 0
				},

				"Weapon": {
					"Name": "None"
				}
			}

			Data = self.GetAllSave()
			Data.append(NewData)

			with open('Saves.json', mode='w') as outfile:
				json.dump(Data, outfile, indent=4)

			self.Load("Loading Save...", 10)

			self.SaveData = NewData
			self.SaveID = len(Data) - 1

			return len(Data) - 1, NewData

		else:
			return self.PlayGame()

	def RenameSave(self, SaveID):
		os.system('cls')
		Data = self.GetAllSave()

		RenameChoice = CoolBoxDialogue(['Are You Sure You Want To Rename This Save?'], ['Y - Yes', 'N - No'], ['Y', 'N'], 88)

		if RenameChoice == 0:
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

			Data[SaveID]['Name'] = Name

			with open('Saves.json', mode='w') as outfile:
				json.dump(Data, outfile, indent=4)

			self.Load("Registered New Save File. Starting Game...", 10)

		return self.SaveMenu(self.GetAllSave())

	def SelectedSave(self, SaveID):
		os.system('cls')
		Data = self.GetSave(SaveID)
		dialogues = [f"Selected Save: {Data['Name']}"]
		actions = ["U - Use Save", "N - Rename Save", "D - Delete Save", "R - Return To Save Menu"]
		answers = ["U", "D", "N", "R"]

		SelectedSaveOption = CoolBoxDialogue(dialogues, actions, answers, 80)

		if SelectedSaveOption == 0:
			self.Load("Loading Save", 5)

			self.SaveData = Data
			self.SaveID = SaveID

			return SaveID, Data

		elif SelectedSaveOption == 1:
			return self.DeleteSave(SaveID)

		elif SelectedSaveOption == 2:
			return self.RenameSave(SaveID)

		else:
			return self.PlayGame()

	# First Function To Be Called #
	def PlayGame(self):
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

			if len(Data) > 0:
				return self.SaveMenu(Data)
			
			else:
				return self.PlayGame()

		else:
			return self.MainMenu()

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
				return self.PlayGame()
			
	def GetVariable(self):
		return self.SaveID, self.SaveData
			
class PostMenu(PreGame):
	def __init__(self):
		super().__init__()

	def ClampCoords(self, PlayerCoord: list, GameMapCoorder: list):
		if PlayerCoord[0] > GameMapCoorder[0]:
			PlayerCoord[0] = GameMapCoorder[0]
		if PlayerCoord[0] < 0:
			PlayerCoord[0] = 0

		if PlayerCoord[1] > GameMapCoorder[1]:
			PlayerCoord[1] = GameMapCoorder[1]
		if PlayerCoord[1] < 0:
			PlayerCoord[1] = 0

		return PlayerCoord

	def Tutorial(self):
		Dialogue("Villager", "Ah Hello! You Don't Seem To Be Around Here. Well In That Case I'll formally welcome you into our town, Windmill Town\n", 0.05)
		Dialogue("Villager", "Would you like a tutorial on the game?\n", 0.05)
		TutorialChoice = Answer(['Y', 'N'])

		if TutorialChoice == 0:
			os.system('cls')
			Dialogue("Villager", "Alright. Here Are The Basics. 1. Quitting The Game. It is always important to know how to quit the game!\n", 0.05)
			Dialogue("Villager", "To Quit The Game You SHOULD Always Click The Red Square Thingy. Try Doing It Now.\n", 0.05)
			time.sleep(5)
			Dialogue("Villager", "No? Alright Next, We've Got A Map. For Tutorial purposes, this will be much simplier\n", 0.05)

			Map = [["[ ]" for i in range(5)] for i in range(5)]
			Map[2][2] = "[P]"
			playerCoords = [2, 2]

			for i in Map:
				print(''.join(i))

			Dialogue("Villager", "Here Is The Basic Map ^^, P Represents YOU On The Map. You'll Be Able To Move Around Once I'm Done\n", 0.05)
			Dialogue("Villager", "To Move Around, You Can Use W - A - S - D. There'll Be A Goal On The Map (G). Try Getting There.", 0.05)
			time.sleep(3)
			os.system('cls')
			GoalCoords = (random.choice([0, 1, 3, 4,]), random.choice([0, 1, 3, 4,]))
			Map[GoalCoords[0]][GoalCoords[1]] = "[G]"

			while tuple(playerCoords) != GoalCoords:
				os.system('cls')
				Movement = CoolBoxDialogue((f"{''.join(i)}" for i in Map), ["W - Move Up", "A - Left", "S - Down", "D - Right"], ['W', 'A', 'S', 'D'], 50)
	
				MapCoorder = [4, 4]
	
				Previous = playerCoords[:]
	
				if Movement == 0:
					playerCoords[0] -= 1
					playerCoords = self.ClampCoords(playerCoords, MapCoorder)
	
				elif Movement == 1:
					playerCoords[1] -= 1
					playerCoords = self.ClampCoords(playerCoords, MapCoorder)
	
				elif Movement == 2:
					playerCoords[0] += 1
					playerCoords = self.ClampCoords(playerCoords, MapCoorder)	
	
				elif Movement == 3:
					playerCoords[1] += 1
					playerCoords = self.ClampCoords(playerCoords, MapCoorder)
	
				Map[Previous[0]][Previous[1]] = '[ ]'
				Map[playerCoords[0]][playerCoords[1]] = "[P]"
		
		os.system('cls')
		if TutorialChoice == 0:
			Dialogue('Villager', "Oh, Nice You Actually Did It. I Was Not Expecting That.\n", 0.05)
		else:
			Dialogue('Villager', "Oh? Really? Well in that case...\n", 0.1)
		Dialogue('Villager',"Now You're On Your Own. I'm Too Lazy To Explain The Rest Of The Game\n", 0.05)
		Dialogue('Villager', 'Remember, To QUIT the game, please click the red square thingy.\n', 0.05)
		Dialogue("Villager", "Goodbye.", 0.5) 

	def TavernStart(self):
		self.SaveID, self.SaveData = super().GetVariable()
		
		os.system("cls")

		print(self.SaveID, self.SaveData)
		if self.SaveData['Misc']['TutorialDone'] == False:
			self.Tutorial()

		os.system('cls')
		Map = [["[ ]" for i in range(10)] for i in range(10)]
		Goals = [(1, 3), (7, 7)]
		PlayerStart = [5, 5]
		Map[5][5] = "[P]"
		Map[1][3] = "[B]"
		Map[7][7] = "[T]"
		
		while tuple(PlayerStart) not in Goals:
			os.system('cls')
			Movement = CoolBoxDialogue((f"{''.join(i)}" for i in Map), ["W - Move Up", "A - Left", "S - Down", "D - Right"], ['W', 'A', 'S', 'D'], 50)

			MapCoorder = [9, 9]

			Previous = PlayerStart[:]

			if Movement == 0:
				PlayerStart[0] -= 1
				PlayerStart = self.ClampCoords(PlayerStart, MapCoorder)

			elif Movement == 1:
				PlayerStart[1] -= 1
				PlayerStart = self.ClampCoords(PlayerStart, MapCoorder)

			elif Movement == 2:
				PlayerStart[0] += 1
				PlayerStart = self.ClampCoords(PlayerStart, MapCoorder)	

			elif Movement == 3:
				PlayerStart[1] += 1
				PlayerStart = self.ClampCoords(PlayerStart, MapCoorder)

			Map[Previous[0]][Previous[1]] = '[ ]'
			Map[PlayerStart[0]][PlayerStart[1]] = "[P]"

class Dungeon:
	def __init__(self, dungeon, PlayerClass) -> None:
		self.dungeon = dungeon
		self.Player = PlayerClass
		self.Enemies = {"tester": {"CurrentEffects": {"Burn": {}}}}

		self.PlayerTurn = random.choice([False, True])

	def StartDungeon(self):

		with open("DData.json", mode='r') as infile:
			AllDungeonData = json.load(infile)

		self.dungeon = AllDungeonData[self.dungeon]