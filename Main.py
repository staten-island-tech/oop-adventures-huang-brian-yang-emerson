import Game, Effects, Enemy, Player, os, win11toast

def Main():
    win11toast.toast("I hate haobin")

    PreGame = Game.PreGame()

    # << PreGame Should Return The Data >> #
    SaveID, SaveData = PreGame.MainMenu()

    # << Register The Player >> #
    player = Player.Player(SaveID, SaveData)

    # << Start The Game >> # 
    PostMainMenu = Game.PostMenu()

    PostMainMenu.TavernStart()

if __name__ == "__main__":
    Main()
