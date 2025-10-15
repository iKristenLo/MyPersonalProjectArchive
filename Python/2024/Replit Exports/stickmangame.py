import random
import os
import time
words = ["hello","coder","school","monday","friday"]
print("Welcome To Hangman")

sword = random.choice(words)

def dash(sword):
  for x in sword:
    print("-",end=" ")
time.sleep(2.5)
os.system('cls'if os.name=='nt' else 'clear')
dash(sword)

def mand(wrong):
  if wrong == 1:
    print("\n ( )")
  elif wrong == 2:
    print("\n  ( )   |")
    print("  \\|/   |")
  elif wrong == 3:
    print("\n  ( )   |")
    print("  \\|/   |")
    print("   |    |")
  elif wrong == 4:
    print("\n  ( )   |")
    print("  \\|/   |")
    print("   |    |")
    print("  / \\   |")
#mand(1)
    
  # print("")
  # print("_________")
  # print("        |")
  # print("  ( )   |")
  # print("  \|/   |")
  # print("   |    |")
  # print("  / \   |")
  # print("________|________")

wrong = 0
cor = 0
while wrong < 4 and cor < len(sword):
  mand(wrong)
  print("Enter A Letter")
  w1 = input()
  
  