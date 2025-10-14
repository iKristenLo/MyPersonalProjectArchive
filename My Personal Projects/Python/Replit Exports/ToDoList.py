print("ToDo List")
name = input("Enter Your Name ")
print("Hello", name)

todos = ["HW", "Sleep"]

while True:
  option = input("\nEnter a to add or V to view ")

  if option == 'a' or option == 'A':
    print("You Picked Add")
    add = input("Add To My Todo List: ")
    todos.append(add)
    
    
  elif option == 'V' or option == 'v':
    print("You Picked View\n")
    print("Your Todos :")
    print(todos)

  else:
    break



print("Exiting")