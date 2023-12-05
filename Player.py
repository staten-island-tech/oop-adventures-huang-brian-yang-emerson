import json, os

class Player:
    def __init__(self, SaveID, Stats) -> None:
        self.SaveID = SaveID
        self.Stats: list = Stats
    
    def UpdateStats(self):
        with open('Saves.json', mode='r') as infile:
            AllData = json.load(infile)
        
        AllData[self.SaveID] = self.Stats
    
    def TakeDamage(self, Damage):
        for item in self.Stats["Inventory"]:
            if item["Type"] == "Armor" and item.get("Wearing", None) == True:
                Damage *= (item["Defense"] / 100)
                item["Durability"] -= Damage.round()

                if item["Durability"] < 1:
                    self.Stats["inventory"].remove(item)
                    print("Your Armor Has Broke! You Will No Longer Get Reduced Damage Until Another Armor Is Equipped")

                if self.Stats["Stats"]["HP"] < 1:
                    print("You Have Died! Your Last Health Points Have Been Saved. Please do not try to re-enter the game as you have proven too weak.")
                    os.abort()
                else:
                    self.UpdateStats()