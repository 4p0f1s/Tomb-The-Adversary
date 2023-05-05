import socket,sys
from modules.banner import *
from modules.options import *
from modules.game import *
from modules.inter import *



##### Variables
playername = pn()
Turn = True
fin = False
ipadv = 0
#####

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

try:

    wel()

    ready()
    ip = gen()
    ipadv = sock.recv(16)

    sock.sendall(bytes(str(ip),"UTF-8"))

    #################

    while fin != True:

        while Turn != False:
            iprec = interf(ip,playername)
            fin = comp(int(ipadv),iprec)
            if fin == True:
                sock.sendall(b"Lost")
                sock.close()
                exit()
            else:
                sock.sendall(b"Your Turn!")
            Turn = False

        data = sock.recv(16)
        if data != b"Your Turn!":
            sock.close()
            cl()
            print("You lost!!")
            exit()
        else:
            print("Your Turn!")
            Turn = True



####################################################################################################


finally:
    sock.close()
