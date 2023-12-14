import Enemy,Player,json,os


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

enemyInfo(0,0)

Opponent = Enemy.Enemy(enemy[0],enemy[1],enemy[1],enemy[2],enemy[3],enemy[4],enemy[5])

Enemy.Encounter()