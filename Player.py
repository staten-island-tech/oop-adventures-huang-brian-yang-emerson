import json, os, random

class Player:
    def __init__(self, SaveID, Stats):
        self.SaveID = SaveID
        self.Stats: list = Stats
    
    def UpdateStats(self):
        with open('Saves.json', mode='r') as infile:
            AllData = json.load(infile)
        
        AllData[self.SaveID] = self.Stats

        with open('Saves.json', mode='w') as outfile:
            json.dump(AllData, outfile, indent=4)
    
    def AddExp(self, exp):
        NeededExp = self.Stats['Stats']['Level'] * 100
        CurrentExp = self.Stats['Stats']['Exp']

        TargetExp = CurrentExp + exp

        if TargetExp >= NeededExp:
            LeftOverExp = NeededExp - TargetExp
            self.Stats['Stats']['Level'] += 1
            self.Stats['Stats']['Hp'] = 100 + (self.Stats['Stats']['Level'] * 50)

        else:
            LeftOverExp = TargetExp
        
        self.Stats['Stats']['Exp'] = LeftOverExp

        self.UpdateStats()    
    
    def ETakeDamage(self, EnemyAttack):
        found = False

        for item in self.Stats['Inventory']:
            if item["Type"] == "Armor" and item.get("Equipped", None) == True:
                found = True
                Damage *= ((EnemyAttack - item["Defense"]) / 100)
                item['Durability'] -= Damage.round()
                
                if item["Durability"] < 1:
                    self.Stats['inventory'].remove(item)
                    print("Your Armor Has Broke! You Will No Longer Get Reduced Damage Until Another Armor Is Equipped")

                if self.Stats[1] < 1:
                    print("You Have Died! Your Last Health Points Have Been Saved. Please quit the game forever and leave.")
                    os.abort()

                else:
                    self.UpdateStats()

        if not found:
            self.Stats['Stats']['HP'] -= EnemyAttack

    def attack(self):
        Found = False

        for item in self.Stats["Inventory"]:
            if item['Type'] == "Weapon" and item.get("Equipped", None) == True:
                Found = True
                return random.randint(0.9 * item['Attack'], 1.1 * item['Attack'])

        if not Found:
            return random.randint(9, 11)

# The Final Boss Should Be A Perfect Copy Of Yourself. Just simply inherit the saveId and Stats.
class FinalBoss(Player):
    def __init__(self, SaveID, Stats):
        super().__init__(SaveID, Stats)