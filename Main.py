from Game import Game, time

def Main():
    StartGame = Game()
    StartGame.MainMenu()
    SaveID, SaveData = StartGame.PlayGame()
    print(f"Debug Menu: Loaded Save {SaveID}\n{SaveData}")

if __name__ == "__main__":
    Main()
