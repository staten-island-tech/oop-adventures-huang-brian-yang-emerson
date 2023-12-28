import Game, Effects, Enemy, Player, os, win11toast

def Main():
    while True:
        win11toast.toast("Whoppper")
    PreGame = Game.PreGame()

    # << PreGame Should Return The Data >> #
    SaveID, SaveData = PreGame.MainMenu()

    # << Register The Player >> #
    player = Player.Player(SaveID, SaveData)

    # << Start The Game >> # 
    PostMainMenu = Game.PostMenu(SaveID, SaveData)

    PostMainMenu.TavernStart()

if __name__ == "__main__":
    Main()
