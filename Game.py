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

class PreGame:
	def __init__(self):
		self.loading_done = False
		self.SaveID = 0
		self.SaveData = {}

	# << Main Menu Functions >> #
	def Information(self):
		print("There's a very specific bug that I CANNOT SEE BRUH".center(80))
		print("Game By Some 2 People I Forgor".center(80))
		print("Press enter to return to the main menu.".center(80))
		input()
		return self.MainMenu()

	def FuturePlans(self):
		print("Future Plans As Of Currently:".center(80))
		print("1. Migrate Maps To Json Files For Easier Usage".center(80))
		print("2. Better Maps And Map Handling".center(80))
		print("3. Finish Construction Of The Lobby And Uh Whatever Matters.".center(80))
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

	def DeleteSave(self, SaveID):
		os.system('cls')
		DeleteChoice = CoolBoxDialogue(['Are You Sure You Want To Delete This Save?', "You Won't Be Able To Recover This File Once Delete"], ['Y - Yes', 'N - No'], ['Y', 'N'], 88)

		if DeleteChoice == 0:
			Data = self.GetAllSave()
			Data.pop(SaveID)

			with open('Saves.json', mode='w') as outfile:
				json.dump(Data, outfile, indent=4)

		return self.PlayGame()

	def GetSave(self, SaveID):
		try:
			return self.GetAllSave()[SaveID]
		except:
			return self.PlayGame()

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
					"Vitality": 0,
					"Exp": 0
				},

				"Misc": {
					'TutorialDone': False
				},
        		"Armor": {
        		    "Name": "None",
        		    "Durability": 0
        		},
        		"Weapon": {
        		    "Name": "None"
        		},
				"Inventory": [

				],
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

		return self.PlayGame()

	def SelectedSave(self, SaveID):
		os.system('cls')
		Data = self.GetSave(SaveID)
		dialogues = [f"Selected Save: {Data['Name']}"]
		actions = ["U - Use Save", "N - Rename Save", "D - Delete Save", "R - Return To Save Menu"]
		answers = ["U", "N", "D", "R"]

		SelectedSaveOption = CoolBoxDialogue(dialogues, actions, answers, 80)

		if SelectedSaveOption == 0:
			self.Load("Loading Save", 5)

			self.SaveData = Data
			self.SaveID = SaveID

			return SaveID, Data

		elif SelectedSaveOption == 1:
			return self.RenameSave(SaveID)

		elif SelectedSaveOption == 2:
			return self.DeleteSave(SaveID)

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

				if len(Data) > 0:
					current_selection = min(len(Data) - 1, current_selection + 1)
				else:
					return self.SaveData(self.GetAllSave())

			elif SavesChoice == 2:
				if len(Data) > 0:
					return self.SelectedSave(current_selection)
				else:
					os.system('cls')

			elif SavesChoice == 3:
				return self.PlayGame()
			
	def GetVariable(self):
		return self.SaveID, self.SaveData

