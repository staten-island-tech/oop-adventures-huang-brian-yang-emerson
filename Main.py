from Game import Game, time

def Main():
    StartGame = Game()
    StartGame.MainMenu()

if __name__ == "__main__":
    for i in range(10):
        for i in range(10):
            time.sleep(0.025)
            print("#", end="")
        print(end="\n")