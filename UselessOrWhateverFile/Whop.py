import os, json, random, time

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

def Dialogue(Author, Text, Time):
	print(f"{Author}: ", end="", flush=True)

	for char in Text:
		print(char, end="", flush=True)
		time.sleep(Time)

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
	
	def DungeonMove(self, Map: list[list[str]], Goals: dict[list[list]], PlayerPosition: list, CurrentTrial):
		os.system('cls')
		Map[PlayerPosition[0]][PlayerPosition[1]] == '[P]'

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
				if CurrentTrial != "Trial1":
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
	
	def DungeonMap(self, DungeonData, CurrentTrial):
	
		with open('Maps.json', mode='r', encoding='utf8') as infile:
			AllDungeonsMaps = json.load(infile)

		for map in AllDungeonsMaps:
			if map['name'] == DungeonData['Dungeon']:
				AllMapData = map
				Map = map['map']

		Map[AllMapData['Trial1'][0]][AllMapData['Trial1'][1]] = "[1]"
		Map[AllMapData['Trial2'][0]][AllMapData['Trial2'][1]] = "[2]"
		Map[AllMapData['Trial3'][0]][AllMapData['Trial3'][1]] = "[3]"

		for i in Map:
			print(''.join(i))		

		Choice = self.DungeonMove(Map, {
			"Trial1": [AllMapData['Trial1']],
			"Trial2": [AllMapData['Trial2']],
			"Trial3": [AllMapData['Trial3']]
		}, [AllMapData['StartY'], AllMapData['StartX']], CurrentTrial)

		return Choice
	
def Guard(self):
	os.system('cls')
	current_selection = 0
	PlayerLevel = 1
	with open('DData.json', mode='r') as infile:
		Dungeons: list[dict] = json.load(infile)
	while True:
		os.system('cls')
		dialogues = ["Select Dungeon:"]
		for i, dungeon in enumerate(Dungeons):
			if PlayerLevel >= dungeon['LevelReq']:
				dialogue = f"Dungeon {i}: {dungeon['Dungeon']}"
			else:
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
			return Dungeoner(Dungeons[current_selection], self.PlayerClass).StartDungeon()
		else:
			print("Exiting!!")
			time.sleep(5)
			return "GET OUT OF MY SKIN"

class Dungeoner:
	def __init__(self, dungeon, PlayerClass) -> None:
		self.dungeonData = dungeon
		self.Player = PlayerClass
		self.Enemies = []
		self.PlayerTurns = random.choice([False, True])

	def StartDungeon(self):
		CurrentTrial = "Trial1"

		TrialChoice = Maps().DungeonMap(self.dungeonData, CurrentTrial=CurrentTrial)
		
		if TrialChoice == 'Exit':
			return
		
		else:
			self.Trials(TrialChoice)
	
	def RandomEnemies(self, Trial):
		Enemies = self.dungeonData["Enemies"].copy()
		EnemyList = []
		Tempt = []

		if Trial == "Trial1":
			Multiplier = 0.5

		elif Trial == "Trial2":
			Multiplier = 1

		elif Trial == "Trial3":
			Multiplier = 1.25

		while len(EnemyList) < 1:
			for Enemy in Enemies:
				Chance = Enemy['Chance']

				Enemy['Hp'] = int(Enemy['Hp'] * Multiplier)
				Enemy['Attack'] = int(Enemy['Attack'] * Multiplier)
				Enemy['Exp'] = int(Enemy['Exp'] * Multiplier)
				Enemy['MovementChance'] = int(Enemy['MovementChance'] * Multiplier)

				Tempt.extend(Enemy for i in range(Chance))
				Tempt.extend(0 for i in range(100 - len(Tempt)))

				Choice = random.choice(Tempt)

				while Choice != 0:
					EnemyList.append(Choice)

					Tempt = []

					Chance = int(Chance/2)
					Tempt.extend(Enemy for i in range(Chance))
					Tempt.extend(0 for i in range(100 - len(Tempt)))

					Choice = random.choice(Tempt)

		self.Enemies = EnemyList
		
		return EnemyList

	def Trials(self, Trial):
		self.Enemies = self.RandomEnemies(Trial)
		print(self.Enemies)
		time.sleep(20)
		
		while len(self.Enemies) > 0 or self.PlayerClass.Stats['HP'] > 0: 
			if self.PlayerTurns:
				self.PlayerTurn()
				self.PlayerTurns = False

			if not self.PlayerTurns:
				self.EnemyTurn()
				self.PlayerTurn = True

	def PlayerTurn(self):
		current_selection = 0
		selected_enemies = []

		while True:
			os.system('cls')
			enemydesc = [f'Enemy {i}: {enemy["Name"]}' + (' (selected)' if i in selected_enemies else '') + (' <---' if i == current_selection else '') for i, enemy in enumerate(self.Enemies)]
			
			Choicer = CoolBoxDialogue(
				enemydesc, 
				['W - Move Up', 'S - Move down', 'P - Select/Deselect Enemy', 'I - Inspect Selected Enemies'],
				['W', 'S', 'P', 'I'],
				88
			)

			if Choicer == 0:  
				current_selection = max(0, current_selection - 1) 

			elif Choicer == 1:
				current_selection = min(len(self.Enemies) - 1, current_selection + 1) 

			elif Choicer == 2:
				if current_selection in selected_enemies: 
					selected_enemies.remove(current_selection) 
				else: 
					selected_enemies.append(current_selection)  

			elif Choicer == 3:
				pass

			else: 
				break  

	def EnemyTurn(self):
		for Enemy in self.Enemies:
			pass

with open('DData.json', mode='r', encoding='utf8') as infile:
	dungeon = json.load(infile)

E = Dungeoner(dungeon[0], 0)
E.RandomEnemies("Trial1")
E.PlayerTurn()
