my_str = input("Enter a string: ")
my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str):
  print("Its a palindrom")
  else:
    print("Its not a palindrome")
