
def pn():
    playername = input("Input your player name: ")
    return playername

def ready():
    rd = False
    ready = input("Ready to play? (Y/N): ").upper()
    if ready == "Y":
        rd = True

    while rd != True:
        if (ready == "Y"):
            print("Start to play")
            rd = True
        elif (ready == "N"):
            print("Dont ready to play")
            ready = input("Ready to play? (Y/N): ").upper()
        else:
            print("Your option is not valid.")
            ready = input("Input a valid option (Y/N): ").upper()
