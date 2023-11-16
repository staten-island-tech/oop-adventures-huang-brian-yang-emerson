import time

def Dialogue(Speaker, sentence, times):

    print(Speaker + ": ", end="", flush=True)
    time.sleep(0.05)

    for char in sentence:
        time.sleep(times)
        print(char, end="", flush=True)
    