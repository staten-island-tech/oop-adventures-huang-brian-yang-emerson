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
        dialogue = []
        if self.name == "Chief Goblin":
            dialogue = GoblinChiefDialogue
        elif self.name == "Goblin Gang":
            dialogue = GoblinGangDialogue
        elif self.name == "Pharoah":
            dialogue = PharoahDialogue
        elif self.name == "Eyed Coffin":
            dialogue = EyedCoffinDialogue
        elif self.name == "Shark-man":
            dialogue = SharkManDialogue
        elif self.name == "Kraken":
            dialogue = KrakenDialogue
        elif self.name == "Demon king":
            dialogue = DemonLordDialogue
        elif self.name == "Death":
            dialogue = DeathDialogue
        else:
            dialogue = None

        if dialogue != None:
            print(f"{self.name}: ", end="", flush=True)
            if turn > len(dialogue):
                for char in dialogue[-1]:
                    print(char, end="", flush=True)
                    time.sleep(0.1)
                time.sleep(1)
            else:
                for char in dialogue[turn-1]:
                    print(char, end="", flush=True)
                    time.sleep(0.1)
                time.sleep(1)

            time.sleep(3)
    
    def BossDeath(self):
        DeadBossDialogue = []
        if self.name == "Chief Goblin":
            DeadBossDialogue = GoblinChiefDeath
        elif self.name == "Goblin Gang":
            DeadBossDialogue = GoblinGangDeath
        elif self.name == "Pharoah":
            DeadBossDialogue = PharoahDeath
        elif self.name == "Eyed Coffin":
            DeadBossDialogue = EyedCoffinDeath
        elif self.name == "Shark-man":
            DeadBossDialogue = SharkManDeath
        elif self.name == "Kraken":
            DeadBossDialogue = KrakenDeath
        elif self.name == "Demon king":
            DeadBossDialogue = DemonLordDeath
        elif self.name == "Death":
            DeadBossDialogue = DeathofDeath
        else:
            DeadBossDialogue = None

        if DeadBossDialogue != None:
            for i in range(len(DeadBossDialogue)):
                print(f"{self.name}: ", end="", flush=True)
                for char in DeadBossDialogue[i]:
                    print(char, end="", flush=True)
                    time.sleep(0.25)
                time.sleep(1)
            time.sleep(3)

