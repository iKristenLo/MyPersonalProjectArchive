import random
import turtle
import time

wb1 = [] #POST+LOGIN BANK
wb2l = ["1.Login","2,SignUp","3,Exit To Desktop"]

#POST
print("Welcome To PassGate v2.4")
POSTQ = input("Press AnyKey To Continue: ")
wb1.append(POSTQ)
print("Enter Your Selection")
print(wb2l)
LOGTQ = input("")
wb1.append(LOGTQ)
print(LOGTQ)
if LOGTQ in wb2l:
    print("Hel")
else:
    print("NO")