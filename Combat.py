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

def ConsumableItems(SaveID):
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
        print("What do you do?".center(80))
        print("           ╔═══════════════════════╗          ".center(80))
        x = str(You.Stats[1])+"/"+str(PlayerMaxHP)+" HP ║ 1[FIGHT]    2[CHECK]  ║  "+str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
        print(x.center(80))
        print("   You     ║ 3[ITEMS]    4[DEFEND] ║   Enemy  ".center(80))        
        print("           ╚═══════════════════════╝          ".center(80))
        print("[1][2][3][4]")
        Action = int(input())

        if Action == 1:
            Opponent.TakeDamage(playerStats[2])
            os.system("cls")
            print()
            print("           ╔═══════════════════════╗          ".center(80))
            x = str(You.Stats[1])+"/"+str(PlayerMaxHP)+" HP ║<1[FIGHT]>             ║  "+str(Opponent.hp)+"/"+str(Opponent.maxhp)+" HP"
            print(x.center(80))
            print("   You     ║                       ║   Enemy  ".center(80))        
            print("           ╚═══════════════════════╝          ".center(80))
            print(Opponent.name+" took "+str(playerStats[2])+" damage.")
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
                    E.PdetermineStatChange(itemNum,'HP')


                except:
                    useitem = 0
            time.sleep(3)

    def PdetermineStatChange(self,itemNum,stat):
        if data3[itemNum][stat] != 0:
            if data3[itemNum][stat] > 0:
                print("Your "+stat+" increased by "+str(data3[itemNum][stat])+"!")
            else:
                print("Your "+stat+" decreased by "+str(abs(data3[itemNum][stat]))+"!")
    
    def PstatChange(self):
        You.Stats[1]




        



enemyInfo(0,0)
playerInfo(0)
items = ConsumableItems(0)

PlayerMaxHP = playerStats[1]

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5])
You = Player.Player(0,playerStats)

Opponent.Encounter()
E = Battle()

while Opponent.hp > 0:
    E.PlayerTurn()
    if Opponent.hp < 1:
            os.system("cls")
            print("You win!")
            time.sleep(3)
            os.system("cls")
            print("You gained "+str(Opponent.exp)+" EXP!")
            exit()
