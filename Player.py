import json, os, random

class Player:
    def __init__(self, SaveID, Stats) -> None:
        self.SaveID = SaveID
        self.Stats: list = Stats
        print(SaveID, Stats)
    
    def UpdateStats(self):
        with open('Saves.json', mode='r') as infile:
            AllData = json.load(infile)
        
        AllData[self.SaveID] = self.Stats

        with open('Saves.json', mode='w') as outfile:
            json.dump(AllData, outfile)
    
    def TakeDamage(self, Enemy):
        for item in self.Stats["Inventory"]:
            if item["Type"] == "Armor" and item.get("Wearing", None) == True:
                Damage *= ((Enemy.attack - item["Defense"]) / 100)
                item["Durability"] -= Damage.round()
                
                if item["Durability"] < 1:
                    self.Stats["inventory"].remove(item)
                    print("Your Armor Has Broke! You Will No Longer Get Reduced Damage Until Another Armor Is Equipped")

                if self.Stats["Stats"]["HP"] < 1:
                    print("You Have Died! Your Last Health Points Have Been Saved. Please quit the game forever and leave.")
                    os.abort()

                else:
                    self.UpdateStats()

    def attack(self):
        Found = False

        for item in self.Stats["Inventory"]:
            if item['Type'] == "Weapon" and item.get("Equipped", None) == True:
                Found = True
                return random.randint(0.9 * item['Attck'], 1.1 * item['Attack'])

            if not Found:
                return random.randint(9, 11)