class Maps:
	def __init__(self) -> None:
		with open('Maps.json', mode='r', encoding='utf8') as infile:
			self.AllMapData: list[dict] = json.load(infile)

	def MapMove(self, Map: list[list[str]], Goals: dict[list[list]], PlayerPosition: list):
		os.system('cls')
		Map[PlayerPosition[0]][PlayerPosition[1]] == '[P]'

		while True:
			os.system('cls')
			PreviousPosition = PlayerPosition.copy()
			TargetPosition = PlayerPosition.copy()

			for i in Map:
				print(''.join(i))
			
			Movement = CoolBoxDialogue(["Where To Now?"], ['W - Up', 'A - Left', 'S - Down', 'D - Right'], ['W', 'A', 'S', 'D'], 88)

			if Movement == 0:
				TargetPosition[0] -= 1
			elif Movement == 1:
				TargetPosition[1] -= 1
			elif Movement == 2:
				TargetPosition[0] += 1
			elif Movement == 3:
				TargetPosition[1] += 1

			TargetPosition[0] = max(0, TargetPosition[0])
			TargetPosition[1] = max(0, TargetPosition[1])
			
			try:
				if Map[TargetPosition[0]][TargetPosition[1]] == "[ ]":
					PlayerPosition = TargetPosition.copy()	
				else:
					PlayerPosition = PreviousPosition

			except:
				PlayerPosition = PreviousPosition

			Map[PreviousPosition[0]][PreviousPosition[1]] = "[ ]"
			Map[PlayerPosition[0]][PlayerPosition[1]] = "[P]"
			
			os.system('cls')

			for key, value in Goals.items():
				for val in value:
					if TargetPosition == val:
						return key
				
	def TutorialMap(self):
		Map = [["[ ]" for i in range(5)] for i in range(5)]
		Map[2][2] = "[P]"
		Goal = [random.randint(0, 4), random.randint(0, 4)]
		Map[Goal[0]][Goal[1]] = '[G]'

		for i in Map:
			print(''.join(i))

		Dialogue("Villager", "Here Is The Basic Map ^^, P Represents YOU On The Map. You'll Be Able To Move Around Once I'm Done\n", 0.05)
		Dialogue("Villager", "To Move Around, You Can Use W - A - S - D. There'll Be A Goal On The Map (G). Try Getting There.", 0.05)
		time.sleep(3)
		os.system('cls')		

		return self.MapMove(Map, {'G': [[Goal[0], Goal[1]]]}, [2, 2])
	
	def DungeonMove(self, Map: list[list[str]], Goals: dict[list[list]], PlayerPosition: list):
		os.system('cls')
		Map[PlayerPosition[0]][PlayerPosition[1]] == '[P]'
		CanLeave = False

		while True:
			os.system('cls')
			PreviousPosition = PlayerPosition.copy()
			TargetPosition = PlayerPosition.copy()

			for i in Map:
				print(''.join(i))
			
			Movement = CoolBoxDialogue(["Where To Now?"], ['W - Up', 'A - Left', 'S - Down', 'D - Right', 'I - Inventory', 'E - Exit'], ['W', 'A', 'S', 'D', 'I', 'E'], 88)

			if Movement == 0:
				TargetPosition[0] -= 1
			elif Movement == 1:
				TargetPosition[1] -= 1
			elif Movement == 2:
				TargetPosition[0] += 1
			elif Movement == 3:
				TargetPosition[1] += 1
			elif Movement == 4:
				pass
			elif Movement == 5:
				if CanLeave:
					return "Exit"


			TargetPosition[0] = max(0, TargetPosition[0])
			TargetPosition[1] = max(0, TargetPosition[1])
			
			try:
				if Map[TargetPosition[0]][TargetPosition[1]] == "[ ]":
					PlayerPosition = TargetPosition.copy()	
				else:
					PlayerPosition = PreviousPosition

			except:
				PlayerPosition = PreviousPosition

			Map[PreviousPosition[0]][PreviousPosition[1]] = "[ ]"
			Map[PlayerPosition[0]][PlayerPosition[1]] = "[P]"
			
			os.system('cls')

			for key, value in Goals.items():
				for val in value:
					if TargetPosition == val:
						return key
					
	def LobbyMap(self):
		for MapData in self.AllMapData:
			if MapData['name'] == 'Lobby':
				LobbyData = MapData

		LobbyMap = LobbyData['map']
		LobbyMap[LobbyData['StartY']][LobbyData['StartX']] = '[P]'

		# For Guard #
		LobbyMap[12][14] = "[G]"
		LobbyMap[12][15] = "[G]"
		LobbyMap[12][16] = "[G]"

		return self.MapMove(
			LobbyMap, 
			{
				"G": [[12, 14], [12, 15], [12, 16]],
				}, 
			[LobbyData['StartY'], LobbyData['StartX']]
			)
	
	def DungeonMap(self, DungeonData):

		with open('Maps.json', mode='r') as infile:
			AllDungeonsMaps = json.load(infile)

		for map in AllDungeonsMaps:
			if map['name'] == DungeonData['Dungeon']:
				AllMapData = map
				Map = map['map']

		Map[AllMapData['Trial1'][0]][AllMapData['Trial1'][1]] = "1"
		Map[AllMapData['Trial2'][0]][AllMapData['Trial2'][1]] = "1"
		Map[AllMapData['Trial3'][0]][AllMapData['Trial3'][1]] = "1"

		for i in Map:
			print(''.join(Map))		

		Choice = self.DungeonMove(Map, {
			"Trial1": AllMapData['Trial1'],
			"Trial2": AllMapData['Trial2'],
			"Trial3": AllMapData['Trial3']
		}, [AllMapData['StartY'], AllMapData['StartX']])

		return Choice

