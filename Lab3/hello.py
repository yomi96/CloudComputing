#this code shows if a word entered by user is a palindrome
my_str = input("Enter a string: ").upper()


my_str = my_str.casefold()
rev_str = reversed(my_str)
if list(my_str) == list(rev_str): #if word is equal to word backwards
  print("Its a palindrom") #print this if its palindrome
else:
  print("Its not a palindrome")
