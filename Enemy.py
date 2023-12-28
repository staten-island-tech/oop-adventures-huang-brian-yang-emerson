import random,time

class Enemy:
    def __init__(self, name, hp, maxhp, attack, exp, chance, desc, status):
        self.name = name
        self.hp = hp
        self.maxhp =maxhp
        self.attack = attack
        self.exp = exp
        self.chance = chance
        self.desc = desc
        self.status = status
    def Check(self):
        print(self.name+":           "+str(self.hp)+"/"+str(self.maxhp)+" HP")
        print("Attack: "+str(self.attack)+"      Status: "+self.status)
    def Desc(self):
            print('"'+str(self.desc)+'"')
            time.sleep(5)
            
    def Encounter(self):
        print(self.name+" blocks the way!")
        time.sleep(3)

    def TakeDamage(self,damage):
        self.hp = self.hp - damage

    def UpdateStatus(self,effect):
        if effect != "None":
            self.status.append(effect)





    
