import Enemy,Player,json,os,time


with open("DData.json", "r") as f:
    # Serialize the updated Python list to a JSON string
    data = json.load(f)
    ##Call classes in here

enemy = []

def enemyInfo(dungeonNum,enemyNum):
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Name'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Hp'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Attack'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Exp'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Chance'])
    enemy.append(data[dungeonNum]['Enemies'][enemyNum]['Desc'])
    return enemy

class Battle:
    def __init__(self) -> None:
        pass
    def PlayerTurn(self):
        os.system("cls")
        print("What do you do?".center(80))
        print("          ╔═══════════════════════╗          ".center(80))
        print("          ║ 1[FIGHT]    2[CHECK]  ║          ".center(80))
        print("   You    ║ 3[ITEMS]    4[DEFEND] ║   Enemy  ".center(80))        
        print("          ╚═══════════════════════╝          ".center(80))
        print("[1][2][3][4]")
        Action = int(input())

        if Action == 1:
            Opponent.TakeDamage()

enemyInfo(0,0)

os.system("cls")
Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5])

Opponent.Encounter()
E = Battle()
E.PlayerTurn()