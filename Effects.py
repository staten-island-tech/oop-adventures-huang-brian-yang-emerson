class Effects:
    def __init__(self) -> None:
        pass

    def poison(self, EnemyData, Strength):
        pass

    def burn(self, EnemyData, Strength):
        pass


    def Turn(self, RoundData: list[dict]):

        for enemyDict in RoundData:

            for effect in enemyDict['CurrentEffects']:
                if effect == "poison":
                    self.poison(enemyDict, enemyDict['CurrentEffects']['Strength'])

                elif effect == "burn":
                    self.burn(enemyDict, enemyDict['CurrentEffects']['Strength'])
                    


