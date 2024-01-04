import os, time

def Answer(Options: list):
    Confirmaton = input(f"{'/'.join(Options)}: ").upper()

    while Confirmaton not in Options:
        Confirmaton = input(f"{'/'.join(Options)}: ").upper()
    
    return Options.index(Confirmaton)

def CoolBoxDialogue(ListOfDialogue: list[str], AvailableActions: list[str], ActionOAnswer, MaxLength):
    print("╔" + "═"*(MaxLength-1) + "╗")

    for dialogue in ListOfDialogue:
        NeededLine = (MaxLength - len(dialogue) - 1) * " " + "║"
        print(f"║{dialogue}" + NeededLine)

    print(f"║" + " "*(MaxLength-1) + "║")
    print("║Available Actions:" + " "*(MaxLength - 19) + "║")

    for Action in AvailableActions:
        print(f"║{Action}" + " "*(MaxLength - len(Action) - 1) + "║" )

    print(f"║" + " "*(MaxLength-1) + "║")
    print(f"╚" + "═"*(MaxLength-1) + "╝")

    return Answer(ActionOAnswer)

List = [
    {
        'Name': "yes"
    },
    {
        "Name": "yes"
    }
]


current = 1

yes = [f"Save {i}: {save['Name']}" + (' <--' if i == current else '') for i, save in enumerate(List)]


dict = {'self': 'yes', 'no': 'l', 'sss': 'ssss'}


Map  = [["#" for i in range(5)] for i in range(5)]

Map[2][2] = "P"


def py(x):
    print(x)

try:
    py()
except:
    print("there was something wrong with the program")

# << What in the world does Enum Do again???? >> #
from enum import Enum

class enumtester(Enum):
    e = 1
    f = 3

# Define the map size
map_size = 10

# Define the player, goals, empty space, trees, and paths with ASCII characters
player = "P"
goal_1 = "X"
goal_2 = "Y"
empty_space = " "
tree = "🌲"
path = "·"

# Initialize the game map with trees as boundaries
game_map = [[tree if i == 0 or i == map_size - 1 or j == 0 or j == map_size - 1 else empty_space for j in range(map_size)] for i in range(map_size)]

# Set the goals
goals = [(1, 3), (7, 7)]

# Set the player's start position
player_start = [5, 5]

# Place the player and goals on the map
game_map[player_start[0]][player_start[1]] = player
game_map[goals[0][0]][goals[0][1]] = goal_1
game_map[goals[1][0]][goals[1][1]] = goal_2

# Add a path from the player to each goal
for i in range(min(player_start[0], goals[0][0]), max(player_start[0], goals[0][0]) + 1):
    game_map[i][player_start[1]] = path
for j in range(min(player_start[1], goals[0][1]), max(player_start[1], goals[0][1]) + 1):
    game_map[goals[0][0]][j] = path

for i in range(min(player_start[0], goals[1][0]), max(player_start[0], goals[1][0]) + 1):
    game_map[i][player_start[1]] = path
for j in range(min(player_start[1], goals[1][1]), max(player_start[1], goals[1][1]) + 1):
    game_map[goals[1][0]][j] = path

# Print the game map
for row in game_map:
    print(' '.join(row))
