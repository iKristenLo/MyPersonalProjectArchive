'''
Create a code that uses a  while loop to ask the user to to add items to a list. 
As soon as the user stops adding items, 
the list is finished and the amount of ITEMS in the list is printed. 
'''

theItemList = [] #empty list
falseitem = "No"

def yest():
  while True:
    itmadder = input("Enter Anything: ")
    if falseitem in itmadder:
      print(theItemList) #''& break' OR 'and break'
      break
    #else:
    theItemList.append(itmadder) 
    

yest()
print(len(theItemList))
 
  
  