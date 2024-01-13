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
    def __init__(self, name, hp, maxhp, attack, exp, chance, Accuracy, desc, status):
        self.name = name
        self.hp = hp
        self.maxhp =maxhp
        self.attack = attack
        self.exp = exp
        self.chance = chance
        self.Accuracy = Accuracy
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
        if not random.randint(0,100) > self.Accuracy:
            attack = random.randint(round(0.5 * self.attack), round(1.5 * self.attack))
        else:
            attack = "MISSED"
        return attack

    def UpdateStatus(self,effect):
        if effect != "None":
            self.status.append(effect)
    
    def BossDialogue(self,turn):
        print(f"{self.name}: ", end="", flush=True)
        if self.name == "Death":
            if turn < len(DeathDialogue):
                for char in DeathDialogue[turn-1]:
                    print(char, end="", flush=True)
                    time.sleep(0.1)
            else:
                for char in DeathDialogue[-1]:
                    print(char, end="", flush=True)
                    time.sleep(0.1)

        time.sleep(3)
    
    def BossDeath(self):
        if self.name == "Death":
            for i in range(len(DeathofDeath)):
                print(f"{self.name}: ", end="", flush=True)
                for char in DeathofDeath[i]:
                    print(char, end="", flush=True)
                    time.sleep(0.25)
                time.sleep(1)
        time.sleep(3)

DeathDialogue = [
    "Hello...\n",
    "It seems it may be the end for you...\n",
    "Unfortunately, it is your time to go...\n",
    "Alas, poor soul...\n",
    "Struggle is futile... your demise is inevitable\n",
    "You lived a great life... but it has to end at one point...\n",
    "Consider it a honor to die in front Death itself...\n",
    "There is no struggle after death... you'll finally be able to know true peace...\n",
    "So stop struggling, embrace the darkness...\n",
    "And die...\n",
    "Goodbye...\n",
    "...\n",
    "...\n",
    "Why?\n" "Why do you keep struggling?\n",
    "You do know that there is nothing for you after this...\n",
    "You'll die at one point...\n",
    "Foolish mortal...\n" "Stuggle is useless...\n",
    "Please...\n" "Give up...\n",
    "I can't do my job like this...\n",
    "So Give up...\n",
    "Give up."

]

DeathofDeath = [
    "...\n",
    "I...\n",
    "Who are you?\n",
    "Why are you here?\n",
    "Just to mock me?\n",
    "...\n",
    "I'm trying my best, alright?\n",
    "It is hard trying to do my job everyday...\n",
    "And then you decided to show up in front of me...\n",
    "...\n",
    "Heh...\n",
    "...\n",
    "How do you feel?\n",
    "I bet you feel great...\n",
    "Congratuations... you beat Death...\n",
    "...\n",
    "Now what?\n"
]

    
