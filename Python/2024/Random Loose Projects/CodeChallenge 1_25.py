'''
Prompt: Create a password generator that takes the user's name, age, and three special characters. 
It should output the combination as a password. 
'''
'''
variables - hold info
variable_int = 1
variable_string="hello"
print(variable_string)
#string - letters, numbers, special characters (hello, hello123, hello123!)
#integers - ONLY numbers

user_input=int(input("Asking for a number"))
user_input=input("Asking for a string")

concatenation - joining two variables together
string + string #for same data type concatenation
string , 1 #for different data type concatenation
string_variable, 1, string_variable2
print(string_variable, 1)
print(string_variable + string_variable1)
'''

question = input("Whats Your Name? ")
print("Hello ",question)
question2 = int(input("Whats Your Age? "))
print("Oh Ok Your", question2 , "Years Old! Nice")
question3 = input("Please Enter A Special Character: ")
question4 = input("Please Enter Another Special Character: ")
question5 = input("Please Enter One Last Special Character: ")
print("The Special Characters You Chosen Are", question3 , question4, question5)
print("Your Special Password You Requested Is ", question,question2,question3,question4,question5,)
