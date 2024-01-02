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
                break
    return items

def EnemySpecialAbilities(name):
    if name == "Cursed Mummy":
        EnemyAbilities = [["Poisoned",25,3],["Burned",25,3]]
    elif name == "Eyed Coffin":
        EnemyAbilities = [["Poisoned",75,3],["Burned",75,3]]
    else:
        EnemyAbilities = "None"

    return EnemyAbilities




class Battle:
    def __init__(self, defend):
        self.defend = defend
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
            print(str(PStamina).center(80))
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
            if not PStamina < 5:
                attack = You.Attack()
                Opponent.TakeDamage(attack)
                os.system("cls")
                print(Opponent.name.center(80))
                x = str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
                print(x.center(80))
                print()
                x = Opponent.name+" took "+str(attack)+" damage."
                print(x.center(80))
                PStamina -= 5
                time.sleep(2)
            else:
                print("You don't have enough stamina!")

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
                    E.PdetermineStatChange(useitem,'HP',1)
                    E.PdetermineStatChange(useitem,'Attack',2)
                    E.PdetermineStatChange(useitem,'Defense',5)
        
                    
                    time.sleep(3)

                except:
                    useitem = 0
                    os.system("cls")
            
        else:
            os.system("cls")
            print("You braced yourself...")
            E.defend = "yes"
            time.sleep(3)

        os.system("cls")

            

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

        playerStats[statNum] += data3[itemNum][stat]
        
    def EnemyTurn(self):
        x = Opponent.name+" attacks you!"
        print(x.center(80))

        attack = Opponent.Attack()

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
        
        time.sleep(3)

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
                    x = "You have been "+EnemyAbilities[i][0].upper()+"!"

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
            
            if data4[e]['Health'][1] != 0:
                You.Stats[1] += data4[e]['Health'][1]
                x = ""
                if data4[e]['Health'][1] < 0:
                    x = str(data4[e]['Health'][1])+" initial HP ["+You.Stats[10][i][0].upper()+"]"
                else:
                    x = "+"+str(data4[e]['Health'][1])+" initial HP ["+You.Stats[10][i][0].upper()+"]"
                print(x.center(80))

    def Effects(self):
        for i in range(len(You.Stats[10])-1):
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

            if You.Stats[10][i][1] < 1:
                You.Stats[10].remove(You.Stats[10][i])
        
        time.sleep(3)



        





        
dungeonNum = 1
enemyNum = 2


enemyInfo(dungeonNum,enemyNum)
playerStats = playerInfo(0)
items = ConsumableItems()

PlayerMaxHP = 100 + playerStats[5]*10
PStamina = 100

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],"None")
You = Player.Player(0,playerStats)

EnemyAbilities = EnemySpecialAbilities(Opponent.name)

Opponent.Encounter(data[dungeonNum]['LevelReq'],You.Stats[4])
E = Battle("no")


while Opponent.hp > 0:
    E.defend = "no"
    E.PlayerTurn()
    if Opponent.hp < 1:
            os.system("cls")
            print("You win!")
            time.sleep(3)
            os.system("cls")
            print("You gained "+str(Opponent.exp)+" EXP!")
            exit()
    E.EnemyTurn()
    if EnemyAbilities != "None":
        E.Effects()
