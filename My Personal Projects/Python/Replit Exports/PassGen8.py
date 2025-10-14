import random, string

def generate_pw(length, special_chars):
  letters = string.ascii_letters
  digits = string.digits
  all_chars = special_chars + letters + digits
  password = random.choice(special_chars)
  for i in range(length -1):
    password+= random.choice(all_chars)
  password = ''.join(random.sample(password,  len(password)))
  return password
if __name__ == "__main__":
  while True:
    response = input("Enter the length of the password or exit if you want to quit :")
    if response.lower()== 'exit':
      break
    else:
      response = int(response)
    special_chars = input("Enter the special characters they want to include (e.x., !@$^()): ")
    if response < 8:
      print("The Password is to short it must be at least 8 characters. ")
    else:
      password = generate_pw(response,   special_chars)
      print(f"Generated Password: {password}")