import time

def whopper(Text, Time):
    print("Dealer: ", end='')
    for char in Text:
        print(char, end='', flush=True)
        time.sleep(0.05)


class BuckShot:
    def __init__(self, SaveID, SaveData) -> None:
        self.SaveID = SaveID
        self.SaveData = SaveData
        self.PlayerData = {"HP": 2, "Items": []}
        self.DealerData = {"HP": 2, "Items": []}
    
    def PlayerTurn(self):
        pass
    
    def DealerTurn(self):
        pass

    def RoundOne(self):
        pass

    def RoundTwo(self):
        pass

    def DeathRound(self):
        pass

    def StartGame(self):
        whopper('Please Sign The Wavier.')
        Name = input("Input Name: ")
        
