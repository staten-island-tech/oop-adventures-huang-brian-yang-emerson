import time

def Dialogue(Speaker, sentence):

    print(Speaker + ": ", end="", flush=True)
    time.sleep(0.5)

    for char in sentence:
        time.sleep(0.05)
        print(char, end="", flush=True)