import os, time

def EndPrompt(Text,Delay):
    print(f"", end="", flush=True)
    for char in Text:
        print(char, end="", flush=True)
        time.sleep(Delay)
    time.sleep(3)
    os.system("cls")

def RedSquare():
    for i in range(10):
        print("                          ".center(180))
    print("            🟥            ".center(180))
    for i in range(10):
        print("                          ".center(180))

os.system("cls")
time.sleep(3)
EndPrompt("...".center(180),0.1)
EndPrompt("....".center(180),0.1)
EndPrompt("It's...dark...".center(180),0.1)
EndPrompt("It's very dark....".center(180),0.1)
EndPrompt("So...Everything's...gone...".center(180),0.1)
time.sleep(3)
RedSquare()
EndPrompt("...".center(180),0.1)
RedSquare()
EndPrompt("....".center(180),0.1)
RedSquare()
EndPrompt("It's...a red square".center(180),0.1)
RedSquare()
time.sleep(3)
EndPrompt("Will you press it?".center(180),0.1)
Answer = None

while Answer == None:
    RedSquare()
    Answer = str(input("Will you press it? [Y/N]"))
    Answer = Answer.upper()
    if Answer != "Y":
        Answer = None
        
os.system("cls")

EndPrompt("...".center(180),0.1)
EndPrompt("You pressed the red square...".center(180),0.1)
os.abort()