class PostMenu:
	def __init__(self, SaveID, SaveData):
		self.SaveID = SaveID
		self.SaveData = SaveData

		
	def Tutorial(self):
		Dialogue("Villager", "Ah Hello! You Don't Seem To Be Around Here. Well In That Case I'll formally welcome you into our town, Windmill Town\n", 0.05)
		Dialogue("Villager", "Would you like a tutorial on the game?\n", 0.05)
		TutorialChoice = Answer(['Y', 'N'])

		if TutorialChoice != 0:
			Dialogue("Villager", "Oh well in that case I guess you're own your own.\n", 0.1)
			time.sleep(3)
			self.SaveData['Misc']['TutorialDone'] = True
			return

		os.system('cls')
		Dialogue("Villager", "Alright. Here Are The Basics. 1. Quitting The Game. It is always important to know how to quit the game!\n", 0.05)
		Dialogue("Villager", "To Quit The Game You SHOULD Always Click The Red Square Thingy. Try Doing It Now.\n", 0.05)
		time.sleep(5)
		Dialogue("Villager", "No? Alright Next, We've Got A Map. For Tutorial purposes, this will be much simplier\n", 0.05)

		Maps().TutorialMap()

		os.system('cls')
		Dialogue('Villager', "Oh, Nice You Actually Did It. I Was Not Expecting That.\n", 0.05)
		Dialogue('Villager', "I mean it's technically my job to explain the rest of the game but...\n", 0.05)
		Dialogue('Villager', "I'm kinda too lazy to explain the rest of the game so yeah.\n", 0.05)
		Dialogue('Villager', 'Remember, To QUIT the game, please click the red square thingy.\n', 0.05)
		Dialogue('Villager', "Try To Quit The Game As Soon As Possible. Please Don't Stay Any Longer.\n", 0.05)
		Dialogue("Villager", "Goodbye.", 0.5) 

	def SystemServices(self):
		pass

	def Guard(self):
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
					print("Enough Level", dungeon['Dungeon'])
					dialogue = f"Dungeon {i}: {dungeon['Dungeon']}"
				else:
					print("Not Enough Level", dungeon['Dungeon'])
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
				return Dungeoner(Dungeons[current_selection])

			else:
				print("Exiting!!")
				time.sleep(5)
				return "GET OUT OF MY SKIN"

	def TavernStart(self):
		
		os.system("cls")

		if self.SaveData['Misc']['TutorialDone'] == False:
			self.Tutorial()

		os.system('cls')

		while True:
			Decision = Maps().LobbyMap()

			if Decision == "G":
				Decision = None
				print(self.Guard())

class Dungeoner:
	def __init__(self, dungeon, PlayerClass, Difficulty) -> None:
		self.dungeonData = dungeon
		self.Player = PlayerClass
		self.Difficulty = Difficulty
		self.Enemies = {"tester": {"CurrentEffects": {"Burn": {}}}}
		self.PlayerTurn = random.choice([False, True])

	def StartDungeon(self):
		TrialChoice = Maps().DungeonMap(self.dungeonData)
		
		if TrialChoice == 'Exit':
			return

	def Trial1(self):
		pass

	def Trial2(self):
		pass

	def Trial3(self):
		pass

	def PlayerTurn(self):
		pass

	def EnemyTurn(self):
		pass
