import time,os
from modules.banner import *

def interf(ip,name):
    cl()
    print("""
#######################################################################################
#                                                        #                            #
#                                                        #     IP: 192.168.0.%s      #
#                                                        #                            #
#                                                        ##############################
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
root@%s:/DOS# ./conn_destroyer.sh
Loading...|
""" %(ip,name))
    time.sleep(1)
    cl()
    print("""
#######################################################################################
#                                                        #                            #
#                                                        #     IP: 192.168.0.%s      #
#                                                        #                            #
#                                                        ##############################
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
#                                                                                     #
root@%s:/DOS# ./conn_destroyer.sh
Plugins loaded!
Exploit ready to work!!""" %(ip,name))

    prompt = input("Enter the IP to tomb in range of (1-254)!!!: ")
    bad = False
    if (len(prompt) > 3) or (int(prompt) < 1) or (int(prompt) > 254):
        bad = True
    while bad != False:
        prompt = input("Enter a valid number in range of (1-254)!!!: ")
        if (len(prompt) < 4) and (int(prompt) > 0) and (int(prompt) < 255):
            bad = False
    return int(prompt)
