import time, os
from itertools import cycle

def Dialogue(Speaker, sentence, times):

    print(Speaker + ": ", end="", flush=True)
    time.sleep(0.05)

    for char in sentence:
        time.sleep(times)
        print(char, end="", flush=True)

def Answer(Question):
    Confirm = input("Y/N: ").lower()

    while Confirm != "y" and Confirm != "n":
        Confirm = input("Y/N (Only): ").lower()
    
    if Confirm == 'y':
        return True
    else:
        return False
    
def stall(times):
    prostall = cycle(['.', '..', '...'])
  
    e = 0

    while e != times:

        os.system('cls')
        print(prostall, end="", flush=True)
        
        time.sleep(1)
        e += 1