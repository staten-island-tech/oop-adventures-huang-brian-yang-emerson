import json, os
import Enemy

class Player:
    def __init__(self, SaveID, Stats) -> None:
        self.SaveID = SaveID
        self.Stats: list = Stats
    
    def UpdateStats(self):
        with open('Saves.json', mode='r') as infile:
            AllData = json.load(infile)
        
        AllData[self.SaveID] = self.Stats

        with open('Saves.json', mode='w') as outfile:
            json.dump(AllData, outfile)
    
    def TakeDamage(self, Damage):
        for item in self.Stats["Inventory"]:
            if item["Type"] == "Armor" and item.get("Wearing", None) == True:
                Damage *= ((100 - item["Defense"]) / 100)
                item["Durability"] -= Damage.round()
                

                if item["Durability"] < 1:
                    self.Stats["inventory"].remove(item)
                    print("Your Armor Has Broke! You Will No Longer Get Reduced Damage Until Another Armor Is Equipped")


                if self.Stats["Stats"]["HP"] < 1:
                    print("You Have Died! Your Last Health Points Have Been Saved. Please quit the game forever and leave.")
                    os.abort()
                else:
                    self.UpdateStats()


