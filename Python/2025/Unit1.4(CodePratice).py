#1
# def display_name():
#     name = "Jordan"
#     print("hello",name)
# display_name()
# print(name)

#2
# global message
# message = "Outside Function"
# def show_message():
#     message = "Inside Function"
#     print(message)
# show_message()
# print(message)

#3
# def add_numbers():
#     total = 10 + 5
#     print(total)
# add_numbers()
# print(total)

#4
# global school
# school = "Molloy"
# def use_gloabal():
#     print(school)
# use_gloabal()

#5
# counter = 0
# def update_counter():
#     global counter
#     counter = counter + 1
#     print(counter)
# update_counter()
# update_counter()
# update_counter()

#6
# def temporary_value():
#     x = 99
#     print(x)
# temporary_value()
# print(x)

#7
# def square(n=0):
#     print(n * n)
# square(4)

#8
# It Prints Inside: 5
# It Prints Outside: 10

#9
# def multiply_numbers(x,y):
#     p = x*y
#     print(p)
# multiply_numbers(7,9)

#10
# def greet_user(x="Guest"):
#     print("Welcome",x)
# greet_user()
# greet_user("Maria")

#11
# def rectangle_math(length=0,width=0,calc_type="area"):
#     if calc_type == "area":
#         k = length*width
#         print(k)
#         return k
#     elif calc_type == "perimeter":
#         p = (length + width)*2
#         print(p)
#         return p
# rectangle_math(10,5)
# rectangle_math(10,5,"perimeter")

#12
# def is_even(x=0):
#     if x % 2 == 0:
#         print(True)
#     else:
#         print(False)
# is_even(14)
# is_even(9)

#13
# def average_two(x,y):
#     a = x+y
#     p = a/2
#     print(p)
# average_two(6,8)

#14
# def square(n):
#     k = n*n
#     return k
# def add_five(x):
#     k = x+5
#     return k
# print(add_five(square(4)))
#
#

#15
def max_of_two():
