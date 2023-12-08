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
    def Check(self,name,hp,maxhp):
        print(name+":           "+str(hp)+"/"+str(maxhp)+" HP")
    def Desc(self,desc):
            print('"'+str(desc))
    def Encounter(self,name):
        print(name+" blocks the way!")
    def TakeDamage(self,name,hp):
        self.hp = hp -10
        print(name+" took 10 damage.")
    def DoDamage(self):
        self.CurrentEffects = {
            'Poison': {
                'Strength': 1,
                'Rounds': 10,
            }
        }
    
    def attack(self):
        return random.randint(self.attack * 0.9 , self.attack * 1.1)


whalen= Enemy("WHALAN",10000,10000,100,1000,0.01,"The final project. This enemy has a handsome beard and a forehead that luminates the dark.")

whalen.Encounter(whalen.name)

whalen.Check(whalen.name, whalen.hp, whalen.maxhp)
whalen.Desc(whalen.desc)

for i in range(10):
    whalen.Check(whalen.name, whalen.hp, whalen.maxhp)
    whalen.TakeDamage(whalen.name, whalen.hp)
    
