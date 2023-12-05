from Game import Game, time

def Main():
    StartGame = Game()
    StartGame.MainMenu()
    SaveID = StartGame.PlayGame()


if __name__ == "__main__":
    Main()
