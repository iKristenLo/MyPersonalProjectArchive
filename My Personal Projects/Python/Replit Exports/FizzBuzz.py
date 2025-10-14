#FIZZBUZZ
# For all values of a number we want to print "FizzBuzz" if its divisble by 15
#Print Fizz if it is divisble by only 3
#Print Buzz if it is divisble by only 5
while True:
  input_res = int(input("Enter a number or exit if you want to quit: "))
  if input_res.lower() == 'exit':
    break
  else:
    input_res = int(input_res+1)
  for i in range(input_res+1):
    if i % 15 == 0:
      print("FizzBuzz")
    elif i%5 == 0:
      print("Buzz")
    elif i%3 == 0:
      print("Fizz")
    elif i%2 == 0:
      print("This i is even!"+ str(i))
    else:
      print("This i is odd"+ str(i))
  