import subprocess
import time
import os

def dfu_helper():
    dfusec = 8
    global predfu
    predfu = input("Press Enter To Begin DFU Entrence")
    for i in range(8):
        print("Press Vol-Up + Power For " + str(dfusec) + " Secounds")
        dfusec -= 1
        time.sleep(0.2)
        print("Now Only Hold Power For " + str(dfusec) + " Secounds")




def ios_downgrade_OSS():
                    #https://ios.cfw.guide/turdusmerula-tethered/#
    ######################## Path Config Start ########################################
    global merulaloader,merdularunner,merulasetup,userdevicetype                                    #-----------------------------------------------#
    merulaloader = "/.nofollow/Applications/Utilities/turdus_m3rula/bin/turdus_merula"              #BEFORE STARTING THE SCRIPT FILL THESE OUT FIRST#
    merdularunner = "/.nofollow/Applications/Utilities/turdus_m3rula/bin/turdusra1n"                #-----------------------------------------------#
    userdevicetype = "A9" #A9 Or A10 iDevices Are Supported
    iBootFile = "A2"
    pteblockimg = "A2 "
    ipswimg = " "
    signedsep = " "
    targetsep = " "
    ######################## Path CONFIG END ##########################################

    def tuscroe(): #Scoreboard For Some Reason IDK :3 <3 >(
        global restorefails,restoresucess
        restorefails = 0
        restoresucess = 0

    def preexecutionsetup():
        print("")

    def preflightA9():#Setup Script For A9 iDevices
        subprocess.run([merulaloader, "--get-shcblock ipswimg"])


    def preflightA10():#Setup Script For A10 iDevices
        subprocess.run([merulaloader,"-o ipsw"])

    def postflightA9():#Post Setup iOS Loader For A9 iDevices
        subprocess.run([merdularunner,"-TP pteblockimg"])

    def postflightA10():#Post Setup iOS Loader For A10 iDevices
        subprocess.run([merdularunner,"-t iBootFile","-i signedsep","-p targetsep"])

    def MobileAirportCheckin():#Main FrontEnd When Script Is Launched <3
        os.system('clear')
        print("----------------------------------------------")
        print("      iDevice Operations For " + str(userdevicetype))
        print("                                              ")
        print("    [1]  Downgrade iDevice                    ")
        print("    [2]  Boot Exploited iDevice               ")
        print("                                              ")
        print("----------------------------------------------")

        userchoice = int(input("Choose a menu option -> "))
        if userchoice == 1:
            if userdevicetype == "A9":
                print("Downgrading A9 Please Wait...")
                preflightA9()

            elif userdevicetype == "A10":
                print("Downgrading A10 Please Wait...")
                preflightA10()

        
        if userchoice == 2:
            if userdevicetype == "A9":
                print("Booting iDevice A9 Please Wait...")
                postflightA9()

            elif userdevicetype == "A10":
                print("Booting iDevice A10 Please Wait...")
                postflightA10()

            

    MobileAirportCheckin()

dfu_helper()
ios_downgrade_OSS()
