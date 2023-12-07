from Game import Game, time

def Main():
    StartGame = Game()
    StartGame.MainMenu()
    SaveID, SaveData = StartGame.PlayGame()

if __name__ == "__main__":
    Main()
