namebank = []
namer = input("What's Your Name: ")
agebank = []
namebank.append(namer)

ager = int(input("What's Your Age: "))
agebank.append(ager)

brithdayl = []
birthday = input("What Was Your Birth Date: ")
brithdayl.append(birthday)

birthMonl = []
birthMon = input("What Month Were You Born In: ")
birthMonl.append(birthMon)

brithYrl = []
birthYr = int(input("What Year Were You Born In: "))
brithYrl.append(birthYr)

print("Your Name Is", namebank)
print("You Are", agebank[0], "Years Old")
print("Your Birth Info Is", "YY/MM/DD", brithdayl[0], birthMonl[0], brithYrl[0])

InfoSelectCrc = []
AfterUse0 = input("Is All The Information Currently Inputted Above Correct? Yes or No: ")
InfoSelectCrc.append(AfterUse0)

word_yah0 = "Yes"
word_nah0 = "No"
wordCrc = []

if word_nah0 in InfoSelectCrc:
    infoSec_Edit = input("Are You Sure You Want To Revise Your Selection: ")
    wordCrc.append(infoSec_Edit)

    if word_yah0 in wordCrc:
        change_bank = []
        change_ne = "1"
        change_Ae = "2"
        change_Bdj = "3"
        change_Bdk = "4"
        change_Bdx = "5"
        print("1. Your Name:", namebank[0])
        print("2. Your Age:", agebank[0])
        print("3. Your Birthday [DD]:", brithdayl[0])
        print("4. Your Birth Month [MM]:", birthMonl[0])
        print("5. Your Birth Year [YY]:", brithYrl[0])
        change_selection = input("What Would You Like To Change: ")
        change_bank.append(change_selection)

        def changer():
            if change_ne in change_bank:
                new_name = input("Enter Your Newly Desired Name: ")
                namebank[0] = new_name
            if change_Ae in change_bank:
                new_age = int(input("Enter Your New Age: "))
                agebank[0] = new_age
            if change_Bdj in change_bank:
                new_birthday = input("Enter Your New Birth Date: ")
                brithdayl[0] = new_birthday
            if change_Bdk in change_bank:
                new_birth_month = input("Enter Your New Birth Month: ")
                birthMonl[0] = new_birth_month
            if change_Bdx in change_bank:
                new_birth_year = int(input("Enter Your New Birth Year: "))
                brithYrl[0] = new_birth_year

        changer()

print("Your Updated Information:")
print("Name:", namebank[0])
print("Age:", agebank[0])
print("Birthday:", brithdayl[0])
print("Birth Month:", birthMonl[0])
print("Birth Year:", brithYrl[0])