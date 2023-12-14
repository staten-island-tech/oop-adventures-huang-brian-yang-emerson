import random

class Enemy:
    def __init__(self, name, hp, maxhp, attack, exp, chance, desc):
        self.name = name
        self.hp = hp
        self.maxhp =maxhp
        self.attack = attack
        self.exp = exp
        self.chance = chance
        self.desc = desc
    def Check(self):
        print(self.name+":           "+str(self.hp)+"/"+str(self.maxhp)+" HP")
    def Desc(self):
            print('"'+str(self.desc))
    def Encounter(self):
        print(self.name+" blocks the way!")
    def TakeDamage(self):
        self.hp = self.hp -10
        print(self.name+" took 10 damage.")
    def DoDamage(self):
        self.CurrentEffects = {
            'Poison': {
                'Strength': 1,
                'Rounds': 10,
            }
        }



    
