class Combat:
    def __init__(self,enemyName, enemyHP, enemyStatuses):
        self.enemyName = enemyName
        self.enemyHP = enemyHP
        self.enemyStatuses = enemyStatuses
    def PlayerAttack(self):
        print("You dealt")