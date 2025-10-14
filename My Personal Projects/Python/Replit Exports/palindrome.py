def check_palindrome(string):
  print(string)
  l = list(string)
  print(l)

  l.reverse()
  print(l)
  rev_string = ''.join(l)
  print(rev_string)
  if string == rev_string:
    return True
  else:
    return False
  
print(check_palindrome("racecar"))

