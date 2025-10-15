#Hw try completing it


Vlist = []


def func2():
  numPutter = int(input("Enter a Number: "))
  Vlist.append(numPutter)
  numPutter2 = int(input("Enter a Secound Number: "))
  Vlist.append(numPutter2)
  numPutter3 = int(input("Enter a Third Number: "))
  Vlist.append(numPutter3)
  
  
  maxnum=Vlist[0]
  print(maxnum)
  for n in Vlist:
    if n > maxnum:
      maxnum = n
  print(maxnum)
  

func2()
  