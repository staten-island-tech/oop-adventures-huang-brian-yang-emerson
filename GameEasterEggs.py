import time, random

def whopper(Text, Time):
    print("Dealer: ", end='')
    for char in Text:
        print(char, end='', flush=True)
        time.sleep(0.05)


class BuckShot:
    def __init__(self, SaveID, SaveData) -> None:
        self.SaveID = SaveID
        self.SaveData = SaveData
        self.Shells = []
        self.PlayerData = {"HP": 2, "Items": []}
        self.DealerData = {"HP": 2, "Items": []}
    
    def PlayerTurn(self):
        pass
    
    def DealerTurn(self):
        pass

    def RoundOne(self):
        whopper("Round 1. 2 Blanks 1 Live.")
        whopper("The shells go into the chamber in a unknown order")
        self.PlayerTurn()

    def RoundTwo(self):
        pass

    def DeathRound(self):
        pass

    def StartGame(self):
        whopper('Please Sign The Wavier.')
        Name = input("Input Name: ")

        
