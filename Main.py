import Game, Player, os #, #win11toast

def Main():
    #win11toast.toast("I hate haobin")
    try:
        PreGame = Game.PreGame()
        
    except Exception as e:
        os.system('cls')
        print("How in the world did you manage to bug out the game. That's some real impressive ability there.")
        print("Anyways give this to emerson yang or brian huang for debugging: ")
        print(e)

    # << PreGame Should Return The Data >> #
    try:
        SaveID, SaveData = PreGame.MainMenu()

        # << Register The Player >> # 
        player = Player.Player(SaveID, SaveData)

        # << Start The Game >> # 
        PostMainMenu = Game.PostMenu(SaveID, SaveData, player)

        PostMainMenu.TavernStart()

    except Exception as e:
        os.system("cls")
        print("HOME RUN!!!!!! YOU got A ERROR WOOO HOOO")
        print("NOW LEAVE THE GAME FOREVER")
        print(e)
        os.abort()

if __name__ == "__main__":
    Main()

