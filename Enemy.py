import random

class Enemy:
    def __init__(self, name, hp, attack, exp, chance) -> None:
        self.name = name
        self.hp = hp
        self.attack = attack
        self.exp = exp
        self.chance = chance
        self.CurrentEffects = {
            'Poison': {
                'Strength': 1,
                'Rounds': 10,
            }
        }
    
    def attack(self):
        return random.randint(self.attack * 0.9 , self.attack * 1.1)
