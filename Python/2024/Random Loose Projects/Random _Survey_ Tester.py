print("Hello")
namebank = []
namer = input("Whats Your Name: ")
agebank = []
namebank.append(namer)
#print("Hello", namer) #***DEBUG***#
ager = int(input("Whats Your Age: "))
agebank.append(ager)
#print("Oh Nice Your:",ager, "Years Old") #***DEBUG***#
brithdayl = []
birthday = input("Whats Was Your Birth Date: ")
brithdayl.append(birthday)
#print("***DEBUG***","Your Birth Day Is: ",brithdayl) #***DEBUG***#
birthMonl = []
birthMon = input("What Month Were you born in: ")
birthMonl.append(birthMon)
#print("****DEBUG**","Your Month Of Birth Is Currently: ",birthMonl) #***DEBUG***#
brithYrl = []
birthYr = int(input("What Year Were You Born In: "))
brithYrl.append(birthYr)
#print("***DEBUG***","You Were Bourn Somewhere During: ",brithYrl) #***DEBUG***#
InfoSelectCrc = []
print("Your Name Is", namebank)
print("You Are", agebank , "Years Old")
print("Your Birth Info Is","YY/MM/DD",birthday,birthMonl,brithYrl)
AfterUse0 = input("Is All The Infomation Currently Inputted Above Correct?, Yes? Or No?: ")
InfoSelectCrc.append(AfterUse0)
#print(InfoSelectCrc) TESTPRINT0
word_yah0 = "Yes"
word_nah0 = "No"
wordCrc = []
if word_yah0 in InfoSelectCrc:
    print("Good")
if word_nah0 in InfoSelectCrc:
    infoSec_Edit = input("Are You Sure You Want To Revise Your Selection: ")
    wordCrc.append(infoSec_Edit)
    #print(infoSec_Edit) #TEST#
    if word_yah0 in wordCrc:
        change_bank = [] #Choices Would Be "1","2","3","4","5"
        change_ne = ["1"]
        change_Ae = ["2"]
        change_Bdj = ["3"]
        change_Bdk = ["4"]
        chnage_Bdx = ["5"]
        print("1.","Your Name", namebank)
        print("2.","Your Age", agebank)
        print("3.","Your BirthDay [DD]", brithdayl)
        print("4.","Your BirthMon [MM]", birthMonl)
        print("5.","Your BirthYear [YY]", brithYrl)
        chanage_selection = input("What Would You Like To Change: ")
        change_bank.append(chanage_selection)
        #print(change_bank) #****TEST***#
        #***CHANGER DATA START****#

        def infomodi():
            if change_ne in change_bank:
                print("Holding")
                change_en = input("Enter Your Newly Desired 'Name': ")
                
            if change_Ae in change_bank:
                print("Holding")
                change_ea = input("Enter Your New 'Age': ")

            if change_Bdj in change_bank:
                print("Holding")
                change_jbd = input("Enter Your New Birth 'Date': ")

            if change_Bdk in change_bank:
                print("Holding")
                change_kdb = input("Enter Your New Birth 'Month': ")

            if chnage_Bdx in change_bank:
                print("Holding")
                change_xdb = input("Enter Your New Birth 'Year': ")       
        infomodi()

        