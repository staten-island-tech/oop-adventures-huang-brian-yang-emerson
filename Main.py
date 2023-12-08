import Game, Effects, Enemy, Player

def Main():
    PreGame = Game.PreGame()

    # << PreGame Should Return The Data >> #
    SaveID, SaveData = PreGame.MainMenu()

    # << Register The Player >> #
    player = Player.Player(SaveID, SaveData)

    #

    # << 

if __name__ == "__main__":
    Main()
