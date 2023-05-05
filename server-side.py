import socket,sys
from modules.banner import *
from modules.options import *
from modules.game import *
from modules.inter import *

##### Variables
playername = pn()
Turn = False
fin = False
ipadv = 0
#####

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

print('waiting for a connection')
connection, client_address = sock.accept()
try:
    print('Player 2 connection from', client_address)

    wel()

    ready()

    ip = gen()
    connection.sendall(bytes(str(ip),"UTF-8"))
    ipadv = connection.recv(16)

    #################

    while fin != True:

        data = connection.recv(16)
        if data != b"Your Turn!":
            cl()
            print("You lost!!")
            connection.close()
            sock.close()
            exit()

        else:
            print("Your Turn!")
            Turn = True
        while Turn != False:
            iprec = interf(ip,playername)
            fin = comp(int(ipadv),iprec)
            if fin == True:
                connection.sendall(b"Lost")
                connection.close()
                sock.close()
                exit()

            else:
                connection.sendall(b"Your Turn!")
            Turn = False



####################################################################################################



finally:
    connection.close()
