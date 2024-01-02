import json, os, random


with open("Weapon list.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)


class Player:
    def __init__(self, SaveID, Stats):
        self.SaveID = SaveID
        self.Stats: list = Stats
    
    def UpdateStats(self):
        with open('Saves.json', mode='r') as infile:
            AllData = json.load(infile)
        
        AllData[self.SaveID] = self.Stats

        with open('Saves.json', mode='w') as outfile:
            json.dump(AllData, outfile)
    
    def ETakeDamage(self, EnemyAttack):
        for item in self.Stats[len(self.Stats)-1]:
            if item["Type"] == "Armor" and item.get("Wearing", None) == True:
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
    
    def TakeDamage(self, EnemyAttack):
        Damage = int(round(EnemyAttack,0))
        if self.Stats[7] != "None":
            Damage *= ((Damage-self.Stats[8]))/Damage
            Damage = int(Damage)
            self.Stats[8] = self.Stats[8] - int(round(Damage,0))

            if self.Stats[8] < 1:
                self.Stats[7] = "None"
                print("Your Armor Has Broke! You Will No Longer Get Reduced Damage Until Another Armor Is Equipped")

        self.Stats[1] -= int(Damage)

        print("You took "+str(Damage)+" damage.")

        if self.Stats[1] < 1:
            print("You Have Died! Your Last Health Points Have Been Saved. Please quit the game forever and leave.")
            os.abort()



    def attack(self):
        Found = False

        for item in self.Stats["Inventory"]:
            if item['Type'] == "Weapon" and item.get("Equipped", None) == True:
                Found = True
                return random.randint(0.9 * item['Attack'], 1.1 * item['Attack'])

            if not Found:
                return random.randint(9, 11)


    def Attack(self):

        for i in range(len(data)):
            if data[i]['Name'] == self.Stats[9]:
                break

        if self.Stats[9] != "None":
            attack = random.randint(round(0.9 * data[i]['Attack']), round(1.1 * data[i]['Attack']))
            attack += self.Stats[2]
        else:
            attack = random.randint(9*(self.Stats[2]+1), 11*(self.Stats[2]+1))

        return attack