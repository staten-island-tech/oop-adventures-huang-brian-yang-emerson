import Enemy,Player,json,os,time,random


with open("DData.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

with open("Saves.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data2 = json.load(f)

with open("ItemList.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data3 = json.load(f)

with open("StatusList.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data4 = json.load(f)

enemy = []
playerStats = []

def enemyInfo(dungeonNum,enemyNum):
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Name'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Hp'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Attack'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Exp'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Chance'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['MovementChance'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Desc'])
    return enemy

def playerInfo(SaveID):
    playerStats.append(data2[SaveID]['Stats']['Gold'])
    playerStats.append(data2[SaveID]['Stats']['HP'])
    playerStats.append(data2[SaveID]['Stats']['Strength'])
    playerStats.append(data2[SaveID]['Stats']['Luck'])
    playerStats.append(data2[SaveID]['Stats']['Level'])
    playerStats.append(data2[SaveID]['Stats']['Vitality'])
    playerStats.append(data2[SaveID]['Inventory'])
    playerStats.append(data2[SaveID]['Armor']['Name'])
    playerStats.append(data2[SaveID]['Armor']['Durability'])
    playerStats.append(data2[SaveID]['Weapon']['Name'])
    playerStats.append([])
    return playerStats

def ConsumableItems():
    items = []
    print(playerStats[6])

    for i in range(len(playerStats[6])):
        for e in range(len(data3)):
            if playerStats[6][i] == data3[e]['Name']:
                items.append(playerStats[6][i])
                
    return items

def EnemySpecialAbilities(name):
    if name == "Cursed Mummy":
        EnemyAbilities = [["Poison",25,3],["Burn",25,3]]
    elif name == "Eyed Coffin":
        EnemyAbilities = [["Poison",75,9],["Burn",75,9]]
    elif name == "Death":
        EnemyAbilities == [["Wither",100,100]]
    else:
        EnemyAbilities = "None"

    return EnemyAbilities




class Battle:
    def __init__(self, defend, PStamina, PDefense, PAccuracy, UsedItems):
        self.defend = defend
        self.PStamina = PStamina
        self.PDefense = PDefense
        self.PAccuracy = PAccuracy
        self.UsedItems = UsedItems
    def PlayerTurn(self):
        Action = 0
        while Action == 0:

            os.system("cls")
            print(Opponent.name.center(80))
            x = str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
            print(x.center(80))
            if Opponent.status != "None":
                print(Opponent.status.upper().center(80))
            else:
                print()
            print()
            print("What do you do?".center(80))
            print("           ╔═══════════════════════╗          ".center(80))
            print("           ║ 1[FIGHT]    2[CHECK]  ║          ".center(80))
            print("           ║ 3[ITEMS]    4[DEFEND] ║          ".center(80))        
            print("           ╚═══════════════════════╝          ".center(80))
            print()
            print("[1][2][3][4]".center(80))
            print()
            print("You".center(80))
            x = str(You.Stats[1])+"/"+str(PlayerMaxHP)+" HP"
            print(x.center(80))
            x = str(E.PDefense)+" DEF"
            print(x.center(80))
            print(str(E.PStamina).center(80))
            if not You.Stats[8] < 1:
                x = "+"+str(You.Stats[8])+" ARMOR"
                print(x.center(80))
            else:
                print()
    
            if not len(You.Stats[10]) < 1:
                for i in range(len(You.Stats[10])):
                    x = You.Stats[10][i][0] + "("+str(You.Stats[10][i][1])+")"
                    print(x.upper().center(80))
            else:
                print()
    
            
            try:
                Action = int(input())
            except:
                Action = 0
    
        if Action == 1:
            if not E.PStamina < 5:
                os.system("cls")
                if not random.randint(0,100) > E.PAccuracy:
                    attack = You.Attack()
                    Opponent.TakeDamage(attack)
                    print(Opponent.name.center(80))
                    x = str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
                    print(x.center(80))
                    print()
                    x = Opponent.name+" took "+str(attack)+" damage."
                    print(x.center(80))
                    E.PStamina -= 5
                else:
                    print("Unfortunately, you MISSED!".center(80))
                
            else:
                print("You don't have enough stamina!")
        
            time.sleep(2)

        elif Action == 2:
            os.system("cls")
            Opponent.Check()
            Opponent.Desc()

        elif Action == 3:
            useitem = 0        
            while useitem == 0:
                os.system("cls")
                print("INVENTORY".center(80))
                for i in range(len(items)):
                    x = "item "+str(i+1)
                    print(x.center(80))
                    print(items[i].center(80))
                    print()

                print("X to cancel!")
                print("Use item (Number)... ".center(80))    
                useitem = input()
                useitem = useitem.upper()

                if useitem == "X":
                    E.PlayerTurn()
                    break

                try:
                    itemNum = int(useitem)-1
                    useitem = items[itemNum]
                    os.system("cls")
                    x = "You used "+useitem+"."                   
                    print(x.center(80))
                    E.itemEffect(useitem)
                    E.PdetermineStatChange(useitem,'HP',1)
                    E.PdetermineStatChange(useitem,'Attack',2)
                    E.PdetermineStatChange(useitem,'Defense',0)
                    E.PdetermineStatChange(useitem,'Stamina',0)
                    
                    E.UsedItems.append(useitem)
                    items.remove(useitem)

                    time.sleep(3)

                except:
                    useitem = 0
            
        else:
            os.system("cls")
            print("You braced yourself...")
            time.sleep(2)
            print("You regained some stamina and focus!")
            E.PStamina += 10
            E.PAccuracy += 10
            E.defend = "yes"
            time.sleep(3)

        os.system("cls")

            
    def itemEffect(self,useitem):
        itemNum = 0
        for i in range(len(data3)):
            if data3[i]['Name'] == useitem:
                itemNum = i

        for i in range(len(data3[itemNum]['StatusEffect'])):
            
            already = "no"

            for e in range(len(You.Stats[10])):
                if data3[itemNum]['StatusEffect'][i][0] in You.Stats[10][e]:
                    already = "yes"
                    break

            if already != "yes":
                You.Stats[10].append([data3[itemNum]['StatusEffect'][i][0],data3[itemNum]['StatusEffect'][i][1]])
                x = "You inflicted yourself with "+data3[itemNum]['StatusEffect'][i][0].upper()+"!"
                E.initialEffect()
            else:
                You.Stats[10][e][1] = data3[itemNum]['StatusEffect'][i][1]
                x = data3[itemNum]['StatusEffect'][i][0].upper()+" has been reapplied."

            print(x.center(80))
    



    def PdetermineStatChange(self,useitem,stat,statNum):
        itemNum = 0
        for i in range(len(data3)):
            if data3[i]['Name'] == useitem:
                itemNum = i

        if data3[itemNum][stat] != 0:
            x = ""
            if data3[itemNum][stat] >= 0:
                x = "Your "+stat+" was increased by "+str(data3[itemNum][stat])+"!"
            else:
                x = "Your "+stat+" was decreased by "+str(abs(data3[itemNum][stat]))+"!"
            
            print(x)

        if stat == "Stamina":
            E.PStamina += data3[itemNum][stat]
        elif stat == "Defense":
            E.PDefense += data3[itemNum][stat]
            
        else:
            playerStats[statNum] += data3[itemNum][stat]
        
    def EnemyTurn(self):
        x = Opponent.name+" attacks you!"
        print(x.center(80))

        attack = Opponent.Attack()

        if attack != "MISSED":
            attack -= E.PDefense
            if attack < 1:
                attack = 0


            if E.defend == "no":
                You.TakeDamage(attack)
            else:
                You.TakeDamage(attack/2)

            print()
            print("You".center(80))

            x = str(You.Stats[1])+"/"+str(PlayerMaxHP)+" HP"
            print(x.center(80))

            if not You.Stats[8] < 1:
                x = "+"+str(You.Stats[8])+" ARMOR"
                print(x.center(80))
            else:
                print()

            if EnemyAbilities != "None":
                E.ApplyEffects()
        else:
            print("They MISSED".center(80))

        
        time.sleep(3)
        os.system("cls")

    def ApplyEffects(self):

        for i in range(len(EnemyAbilities)):
            e = 0
            if random.randint(0,100) <= EnemyAbilities[i][1]:
                already = "no"
                for e in range(len(You.Stats[10])):
                    if EnemyAbilities[i][0] in You.Stats[10][e]:
                        already = "yes"
                        break

                if already == "no":
                    You.Stats[10].append([EnemyAbilities[i][0],EnemyAbilities[i][2]])
                    x = "You have been inflicted with "+EnemyAbilities[i][0].upper()+"!"

                    E.initialEffect()
                else:
                    You.Stats[10][e][1] = EnemyAbilities[i][2]
                    x = EnemyAbilities[i][0].upper()+" has been reapplied."
                
                print(x)

    def initialEffect(self):
        for i in range(len(You.Stats[10])):
            e = 0

            for e in range(len(data4)):
                if data4[e]['Name'] == You.Stats[10][i][0]:
                    break
            
            if data4[e]['Health'][0] != 0:
                You.Stats[1] += data4[e]['Health'][0]
                x = ""
                if data4[e]['Health'][0] < 0:
                    x = str(data4[e]['Health'][0])+" initial HP ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Health'][0])+" initial HP ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))
            
            if data4[e]['Attack'][0] != 0:
                You.Stats[0] += data4[e]['Attack'][0]
                x = ""
                if data4[e]['Attack'][0] < 0:
                    x = str(data4[e]['Attack'][0])+" initial ATK ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Attack'][0])+" initial ATK ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))
            
            if data4[e]['Defense'][0] != 0:
                E.PDefense += data4[e]['Defense'][0]
                x = ""
                if data4[e]['Defense'][0] < 0:
                    x = str(data4[e]['Defense'][0])+" initial DEF ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Defense'][0])+" initial DEF ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))

            if data4[e]['Stamina'][0] != 0:
                E.PStamina += data4[e]['Stamina'][0]
                x = ""
                if data4[e]['Stamina'][0] < 0:
                    x = str(data4[e]['Stamina'][0])+" initial stamina ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Stamina'][0])+" initial stamina ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))

            if data4[e]['Accuracy'][0] != 0:
                E.PAccuracy += data4[e]['Accuracy'][0]
                x = ""
                if data4[e]['Accuracy'][0] < 0:
                    x = str(data4[e]['Accuracy'][0])+" initial ACC ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Accuracy'][0])+" initial ACC ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))

    def Effects(self):
        if EnemyAbilities != "None":
            for i in range(len(You.Stats[10])):
                e = 0
                for e in range(len(data4)-1):
                    if data4[e]['Name'] == You.Stats[10][i][0]:
                        break
                    
                if data4[e]['Health'][1] != 0:
                    You.Stats[1] += data4[e]['Health'][1]
                    You.Stats[10][i][1] -= 1
                    x = ""
                    if data4[e]['Health'][1] < 0:
                        x = str(data4[e]['Health'][1])+" HP ["+You.Stats[10][i][0].upper()+"]"
                    else:
                        x = "+"+str(data4[e]['Health'][1])+" HP ["+You.Stats[10][i][0].upper()+"]"
                    print(x.center(80))

                if data4[e]['Attack'][1] != 0:
                    You.Stats[1] += data4[e]['Attack'][1]
                    You.Stats[10][i][1] -= 1
                    x = ""
                    if data4[e]['Attack'][1] < 0:
                        x = str(data4[e]['Attack'][1])+" ATK ["+You.Stats[10][i][0].upper()+"]"
                    else:
                        x = "+"+str(data4[e]['Attack'][1])+" ATK ["+You.Stats[10][i][0].upper()+"]"
                    print(x.center(80))
                
                if data4[e]['Defense'][1] != 0:
                    E.PDefense += data4[e]['Defense'][1]
                    x = ""
                    if data4[e]['Defense'][1] < 0:
                        x = str(data4[e]['Defense'][1])+" initial DEF ["+You.Stats[10][i][0].upper()+"]"
                    else:
                        x = "+"+str(data4[e]['Defense'][1])+" initial DEF ["+You.Stats[10][i][0].upper()+"]"
                    print(x.center(80))

                if data4[e]['Stamina'][1] != 0:
                    E.PStamina += data4[e]['Stamina'][1]
                    x = ""
                    if data4[e]['Stamina'][1] < 0:
                        x = str(data4[e]['Stamina'][1])+" initial stamina ["+You.Stats[10][i][0].upper()+"]"
                    else:
                        x = "+"+str(data4[e]['Stamina'][1])+" initial stamina ["+You.Stats[10][i][0].upper()+"]"
                    print(x.center(80))

                if data4[e]['Accuracy'][1] != 0:
                    E.PAccuracy += data4[e]['Accuracy'][1]
                    x = ""
                    if data4[e]['Accuracy'][1] < 0:
                        x = str(data4[e]['Accuracy'][1])+" initial ACC ["+You.Stats[10][i][0].upper()+"]"
                    else:
                        x = "+"+str(data4[e]['Accuracy'][1])+" initial ACC ["+You.Stats[10][i][0].upper()+"]"
                    print(x.center(80))
                    if You.Stats[10][i][1] < 1:
                        You.Stats[10].remove(You.Stats[10][i])

            time.sleep(3)



        





        
