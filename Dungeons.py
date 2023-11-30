import json

class Dungeon:
    def __init__(self, dungeon, difficulty) -> None:
        self.dungeon = dungeon
        self.difficulty = difficulty
    
    def StartDungeon(self, playerClass):

        with open('DData.json', mode='r') as infile:
            DungeonData: list[dict] = json.load(infile)
        
        for Dungeons in DungeonData:
            for DungeonName in Dungeons:
                if DungeonName == self.dungeon:
                    print("start")
        