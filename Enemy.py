import random,time

class Enemy:
    def __init__(self, name, hp, attack, exp, chance, description, movementchance) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp = exp
        self.chance = chance
        self.description = description
        self.movementchance = movementchance
        self.CurrentEffects = {}
    
    def TakeDamage(self):
        pass

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
        x = self.name+":           "+str(self.hp)+"/"+str(self.maxhp)+" HP"
        print(x.center(80))
        x = "Attack: "+str(self.attack)+"      Status: "+self.status
        print(x.center(80))
    def Desc(self):
            x = '"'+str(self.desc)+'"'
            print(x.center(80))
            time.sleep(3)
            
    def Encounter(self,dungeonlvl,playerlvl):
        if not playerlvl > dungeonlvl + 25:
            EncounterTxt = [self.name+" blocks the way!", self.name+" approaches you!", self.name+" makes its appearance!", "It's "+self.name+"!"]
        else:
            EncounterTxt = [self.name+" is in YOUR way...", "YOU approached "+self.name+"...", "YOU appeared before "+self.name+"...", "It was "+self.name+"..."]

        txtNum = random.randint(0,len(EncounterTxt)-1)

        print(EncounterTxt[txtNum])
        time.sleep(3)

    def TakeDamage(self,damage):
        self.hp = self.hp - damage
    
    def Attack(self):
        attack = random.randint(round(0.5 * self.attack), round(1.5 * self.attack))
        return attack

    def UpdateStatus(self,effect):
        if effect != "None":
            self.status.append(effect)





    
