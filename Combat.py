import Enemy,Player,json,os,time


with open("DData.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)

with open("Saves.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data2 = json.load(f)


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
        
        if Opponent.hp < 1:
            os.system("cls")
            print("You win!")
            time.sleep(3)
            os.system("cls")
            print("You gained "+str(Opponent.exp)+" EXP!")
            exit()




enemyInfo(0,0)
playerInfo(0)
PlayerMaxHP = playerStats[1]

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5])
You = Player.Player(0,playerStats)

Opponent.Encounter()
E = Battle()

for i in range(10):
    E.PlayerTurn()

#You.TakeDamage(Opponent.attack)
