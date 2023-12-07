from Game import Game, time

def Main():
    StartGame = Game()
    StartGame.MainMenu()
    SaveID, SaveData = StartGame.PlayGame()
    print(SaveID, SaveData)

if __name__ == "__main__":
    Main()
