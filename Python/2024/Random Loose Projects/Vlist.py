#Hw try completing it


Vlist = []


def func2(n):
  numPutter = int(input("Enter a Number: "))
  Vlist.append(numPutter)
  numPutter2 = int(input("Enter a Secound Number: "))
  Vlist.append(numPutter2)
  numPutter3 = int(input("Enter a Third Number: "))
  Vlist.append(numPutter3)
  
  maxnum=n[numPutter]
  for i in range( numPutter+1, numPutter2+1):
    if n[i] > maxnum:
      maxnum = n[i]

func2()
  