GoblinChiefDialogue = [
    "Ooga Booga?! (You dare enter my territory?!)\n",
    "Ooga Booga! (Begone!)\n"
],
GoblinChiefDeath = [
    "...",
    "Ouch."
]
GoblinGangDialogue = [
    "Ooga Booga! Ooga Booga!!! (Look over there! It's the person who killed our chief)\n",
    "Ooga Booga! (We will avenge the chief!)\n",
    "OOGA BOOGA! (Die!!!)\n"
],
GoblinGangDeath = [
    "*All of them die*\n"
]
PharoahDialogue = [
    "WHO ARE YOU TO AWAKEN ME FROM MY SLUMBER?\n",
    "YOU SURE HAVE ALOT OF GUTS!\n",
    "HAHAHA!\n",
    "OH? YOU'RE APPROACHING ME?\n",
    "INSTEAD OF RUNNING AWAY, YOU'RE COMING TOWARDS ME?\n",
    "VERY WELL! GET AS CLOSE AS YOU LIKE?\n",
    "YOU'RE NOTHING TO ME, BUT A SMALL PEST IN THE WAY!\n",
    "A QUINTESSENCE OF DUST, THAT'S WHAT YOU ARE!\n",
    "A LITTLE SPECK, IN THE GRAND SCHEME OF THE WORLD!\n",
    "AND YOU THINK YOU CAN CHALLENGE ME?\n",
    "FOOLISH BEING! I WILL CRUSH YOU WHERE YOU STAND!\n",
    "TIME TO DIE!\n"
]
PharoahDeath = [
    "WHAT!\n",
    "IMPOSSIBLE!\n",
    "THIS...CAN'T BE!\n",
    "BUT...\n",
    "I'M...\n",
    "THE PHAROA...\n"
]
EyedCoffinDialogue = [
    "W̴̭̞̺̗̺̣̱͒̑͒͌̀̒̇̕ḩ̷̛̬̼̫͉̭͋̔̄̎̀̂̃͌̇͛͝͠y̷̡̛̬͉̦̠̝̞͇͌̂̔̈̑́̀͘͠ͅ ̴̢̧̛̣̈́̐̓̉̌͛͑á̸̙̜͔̰͉̜̱̙̺̻̓͊́̈́̕͘ȓ̷̟͛e̷͎̗͔̼̪̞̓̔̈́ͅ ̴͕͈̻̰̭̻̙̤̘̹̀̀̒͒͊̈͆̉ͅy̴̨͕͙̩̪̙͕̩̘̯͖̒̋͐́̌̆́̄͜ó̶̜͈̲̼̪̩̖͎̳͕͚͚͕͎̀̆͜ų̴̣̠͎̝̟̲̼̪͉͖̝̗̒́ ̷̡̢̝͍̲̮̹͕̩̩͔͖̩͉͈͋̅̀̃̽͊̃h̸͖̻́̈́̈́͊̉̑́͊͑̓͘̚͝͝e̵̢̛̜͍̼̼̳̪̾̈̍̍̈̾͊͐̚͘͠r̵͎͍̩̬̝̦̟̪͇̜͕̬̩̖̙̾̑́̀̎̋̃̐̊̈́̒̋́̚è̷̢̳̙̉̊͐̅̿̂̏̓̑̒͌͊̚͝?̷̯͂͋̏̿̑̉̂̃̅͊\n",
    "J̷̡͇̠̠̲̌ư̸̼̤̟̔̊͑͑͆͘ṡ̵̞̰̤̖̮̱̻̬̯̘̪̀͆t̷̛͇̬͍̟̜̞͂̃̌͛͂̾̇̒̕͘͠͝ ̸̨̩̖͓̼͈̮̖̖̻̮̹̈́͑̈́̽͊̉́t̴̜͖͑́́̀̀̃̀͑̋̚͠͝ò̴͕͈̼̥̚͘͝ ̶̙͖̼̩͋s̵̬̪̈́̾͌̅̿͋̃͆͝ư̵͖̘͍̹̈́͑̌͆͒̃̉͂̕̕̕͝f̶̛͎̼͂̾̀̓̐̇̄̒f̸̫̪̬̘͕̫͗̓̈̑͋̍̈́̒̂͝e̵̡̨̢̧̼̤̞̣̫͙͔̥̜͊̉͐͛͋̾̊̃r̷̪̓̈́̐͋̓̀̈̔͑̽̚͠͝?̸̧̫̯͙̆͑͋̒͋̓̀́̈́͆̇̆͝\n",
    "Ḩ̴̱̖̘̜̱̥͉̆̊̈́̊̎́͐̾ō̴͕͉̪̝̬̠̺̾̃̂̇w̴̫̯͛ ̷͍͇͉̯̗̞͐͐̈́̾́͋̍̾͗̍̓̄̿̀̕F̴̛̼̮̠̗͖̭̖̎͒̃̇͑̍̃̚͠͝ô̷̖͎̓̈́̔̀͑́̒͘̚ó̷̡͖͙̩̤̪̯̗͒̔͐̽͑̀͌͜͜͜ͅl̵̨̧̛̲̗͎̪͉͔͙̗̯͉̊̀̀͂̅̿̌͐̐̍̈́̌̈́͜͜i̴̠̝͉̜͔͍̒̒̍̈́̒̃s̴̡̛̮̯̲̘̠͈̣̘͙̟͑͐̈́̈́͊̋̓͂̀͗̚̚͝h̶̝̱̼̱̞̭̬̩͖͛̀̌͌̄͘͘͠.̶̢̙̩̜̜̝̍̍.̶̧̧̨̪̤͍̯̗̼̯̮̺̙̲̩̀̋̀̽̈̑̈̕.̵̧̟͚̹̝͗̏̔̏̎͘͝\n",
    "Ÿ̴̫̯͚̮͔̝͍̺̺͍̬́̊̓͐ͅͅò̷̢̲͇̥̠͔̘̲̭̫̂̌̊͝͝u̸̢̢̖̖̓̀̀͂́̅͐́̊̄͜͝͝͝ ̶̭͖͆̀̇̑͆w̵̪̳̟̓̀̃̋͌͐͘į̸̭̯͎̱͙͈̑̃͛̿̑̊ľ̶̹̃̈l̵̛̜̟͕͖͇͔͍̜̼̀̊͛̓̐̈́̆̓́͋͗̚͝ͅ ̷̨̜̯̣̝͚̺̓̇͊͆̄͜͠͝ḑ̴̨̛̺͔͈͎̹͐̉͜i̵̧̢̯̭͊͊ȩ̵̦͈̙͎̺̙͍̤͎̜͔̒́̌͊͜͝ ̴̡̢̖͓͙̝̬̪̥̬̫͔̟́͑͛̀͋̾̑̾̈̀͘͝͝͝w̸̢͍͔͉̤͙̬̻̙̜̦̟͛̈̑́̆͂̏̇̄̀͜ḥ̶̣̑̏̿̉̏̒͛̅͒̋̌͂̚̕͠e̴͚̜̦̺͔͒̓̂̇r̴̭̊̎̀͒̔̈̑̃͂̐̚̚͘͝é̵̼͔̯ ̵̢̣̦͍͓͈̝̦͌̿͊̿͋͊͗͋̈́͊̕͜y̸̖̩̳̕͝o̷̰̺͍̱̝͕̯̲̣̩̓̀͌͗u̴̻̟̞͈͕͍͑̓̓̓͗̌̾̅̀͝ ̷̰̙̜̦͓̓̒̽̀̏́ͅͅs̵̛̬̫͉̟̲̓̋͛̓͑̒̚͘t̶̛̮͉̟̯̝̩͈̞͈͕̭̬̫͑̈́͗̃͗̈́͐̊̏͛͘͘a̶̛̤̘̒͊̇̍͆͑͂̔͠͝ͅn̶̢̡̛̮̝̯̬̬͉̺̰̮͕͐̓͑̈́͐̉̾̔́̀͋̕d̶͇͉̰̝̘̗̺̳̺̯̪̋̇͆͆̾̈́̋̾̓͌͋̉̈́̕͝\n",
    "...\n",
    "...\n",
    '"̴̨͇̼̭̳͕̳̜̙͍̣̪̽͋̅͘ͅW̷̞̭̯̦̒̾͐̇͐̔͛̄̉͊H̵̢̖̲̪̙̝͙̞̻̟̯̯͓̔̔̕͜ͅI̶̘͙̟̫̯̯̭͔̗̥͙͑̑̒͐̐̎̏̐͗̏͑̕S̴̬̟̼̗͊͝P̴̨̡̘̪͍̭̬͉̯̦̱̑̉̓͒̌͗̂͊͂̀͝͠ͅȨ̷̧͔̣̘͚̞́̒͠͝Ŗ̴̺̜̪̦̝̪̱̯̪̠͂͑̔͜S̴̨͕̝͉̄̾̅̐́́͘̚ ̶̧̡̥̮̪̮̖̳͇̂͑̊̆̋̽ͅĮ̶͈͔̿̃̒́̋̏̋̿͒̋͐̿̓͝N̷̡͔̯͓̝͓̬̤̑̃̈̚͜͝ ̶̢͍̗̘̥̯͈̞̺̍̓̏̆̅͒Ť̶̨̡̛̩̻̫̲͖̲͎̫̬̣͒̓̃̊̏̋̌͘ͅH̴̨̢̺̫̮̰͍̱̯̰͗̈́̍̃͊̂̚Ȇ̵̛̞̥͎̀̐̈̍̆͌͘͜ ̴͔͚̮̱̟̮̱̯̖̂͝D̷̺͓̺͙̗̫̠̭͈̣̯̪̩̏̓̉̎̇̀͆̒̅̐̓̕͝A̸̛̫̯̱͔̲̬̝̫̮̭͖̙̳̭͔͑̌̈̋́̀̓͠R̶̡̛̠͕̯̤̙̎̇̇̾͊̓͛͊͂̂͠͝K̵̢̞̦̪͈̜͂̇͐"̸̨̨̛̖̫͈̣̬̥͋̎̍͆͊̈́̉̀̍́͜͝\n',
    '"̶̡̨̨̛͕̻͔̓͒̐̇̅̂̌̉͛̒͘͘͝Ṭ̴̘͍̠͉̥̘̦̱̺͎̤̫̣͒̽̐́͘̕͘Ȟ̶̖̝̝͖̫͕̜́̉̃̽̏̌̓̈́͜͜͝Ĕ̶̞̳͈͕̫̦̮̐̽̈́͒̒͘Y̸̱̠̰͔̤͙͖̞̠͓̲͌̂̕ͅ ̴̬̞̘̊̈́̑́͌̇͌͛̈̂͗̋͘S̶̢̻̩͈̦̘̱͎͙͛̇́̾̈̐͜P̵̢͉̻̥̈̑́̎̄̋̈̑̽̈́͗̄͝͝E̸̬̱̞̯̫̺̥͉̳̓́͗̌́̿̏͜͠A̷̩͔͎̘͈̹͖̐͌͗̾̓̊͑̈́́̑̈́̚͝͠K̴̯͇͈̦̭͔̈́̈́̋́̿͛͘͜ ̶̤̹̼̤̘̘̞͜͠T̶̳̻̼͎̹̣̼͔̗͇̿́͒́̔̊̄͂̏̉̎̊͝Ȯ̷͚̞̳̼͈̠̭̣̱̈͂̈́͑͊͝͠ ̴̠̲͈͕̦̘͖̝̐̀̾̊̿͑̓̒̾̐̉͛̚͝M̸̛̛͖͍͒̍̾̈̇̔̆́̏̿̕̕͜͝Ę̷̨̪̙̳̤̼̺͉͖̗͙̗̣̼̏̊̆͒͆̉̑͂̌́͠͠"̶̡̭̠̹͖͉̟͍͈̜̤̙̘̲͋̌͊͊͌̆̀̀̓\n',
    '"̷̨̛̻̭͚̣̜̬͔̬͈̝͔̪̝̅̾͗̊̀̂I̴̛͙̤̠̮̣̹̾̽̓̋̽̊̑̋̌̅̚ ̴̨̢̧͓̙̮̻̰͔͚͈͍̇̈̉͒̂̎͋̌͊̀͊̌͑̚̕N̴̢̲̥̤͌͛̈͒̀̈́̊̓̃́̓̀͝͝͝Ő̸̧̢̫̳̤̠̺̙̬̭͎͖̘̾͑͋̀̓̕͝͠͠ ̸̫̼̳̺̹̖̦̲͉̽̒̒͐̈́̄͊̊͆̌̀̌L̷̢̨͈̫͕͎̲̹̳̐̍̇͒̆̆O̷͕̭̣̼̱̮̮̮̪̳̻̎̀̌̍N̶̢̮̺͙̣͎̾̋̔̎̄͗̎̀̊͊ͅG̷͔̪͒͌͗̒̑̆̇̋͂̓̿͌̈̈͠E̷̛̛̻̯̫̬̜̥̘͙̻̙̊͐̐͊̅̐͊̐̽͐͘R̶̝̖̦͇̦͑̔͊̈͂ ̴̛͓̙̻̓̈́̐͐͗̑͌͂̒̌̏̃̕Ņ̶̝̭̜͈̺͇̟̮̣͉͓̱͌́̓̾̏̆̎̃͗͑̅͆͝͝E̶̢̛̲͕̣̲̬͈̫͉͓͍̋͌͊̔͋̾É̴̛͇̪͓͑̊͂̐̅̍̂̍͗̓̏̈D̵͈͍̼̯̖͑̒̏̍́͐̍̾͂̎̚ ̸̺͕̘̼̲̪̹̼̪͎̓̉̔̈́͗͒̏͝͝͝͠M̶̘̹͓̳̟̦̠͓̋͋̐͗̏̋͒͐̉ͅY̷̡̺͖͌̀̐̃̇́͋̕͘ ̷̪̳̤̌̄͋͒̾͂̅̚̚Ė̶̟̟̎͛͊̉̋̍̈́̂̐̾Ỳ̷̪̀͆͊͌̉͂̍͊͘͘͜E̶̦̪̪͖͋͆̋̂͋͌̄̊̅͆́̈́S̴̡̨̳͕̬̝̅̓̒͗͜ ̷̢͈̭̻̩̞̘̣̜̲̈̀͋͌̽̄͌̋̆͂͜͜͠T̵̢̻̥͉̟̤͉͊̿̀́́̅̃́̌̒̊̈́̂͜ͅỌ̶̡̮͈̠͚̖͍̹̆͒͋ͅ ̵̢̡̞͓͍̱̦͔͖̠͙̖̎͒G̷̢̥̫͎͙̝̱̩̥̥̰̙̖̐̈̔̾̈́͊̂̊͝͝͝ͅȖ̴͇̟̙̖̫̣̱͈͖̖̈̋͋̄̃̅͗̓̍̍̉̋̇̚ͅI̴̡͈̰̺̩͚͖͔̹̼̟̜̲͂̌̀̈̀̄͒̐̅͐͋̑͋͜͝D̴̛̟̥̼͚̗̝̟̗̦̪̳͉͎̍̒̏͆̐́̈́̀̊̊̊͜͠Ę̴̧̤̩̎̓͌̊̕ ̸̡͉͓̱̙̹̼̇͗͌̽̒̄̒͘M̷̨̪̬̰̞͊̿̈́̃̂̀̊̏̽̆͝͠͝Ȩ̴̨̦̼͈͇̥͚̮̮̯̮̪̘̞̓̄̏"̴̧̡̨͖͔̖͙͓͉̹̙͎̯̱̒͝ͅ\n',
    'T̵̨͈̝̩̞͖͔̩̋͒̊͆͠Ḧ̵̨̬̲̰͍͉̗̟͙̭́̔̑͛̈́̚͝͠E̴̛̗̟͕̰̰̒̉̑͝ ̵̯̤͈̯͈̞̞̪̱͓̳̏̊͌͌̉̊̔̇̉͒̾́̀D̸͓̝͑̀Ặ̵̡̧̦̝͔̠̯R̶̢̳̮͇̤̫̖̩̰̓̄͘͝K̶̡̦̦̝̱̙̰̏͌̋͑̈́̽̂͌͗͐̏͝͠N̴̢̠͖͍̬͔͎̹̤͙͎͎̪̮͆̓E̴̙̝̰͚̬͋͑́̆S̴̢̨͍̫͕̞̝̞͔̽̀Ş̴̧̣͙͎͓̟̪͉͓͉̠͓͔̎̽̋̀́̀̂̑͌͊̈́̅̚͝ͅ ̶̧͈̩̥̮̖̩̙̿̊̋͆̒̂̈́̾̽̀̍̕͜͝͠Ṯ̶͕̄̄̿͗̄̌̎͘̕͠͠O̸͖̲̳͉̰̟̓̂Ư̷̛̠̮̫̘̱̻͆̆͂͒̋̽̈͆̾̃͝Ç̴̛̪̥̦̠͍̯̠̜̑̀͂̅̚͠Ḧ̸̹͙̳̙̺͓̻̮̳̇͊̋̌́̂̈̾̏̈̌̿̎ͅE̷̹͛̚͝S̷̛̛͈̥̰̹̔̆̂͂̿͒͆̅̒̕͜ͅ ̴̻̫͗̈̐̄̋̊͝A̴̡̧̹̟̣̗͇̭̪̘̭̣͙͉̒̅̍̑̐͛͐͗̆̊̾͠L̶̲̤̮͇̖̞͇̹̐̉̊͒͒̊̔́͜Ļ̷̥͙͎̭̩͔̱̪͕̣̠̘͗͋̉̂"̸̡̹͕̺̭͈̬̫̞͚̮̠̱̿͂̆̆͆̅́͝͝\n',
    "......\n",
    ".......\n",
    "...\n",
    "Ẁ̵͔͚̪̤͙͚̳̩̍͊͝I̷̹͋̎̐̓̐̄́̈́̀̄̚Ţ̴̪̟͈̬͖̿̉̏̈́̅̇͝H̶̖͚̖͇͔̭̙̖̦͋͋̉̑̌͌͊̎̒̕͘͝ͅE̸̪̍͆͗R̶͔͖͂ͅ ̷̞̩̦̺̻̩̲͕̂̌̌͑̇̚͝W̶͔̰̼̮̫͕̹̲͕͊͜͝Ḯ̴͇̳̳̏̒̽̕Ț̵̳̤̭͙̈́͊̂̑̅H̶̡̢̪̖̥̜̖͙͍͇̅̀̄͒̎͜ ̷̨̥̔̍̑̌̓͌M̷͕̠̬̯̜̦̰̼͔̉̉Ḙ̷̃̋̆̏̓̿̀͘͠ͅ ̵̦̲̫̙͕̭̒̓̍̀́̐̑Ẅ̸̩̯́̈̄̐̌Į̵̫̦̅̐̈͌̾̈̌͒͗Ṯ̵̛͋̅̓̇̃̊́Ĥ̸͚̖͋̓͜E̸̛͓̯̤̳̬͔͛̏̃͑̅̐̐͂̏̚R̶͖̝̙̼̼̺̥͖̯̗̠̉̓̓͜ ̶̢̨̣̺̼̂̂̂͐͜͝W̴̬͓̞̝͑͑̉͂̎̄͛̚ͅI̶̢̞̥̗͇̩̤͒͊͋̓͆̈́̕Ṱ̸̢̧͕̣͎̮̟̺̬͊͋͌͂͑̄͑̚ͅH̶̡̙͇͍̜͈̾́̐͜ͅ ̵̢̥̗̲̦̲͎̖̬̔̽́́̉͐͘̚M̴̛̫̟̱̻͒̀̈́͐̚E̴̡̗͕̿́̎̓̓̅́̄̒̈́͠ ̶̢̫̰̺͈͇͇̳͈̭̩̫̉̉̾̄͆͊͛̇͝Ẇ̴̡̛̬̦̿Ȋ̷̢̛͎̲͖̯̘̜̭̥̬̄̋̑͝͝T̶̫̲͔̘͎̼̟̤͖̖͂̂̀̀̅ͅH̵̢̛̥̪̲͕͈̟̺̄͒̑̾͐̈̎ͅE̷͕͈͉̦̰̋̽̏͋̎͒͘͘͝Ȓ̶̢̢̨̛̥͔̝̬̣͇̱͕̤̀͌͊̈́͊̚̚͝͝͠ ̴̨̲̤̟̰̱͒̾̇̄͑̂̆͋̀̓̇͠W̴̼͒͐̾̐̊̔͋͑̑İ̷̢̧͔͎̗̼Ţ̵̭͕̫̲̲̙̲̗̠̐́͌̐̀̃́͗͘̚ͅḨ̸̨̣̠͔̩͖͎͔̙́͆̌̄͗̚͘͜ ̷̢͔̜̹͇̜̐̅͌̓̔̊̇̐̈́̎̈́͂M̵̨̞̺̼͇̎̓̃̎Ë̵̢̢̛̼́͒͋͌͋̀̀ͅ ̵̣͎̈͆̔̀̋͆͌̊̀̓̕̚W̴̩̳͌͒͋̈́I̶͚̞̓́͋͂̈́T̴̫͎̼̹̻̩̜͍́̈́͂͂̊͗̈ͅH̶̰̋́̍̈́͋̆̅̾Ȅ̸̢͖̥̥̀̍̓̒́̓͂̈̚͘ͅṚ̴̨̭̙̹̼̣̮̲̜͑͗̒̀̓͂̆̐͌̐̑̚ ̴̹̆̈́W̷̠̞̠͔̦̋̂Į̷͖̬̳͔͛̌̚ͅṰ̷̫͖̊͋̔̈́́̃͘̚͠H̸̡̧̱̞̣͉͎̝͉̄ ̸̡̠͖̞̙̺͖͓̜͍̈́͒́̾̿͐ͅM̸̡̧̢̬̎̇̐̐͗E̸̜̗̪͚͌͛̈́̓̔͛͒͠ͅ ̷̢̛̛̱̠̒̒̉̃̆̋͛̄͠Ẃ̵̖̅̑̕I̵̧͓̮̠̥̹̱̎͒͗̌͌̈̎̚Ṭ̵̨̘̭̾͗̈́̎̆̂̇̚H̷̨̬̯̘̭͉̫̏͋̂́Ę̸͉͔̪͖̣͇͉͓͊̃͊̾͗͐͐̽Ŕ̸̛͍͉̠̙̗͓̭͉͈̣̄̿̎͝ͅ ̶̛̯͙̟̣̣͉̬̠̦̜̟͛́̄̑W̶̛͍̫̻̗͛̋͒̈͒̈́I̸̡̼̗͉̪̟̻̬̹͉͙̐̅̌ͅT̴̛̻̙͉̭͇̊̽̓̉͊̑͘H̶̖͙̗́̃͑͌̈́̍̒̐̉͝ ̶̮͕̯͛͐͊M̵̡̤̰̯̩͌̌͐̎̔̾̆̀̓͐̚Ë̵̡̛̛͓̳̜̖̣̙̩̬́̂̌̀͘ͅ ̷̢̡̲͖̺͇̣̇̌͗̂͑W̵̠̏̉̆̉͊Ȋ̵̳̈́̂͗̓̓͋̀̀̕T̴̫͍̪̫͕̝̼̜́̉̍̔̃̃̾͑̓͊̉̕H̴̨͈͓̲͙͛͂͐͐Ę̸͙͍̰͓͍̲̦̦͆̀͌͐̋R̸̡̼͍̳̣̬̤̗̃̐̀̓̈̀̾͐̽́̾͜ ̸̺̗̙͇̹͎̻͖̏̄̉̀̇͗́̂̏̄͘͠ͅẆ̸̢̧̠̰͙̭̗̲͎̏̉̈̅̏̄͋Í̸̧͈̼͙̭̪͓̝̩̺̍͛́͘͝T̸͙͎̠̝̦̜̙̤̰̜̠̺̀́̕Ḧ̴̩̘̫̼͓̺͔̟̞̒͊̒̾̚ͅ ̸̧̛̱̲̣̝͍͇̂̐̓̍̄͌͂͒͛̚M̶̢̲̙͇̖̺͔̰͙̫͓͙̀̅E̶͙̰͌͛̉̌́̔͑ ̶̤̙͂Ŵ̸̲̗̦̝̤͖͑̏͒͆̎Į̷̺̖̟͖͎̞̯͐͐̕͜Ţ̴̱͎͚͈̤̗̙̗̾̊́̑̓́̋̉̀͘H̵̱̹̩̫͈͔͉̄͐̆̍͂̚͝E̷̩̭̝̱̲̾̾̄̓͂̅̔͘R̴͈̬͙̳̱͇̦̻̩͚̭̿̾̌̌̿͗̕͝ ̶̨̻̗̬̣̩̥̺̮̱̲̆̾̇W̷̨̡̡͍͕̪͈̲͖͇̣̼̏̿̾̊͑̕͠I̶̡̫͎̬̗̱̪͇̬̝̙̔̀͠T̸̳͎̱͔̣͉̞̻̅̄̀̒͋͐̀̐ͅḨ̶̛̛̤͈͉̫̋͋͌̀̀̑̕͝ ̷̧̡̲̰̩̞̠̫̘͍̦̆̋͐̿̒̏͑̀̽M̵̜̤̽̒̏̐̾͝Ę̷̻̖̬̖̬̟̺̝͍͚̤̍̊̉̍̔͐̌̑̓̋̕͝ ̸̪̰͕̓̔W̷̘̯̬̗̓̈́͐̏̓́̕ͅḬ̵̗̱̼͉̈̑̚͜T̶̨̰̻̟͕͌̿̚͝H̴̲͈̼͔̺͚͖̬͉͓̐̊͒̚͝E̴̪͋͒͗͑͘R̶̪͚̫̺̗͙̼̯̂̌̓͘͠ ̷̲̣̥̭͙̞̩͎̟̃̐̉͂͠ͅW̵͇̞̠͇͍̭̲̗̉Į̴̙̳̳̗̖͔͉͔̥̘̔͂͋̅́̿̕̚̕͘͠͝ͅṰ̵̢̋͒͑̿͝͝H̷͙̹̰͕͙̹͎̣͓̀̀̀̀̌̉̏̀͐͆͠ ̶͓͉͌͊̎̎M̶̛͕̙̖̫͕̗̹͕̬̲̬̂͆̃͛̀͛͜͠E̷̢̦͈̜̝̻̼̳̼͚̳̋́͗͆ ̵̡̛͈̻̟͙͎̗͌̍̑̒̇̃̽̌̕̕W̵̧̮͖͍̠̥̮̹̍̽̉́̃̆̀̍̚Ȋ̷̢̛̛̖͓̺̠̖̮̹̭̠̮̺̈́̂͘͝͝Ť̷̐͆̓̿̒͂̍̊ͅH̶͖̣̰̓̈́̓̎̋̑̑̉̈̕E̵̛̦͎̬̍͌̋͐̀̊̕͘R̷̛̞͖̻̈́̈́͂͒̃̇͂̃̈́ ̸͖̥͚̜̼̎W̸̘̯̮͍̼̬̠̱̣̘̰̓̌͊̿͌̅̇͝Ȋ̴̛̱̜̣̮̣͇̖̻̤͈̊Ť̶̥̫̬̩̻̹̬͓͇͚̹̟̏̌̀Ḥ̴̢̺͚̝̙͉̘̩̜̫͇͊̀̓̓̀͐ ̴̡̛̭͚͙̰̳̱̱͉̏͌̀̓͂̔̄̎̒̿ͅM̴̢͎̦̗͈̝͓͙̰̺̝̹̀Ȩ̵̧̢͙̗̝̺̈́̇̊͐͐͆͑̓̂̚ ̶̢̦͙̳̹̞̰̩̜̦͍̓̇͋̀W̴̧̨͓̠͈̤̤̩͙̃͗̈́͋̔̆͘̚I̸̹͕͎̖͚̽͂͗T̶̨̨̻̝̖͇͎̻̫̀̅̃̊̐̽̑́̀̊̕̚H̷̙͈̪̤̠͊͌Ẹ̶͕̱̔͐̀͊̕͜͠ͅR̵̳͇̯̈́̿̕ ̶̛̬̰̣͈̒̊̒͌̾̄͋͘͘͝W̷̳͍̦̦͎͔̓̓̂̈́͋̋̏͜͜I̸̲̫̮̎́̅́͌T̸̛̠̠̠̙̟͔͖͖͌̓̔͐͂̽̉̉̏͜H̸̛͖͈̱̟͍̬̝̏̾̓̃̎́́͊ ̶͈̱͕͎̖̪̲̀̊̃͐̎̑̏͠M̸̙͒̑̅̌͗̽͆̾̿͗̂̕Ȩ̶̺̼̪̙͎̋͑͗͑̃̓͐̄̕̕ ̵̨̙̺̲͔́͆̃̚͠W̵̬̬̯͙̍̓I̷͍̍̿͛͛̎T̸̛͚̦̘͙̄̓̃͜H̶̯̦̝̠̀̃̔̽̓̔̀̊̽̀̄͋͜E̶̡͙̺̙̺͉̦̹̟̻͈̔͗͋͗́R̵̛̛͙̰̪̺̭̾̿̆͒̑̇̍ ̸̧̡̩͕̦̻̰̣͛̀̓W̶͙͇̾Ĭ̸͓̮̒̽̒̕T̵͓̆H̶̡̛̯͔̺̥̱̲͓̊͊ ̶̯̾͛M̴̢̺̤̳̦͓̠̺͖͖͕͍̀͂̽͐̆͆̅̕Ë̴̞̪̑̀̀͂̓̉̈̆̓͝ ̶̛͈̀͛͗͒́̉͂͒͌W̶̢̡̥̜̹̠͔̪͕̮̞̓͊͊̆I̴͔̼̯̰̲̜̲̓̑̓̊̒̋̕̕Ṫ̸̢̳̙͉̞̗̲̜̆͛̿̒̓̉̈́͋̃̊̐H̴̡̢͎͍̲̥̥̗̻̹̙̩́͋̕É̷̞̠̫́͠ͅŘ̵̢̲͍̍̏ ̵̱͔̤̻͊̉͂W̸̻̱̩͑́́́͛͗̀Ī̶̮͍̞̒͂̐̈́̓̓̔̽̚T̸̯̱̦̲̘͚̗̠͎̫͑̽͠H̴̤̟̬̖̠̼́̐͆̾͋̓̇͝͝ͅ ̴̧̗͚͍̦̅̂́̿̑̊͆̅͘̚͠͠M̸̨͖̫̫͖͋̚Ȩ̴͗͒̌̆ ̴̨̡̖̠͔̗̗̯̣͉̌̔̄̉̆͂̾̚͜W̷̢͎̞̤̦͖̱̹̪̜̕̕I̴̢̛̮̯͔͎͎͕̖̖̓͂̏͂͆́̕Ţ̶̖̰̳̜͓̜̘̑͛̒̄̈͛̔̾͗͜H̸̡̡̡̫̳̩̤̟̘̜̥͐̊̾̑̽̅̎̽͜Ḙ̷͛̇͆̋̄́̓̚̕̕R̶͙̳͓̩̲͂͆̊͊̇ ̶̡͉̥̘̼̼͓̰̪̖͚̀͗͗́W̴̨̫̺̘̹̜̲̪̞̓̔̈́İ̴̛̘̠̘͎̙̳̪̹̓͛Ț̸͉̞͉̗̟̻͕̠̥̙̑̈́͛̚͘ͅḨ̸̧̙̠̦̹̜̯̘̮̫̮̔́̅̌̈́̏͑͐̃̃̅ ̴̣̬͖̝̞̳̟͇̞̹̼̫̈͊̔͑͊͝͠M̴͙̰̫̯̺͈̠̭̎́̒̄̄̏̋̀̅͂̕E̷͈̖̩̺̩̜͇̠̭͎̥̥̊̀͝ ̷̡̛͔̪̥̥͕͎͚͎̌̀̔͊̕͝W̵̥̿͑͌̄̏̏̍͊̈́̀̍͠I̵̠̅́̾T̸̡̛͚̺̔́͑̒̃͑̐̈́̍́̈H̷̗̰̣̆̽̽̑̐͆̀̚E̷̤̓̃̓̽̈́̂͑̓͊̈́͝R̵̛̺̭̝̪̈́̊͐͝͝ ̸̢̢̝͎̟͔̜̠̜̲̒̆͝W̵̢̫̮̘͛͋̈̽̆̈͌Ḯ̴̖͓͇̱͔̝̅̈́͊̃͐̉̓͆͜͝T̷̡̜̱̦͓̹̤̖͕̱̓̓̈́̕H̵̛͓̯̺͉̭͔̟̰͖͝ͅ ̷̧͖̘͗̃́̏͆̀̈̿̐͋̚͘M̸̡̨͖͈͚͙̲͇̬̗͒̄̿̏͌̽̀͘̕͜ͅẼ̵̢̡̡̢͎̰̰͉́́̄̂͛͋͘̕͜͝ ̷͓̥̹͔̦̩͆̃̓̔̈́̌Ẃ̶̧̨̛͎͍͙͔̭̳̅͒̃̑̅͝Ḯ̷̯͍̼̗́̀͒͝Ţ̴̣͚͙̙̲̯̏͊̀̒͛̅͝H̷͉̣̲̞̓̈́Ḙ̴̡̡̨͎̻̠̭̙͗̾͌͑̍̄̕Ŗ̴̼̟̣̳͌̊̏͂͆̏̕͘̚ ̴̰̣͚̣̮͖̟̺̐̈̃̚͝͠W̸̺͐̊͗̈̋̀̈́̃I̴̢̬͔̱̍̍̎͋̈́́͒̆̊̐̚͜T̷̢̨͇̙̻̫̰̗̍̃͠H̸͙̱̥̩͐͗̽͊ ̵̥̳̞̱̟̙̘̜̗̱̆̇͜M̷̫̫̄̍̌̈̒̅̚͝͝Ḛ̷̹̳̪̼̘̺̠̀ ̸̧͚̙͎̜͇̈̎W̶͇̥̠̰͙͉̠͘ͅI̸̛͚̟͒͂̂͐T̵͎͆̂̄̉́̕͠H̷̝̱̜͙̯̰͎̤͇͇̲̊͝Ę̷͖̗̫̪͍̹̹̙̋͊̊͊͒̈́ͅR̶͚̬̜̘̠̃̆͗́̏̅̿͠ ̵̩͙͇̲̗͈̜̓ͅW̴̢̢̢̤̮̝̳̗͎̮̦̎I̴̢̯̦̹̙͖̼̊̈́̅̐̐͛̃͐̂̕T̵̯̥̙͍̰̘͇̮͉͈̳̎͐̿̿̒̈̈̋͆̕͠H̶̪͐ ̴̺͈̳͇̜͛͌͗͋́̍͛̅̐̚M̴̱̯̪̄̅͋̾̽͗̽͠͝E̷̺̗̪̹̋̆͛͒͆ ̶͚̜̫͛̍͌̏͘͠W̴͔͈̱̤̜̩͈͍̹͕͚̑̽̉̽̀͆̎̎͒̚͠I̴͖̳̤̳̪̝̺̼̐̓̉̽̎̆̽Ţ̸̡̧̭̬̤̬̦͙̲̙̱̆̋͌H̸̛̭̤̫̮̓͆͑͌̿̈́͊̊̂͐͜È̴̡̙͖̬͎̯̦̼̄͐͑̌͂R̴͇̯̣̲͎̠̈́̆̀ ̷̡͇̦̼̗̰͙̗͕̟̝̰̄̑͋̈́͆̌̏̾͛̚͝Ẅ̸̨̡̹̩͚͎̺̪̙̭́͑̉͌̈́͝Ḭ̷̧̦̯̪̦͎̩̏̎͝T̷̡͕̲̞̀͐̏̀͆̀̓̚͝Ḧ̶̱̙̤̝̥͇́́͘ ̵̢̢̢̡̧̟̫̰̳̞̟͍̍̈́̃̎͗̒̄̊̉͠͝M̴̡̨̩̏̿̾͐̓͛Ẽ̷̛̛͍͍͈̯̠̜͇̙̈͐̏̍͂͂̌̽̆ͅͅͅ ̶̤̞̼̦̟̈́̿͊̐͋͐͊̀͜W̸͓̫͓̮̓̑͝I̸̺̯̪̝̤͓̱͉̘͓̬̘̊̄̔̀̆̎͑̒͠T̴͚̞͑̾́͝Ḫ̴̮͈̰̖̦̿̓̍̂̀͂͘͝͠Ė̶̳̦̳̔͂̑͊̾͑͐͝R̷̲̳͓̙̘͙͍̩͊̒͌̒͗̓͑̆̋́͘ ̴͙̺͖̳͓̠̬̈̒̐̽̊̒̕͝ͅW̶̢̘̣̰͈̱̱͚͂͂̊I̴̖͖̓̃̂́̓̋͌̑͂̏͝Ţ̷͕̤̫̠̠̘̙̓̍̍̉̉͑̊̕͝Ḧ̵̙̜̩̩̠́ ̸̛͕̲̃̔̒̕ͅM̸̢͙̗̩͔̰͊̅̚E̴͇̦͇̭̻͒͌̈̈́͗̂͂ ̴̧̛͈̤̗͔͌͒Ẁ̵̪̠̠̺͍́͋͌̒̌̌̉̓͗Į̴̧̘̺̤̎̾͋̊̇̌͜͠T̴̨̨̛̞̻̺̲̪͚̺̓̾̍̑̽̾͜H̴̨͚̝̹̹̭̀̎͂͊̅̎̎̏̎̐Ḛ̸̡̧̢̡̞͕̺͙̻̪̈̑̍͑̀͂̉̊̋͌͌̋͜R̸̛̯̖̫͖͖̲̱͖̭͋̀̓̈̑͘͜ ̸̢̡̻̜̗̻̝̜̠̜̠̏̊̋̆͠Ẃ̴̥͈͗̈̋͛͘I̴̙̖̎̊̒̔̌͐̄̎̉̅̚T̸̺̖̳͍̮̮̃̾H̴̻̤͙͎͓͎̉̕̕ ̶̧͈̣͈̥̪̦͉͉̘͑̾̇̐́̂̈̌͐́͘̚͜M̶͉͉͓̗̌̇̿̐͝Ë̶̬́ ̶̨͙͓̺̖̰̞͍͛́̀W̸̢̡͍͕̝̅̎̈͗̓̐̌̄̚Ȉ̴͚̳̯̓͝Ṯ̵͑͒͆̒̒͂͗̕H̶̱͎̠̼̝̺̗̲̩̠͇̿̽́̂̑̔͜E̷̛̩͎̓̆R̷̠͉͑̔̿̃͆̌͊̋̚͘̕͝ ̴̢̦̲̗̪͖̳̰̞̰̊̌͑̊̾̉W̶͇̜̜͓̘̟̣̩̙̙̅̾̓̕Į̶̻̺̖͕̠̒̌̐͝T̴͙̄̅͐͒̽H̷̹̫͙́̓̎ ̵̡͉͖͙̺̓M̷͈͉̔̓͒͐E̶̢̨͇̼͚̩̟͖̟̺̠̒̃̀́͌̓̑̔́̕̕͠ͅ ̷̣͎̣̹̱̖̺̏W̶̛͇̳̭̑̐̅̍̐͒̊͒̋͝I̷͎͔̠̻͔̤͂͝T̷͔͍͖̯͕̗͍̃̈̔̇͂̏̌̌̕͘͠ͅH̵̤͗͋͠È̴̱̟̯̈́̈̚͝͝R̵̥̭̟̚ ̸̢̡̥͇̥̟̻̠̮̩̱̿̅̒̊͂͒͋̂̅͒̚ͅW̶̛͈̱̲̆̿̏̀̐̀̏̈́̀͐̕Ḭ̴̡͈͇̞̪͗̐͂́̒̾͗̚͝͝T̸͓̰̟̲̦̹̜͛̅̔̐̈́͑̆̌͛̓̑͜H̸̨̨̜̮͔̮̆͗́́̚ ̶̢̂̅̊̿̎̿̽̔̐͐̌͘M̷̩͔̋̒̈̌̈́Ę̴͔̹̩̬͌̒ͅ ̶̨̢̞͉̯͔̱̟̭͔̣̂͆W̵̛̙̗̘̗̥͕̘̠̌͆̓̆͋̈̆̈́̐͘͝Į̵̘̦̰̺͓͎̣̞̀̅͑̓͗̆̓́͗̽ͅŢ̵̢̢̳̘̖͎̭̥̮͕̀̔͐̿̇H̸̢̡̻͎̹̥̻͇̫̠͍̯͒̂̍͋̂̀̄̍̀̆E̴͖̯͚̪͎̐͐̓͌̄̆̄͒Ř̸͕̟̟̺͓͇̏̌̉̊̀́̉͆ ̵̦͍̜̺͂̇̽͑͜W̷̧͈͇͉̌̓̇̾̎̚I̶̤͙̹̖͈̰͚̭̳͑́͗͝T̸̡͙̟̙̜̫̮͈̀̅̈́͊̆̈̏̾̎̎̃͘Ȟ̵̨̠͕̖͍̠̘̪͂͗̿̉ͅͅ ̵̨̨̲̤̤͎͐̂̐̀̄̕M̴̛̯̜̓̈́͋̀͊̔̈̆̓͝E̴̝̤͔̣̬͎̲͑͐̀̒̋\n"
]
EyedCoffinDeath = [
    '"̷̦͔͐͋̆̂̆͋̔̿̆̕͝T̸͎̪̿̈͆͝ͅḨ̸̡̧̩̭̬͉̞̠̫̞̯̖̦̗̌̿̒̆͂͊͐̉̄̂͘͝Ȩ̶̨̗̪̜̼͉̮̭̱͙̏̋̽͋̆̃̒͊̓ ̴̧̢̛͍̲̻̠̳̘̲̦͓͉̔̋̍̔͂S̵͙͇̻͚͓͆̐͂͆̅ͅO̷͍͇͇̱͈̺̱̠͐̎̓͗̾̓͋͘͜͠Ṵ̷̡̠͍̗̖̩̜̤̹̹̎͋̏̾̀̾̚͠͠Ṇ̸͆̿͒̆͒͝D̸̛̼̮́͋̔̐̋͐͛̈͠͠͠ ̷̦̜̪̫̝̣̣͔̙͈̣́̋̅̀̚͝͠B̵̡̨͙̭͚̘͚͈̜̩̝̘̗̃U̸̝͎͕̗̦̱̜͍̩͛͐̑͑̀̄̈́R̵̪͓̯̖̯̟̳͕͍̹͋́͝͠R̷͉̙̬̋̃̀̅Ǫ̸̛̲̹̹̹̗̜́̅͗̐̽͒̑W̷̛̠̰̖̯̩̲̌̂̈́͂̄͒͆̚͠È̴̫̮̩̦͓̱̼̝͚͉̣̮͉̃͌͋̓͠Ḋ̵̢̨͕̣̭̰̘̜̩̪̏̔̂͋͠ ̵̛̹̳̰̙̏́͛̐̓̈̾͌̓̊̋̓͝D̷̟̦̙̯̜̀̌̐̈̌͆̋̀̂͊͒̚̚͜͠Ḝ̷̨̢̡̞̱̫̼͍̩̩̓̂̅̆̔̄̀̃̾̅̃̔͝ͅĘ̸̨̛̭̝̒͛͠P̵̢̼̼̫̭̺̪̩̯͇̘̋̓̅̎̀̋̈́̑̍̂̔͘͘ ̸̛̞̰̔̽̃̓͊͂̀̑̊̑̚͜͝Ȉ̷̧͈͙̞̥̗̫͌̿̈̿͑̍Ņ̷̜̝̳̳̝̭̤̙̩̥͈̅͗̍͋͘̚͝͝T̴̼̟̜͍̘̑͑̋͛̔͝Ő̶̺͕͍̠̥̞̌̎̂̂̽̽͒̉͗̐͘͝ ̷̡̳͙̹͕̱̗̪̒̋̐̏̃́̃M̷̛͕̩̦̬̂̓̂͐̉̐̈́̌̚͝ͅY̸̩̯͕͓̤̹̤̫̰̰͛̏̍̊̓ͅ ̷͉͉̗̓F̴̧̨̢̤͙͓̲̫͚̻̟̭̯̎́̿̓̀̑͐̈́͜͝͝L̸̝̞͕̠̙͍̭̠̳͎͎̞̺̟̇̈́́̏̃̈́͒̎͂͆̕͘Ȩ̸̢̫͙̝͉̤̲͚̮̳̜̫̱̾̽͌͠Ş̶̨͍̣̘͎̳̬͈̂̇ͅH̵̢͈͈͔̘̤̬̻̠̪͙̯͂̑̒̿̎́͋̔"̸̫̠̦͎̬͠ͅ\n'
]
SharkManDialogue = [
    "You're not here for business...\n",
    "I can sense the violent nature in you...\n",
    "It's...suffocating...\n",
    "I don't like you.\n",
    "Get out!\n",
    "I have a job to do!\n",
    "Stop bothering me!\n",
    "You're lucky I can't summon security!\n",
    "You've probably killed them all!\n",
    "I'm pretty capable myself...\n",
    "But you didn't have to kill all my employees!\n",
    "...\n",
    "I will destroy you...for the sake of the company...\n",
    "...\n"
    ]
SharkManDeath = [
    "...\n",
    "I...\n",
    "Damn...looks like I'm dying...\n",
    "My business was successful...where did it go wrong?\n",
    "...\n",
    "I see...\n",
    "It's not me...\n",
    "It's you...\n",
    "As long as you're here...\n",
    "Everything will fall...\n",
    "Damn...\n",
    "I didn't want to do this...\n"
    "...\n",
    "Release...it...\n"
]
KrakenDialogue = [
    "OwO\n",
    "UwU\n",
    "OwO\n"
]
DemonLordDialogue = [
    "...\n",
    "I'm honestly surprised...\n",
    "You're much eviler than I am...\n",
    "Damn...\n",
    "...\n",
    "Let's make a deal.\n",
    "Give me your soul...\n",
    "And together we'll rule the world!\n",
    "...\n",
    "No?\n",
    "Then burn.\n",
    "...\n"
]
DemonLordDeath = [
    "...\n",
    "Hey...\n",
    "Let's make a deal...\n",
    "Let me live and...\n",
    "...\n",
    "....\n",
    "Forget it...\n",
    "Not that you'll listen anyways...\n",
    "...\n"
]
KrakenDeath = [
    "O_O\n",
    "...\n",
    "QwQ\n"
]
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

    
