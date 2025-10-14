#For loop challenge

'''
range(num) goes from 0 to the number-1

range(include,exclude) goes from the number included to the number excluded-1
range(100,201)

range(include, exclude, step)
'''

#Lottery number generator
#use import random on line 
#use a = random.randint(0,50) to...
#generate a random integer between 0 and 50
#use a for loop to generate...
#6 random integers 
'''
import random

for i in range(6):
  a = random.randint(1,49)
  print(a)
'''

#Challenge 2
#Create some code that..
#asks a user for an int below 100
#displays a backwards count to zero
'''
response = int(input("Enter A Number Below 100: "))

for i in range(response,-1,-1):
  print(i)
'''

#The code below is mixed up and has an error
#It should display the 7 colours of the rainbow...
#...in order and count them too.
#The colours are in a list
#HINT: You may have to fix indentation too
'''
number = 0 
rainbow =["red","orange","yellow","green","blue","indigo", "violet"]
for i in rainbow:
  number = number + 1
  print ("Colour",number*1,"is", i)
'''

#Monopoly with extras.
#To make the board game monopoly more fun..
#Create a list with amounts of money..
#ranging from 0 to 100000
#use import random and also use...
#list = random.choice(money)
#to randomly choose an amount of money
#use a for loop to assign a...
#random amout of money to 8 players

import random
CASH = []

for i in range(100,100001 , 100): #the amount of money in the list should be multiples of 100
  CASH.append(i) #add i back into the list we created above

for i in range(8):
  list = random.choice(CASH)
  print(list)

#100,200,300,400,500
