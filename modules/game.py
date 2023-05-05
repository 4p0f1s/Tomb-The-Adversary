import random

def gen():
    print("Generating IP...")
    ip = random.randint(1, 254)
    keep = False
    regen = input("This is your Ip: 192.168.0.%s\nWant to keep or generate a new one? (K/N): " %(ip)).upper()

    if regen == "K":
        keep = True

    while keep != True:
        if regen == "K":
            keep = True
        elif regen == "N":
            ip = random.randint(1, 254)
            regen = input("This is your New Ip: 192.168.0.%s\nWant to keep or generate a new one? (K/N): " %(ip)).upper()
        else:
            print("Your option is not valid.")
            regen = input("Input a valid option (K/N): ").upper()

    return ip


def comp(ipadv,iprec):
    if iprec == ipadv:
        print("DOSing the IP!!!\nTarget IP correct!!\n")
        return True
    else:
        print("DOSing the IP!!!\nHost unrechable!")
        return False
