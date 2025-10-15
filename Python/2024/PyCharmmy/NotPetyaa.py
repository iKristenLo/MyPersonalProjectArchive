import time
import math
import random
import os

global usersektors
usersektors = random.randint(100,83772)

def rankeygen():
    global encryptkey
    encryptkey = random.randint(7382872,281928812)

def fileencrypt():
    global sectornum
    sectornum = 0
    for sectornum in range(1):
        os.system('clear')
        sectornum += 1
        print("Repairing file system on C:")
        print(" ")
        print("The type of the file system is NTFS")
        print("One of your disks contains errors and needs to be repaired. This process")
        print("may take several hours to complete. It is strongly recommended to let it")
        print("complete.")
        print(" ")
        print("WARNING: DO NOT TURN OFF YOUR PC! IF YOU ABORT THIS PROCESS. YOU COULD")
        print("DESTROY ALL OF YOUR DATA! PLEASE ENSURE THAT YOUR POWER CABLE IS PLUGGED")
        print("IN!")
        print(" ")
        print("CHKDSK is repairing sector " + str(sectornum) + " of " + str(usersektors))
        time.sleep(0.1)
        os.system('clear')
        

fileencrypt()

def petani():
    for i in range(10):
        os.system('clear')
        print(
        """
        xxxxxxxxxxxx
        xxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxx
        xxxxxxxxxxxxxxxxxx
        xxx xxx xx xxx
        xx   xxx   xxx
        xx   xxx   xx
        xx   xxxx   xx
        xxxxxxxxxxxxx
        xxxx  xxxx
            xxxxxxxx
            x xxxxxx
            x     xx
            xxxxxx
            xxxx
    xxxx       xx       xxxx
    xxxx              xxxx
    xxxxxx          xxxxxx
    xxxxx xxxxx    xxxxxxxx
    xx    xxxxxx    xx
            xxxx
            xxxxxxx
        xxxx   xxxx
    xxxxxx      xxxxxx
    xxxxxx          xxxxxx
    xxxxxx            xxxxxx
    xxxxx            xxx
        xx              x
    """
        )
    time.sleep(2)
    os.system('clear')

def ranote():
    rankeygen()
    print(encryptkey)
    print("Oh No Your Files Have Been Encrypted By NosPetya!")
    print("You Have 4 Days To Pay The Ransome!")
    vicinput = int(input("Please Enter Your Decryption Key! -> "))
    while vicinput != encryptkey:
        print("Sorry The Key Is Incorrect!")
        vicinput = int(input("Please Enter Your Decryption Page! -> "))

petani()
ranote()

def usrdecrypt():
    sectornum = 0
    for i in range(usersektors):
        os.system('clear')
        sectornum += 2
        print("Decrypting sector " + str(sectornum) + " of " + str(usersektors))
        time.sleep(0.1)
        os.system('clear')

os.system('clear')

usrdecrypt()




