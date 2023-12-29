import Enemy,Player,json,os,time


with open("DData.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

with open("Saves.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data2 = json.load(f)

with open("ItemList.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data3 = json.load(f)

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
    playerStats.append([])

def ConsumableItems():
    items = []
    print(playerStats[6])

    for i in range(len(playerStats[6])):
        for e in range(len(data3)):
            if playerStats[6][i] == data3[e]['Name']:
                items.append(playerStats[6][i])
                break
    return items



class Battle:
    def __init__(self) -> None:
        pass
    def PlayerTurn(self):
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
        if not You.Stats[8] < 1:
            x = "+"+str(You.Stats[8])+" ARMOR"
            print(x.center(80))
        else:
            print()

        
        Action = int(input())

        if Action == 1:
            Opponent.TakeDamage(playerStats[2])
            os.system("cls")
            print(Opponent.name.center(80))
            x = str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
            print(x.center(80))
            print()
            x = Opponent.name+" took "+str(playerStats[2])+" damage."
            print(x.center(80))
            time.sleep(2)

        elif Action == 2:
            os.system("cls")
            Opponent.Check()
            Opponent.Desc()

        elif Action == 3:
            useitem = 0        
            while useitem == 0:
                print("INVENTORY")
                for i in range(len(items)):
                    print("item "+str(i+1)+":  "+items[i])
            
                useitem = input("Use item... ")
                try:
                    itemNum = int(useitem)-1
                    useitem = items[itemNum]
                    os.system("cls")                   
                    print("You used "+useitem+".")
                    E.PdetermineStatChange(useitem,'HP',1)
                    E.PdetermineStatChange(useitem,'Attack',2)
                    E.PdetermineStatChange(useitem,'Defense',5)



                except:
                    useitem = 0
                    os.system("cls")
            
            else:
                print("You braced yourself...")



    def PdetermineStatChange(self,useitem,stat,statNum):
        itemNum = 0
        for i in range(len(data3)):
            if data3[i]['Name'] == useitem:
                itemNum = i

        if data3[itemNum][stat] != 0:
            if data3[itemNum][stat] >= 0:
                print("Your "+stat+" was increased by "+str(data3[itemNum][stat])+"!")

        playerStats[statNum] += data3[itemNum][stat]

    def Defend():
        Defend = "yes"
        return Defend
        
    def EnemyTurn(self):
        if Defend == "no":
            You.TakeDamage(Opponent.attack)
        else:
            You.TakeDamage(Opponent.attack/2)
        
        time.sleep(3)


        





        



enemyInfo(0,2)
playerInfo(0)
items = ConsumableItems()

PlayerMaxHP = playerStats[1]

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5],"None")
You = Player.Player(0,playerStats)

Opponent.Encounter()
E = Battle()

while Opponent.hp > 0:
    Defend = "no"
    E.PlayerTurn()
    if Opponent.hp < 1:
            os.system("cls")
            print("You win!")
            time.sleep(3)
            os.system("cls")
            print("You gained "+str(Opponent.exp)+" EXP!")
            exit()
    E.EnemyTurn()