dungeonNum = 3
enemyNum = 4


enemyInfo(dungeonNum,enemyNum)
playerStats = playerInfo(0)
items = ConsumableItems()

PlayerMaxHP = 100 + playerStats[5]*10
PMaxStamina = 10 + playerStats[4]*5
PDefense = playerStats[4]
PAccuracy = 100
SaveID = 0

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],enemy[6],"None")
You = Player.Player(SaveID,playerStats)

EnemyAbilities = EnemySpecialAbilities(Opponent.name)

Opponent.Encounter(data[dungeonNum]['LevelReq'],You.Stats[4])
E = Battle("no", PMaxStamina, PDefense, PAccuracy, [])


while Opponent.hp > 0:
    E.defend = "no"
    if random.randint(1,2) == 1:
        E.PlayerTurn()
        if Opponent.hp < 1:
            break
        E.EnemyTurn()
    else:
        E.EnemyTurn()
        E.PlayerTurn()

    E.Effects()

os.system("cls")
print("You win!")
time.sleep(3)
os.system("cls")
print("You gained "+str(Opponent.exp)+" EXP!")

for i in range(len(E.UsedItems)):
        data2[SaveID]['Inventory'].remove(E.UsedItems[i])

data2[SaveID]['Armor']['Name'] = You.Stats[7]
data2[SaveID]['Armor']['Durability'] = You.Stats[8]

with open('Saves.json', mode='w') as outfile:
    json.dump(data2, outfile, indent=4)

exit()
