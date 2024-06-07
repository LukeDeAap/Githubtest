import random
import string
char_amount = int(input("How many characters do u want ur password to be: "))

letters = string.ascii_letters
numbers = string.digits
spec_char = string.punctuation
list = [*letters, *numbers]
list2 = [*letters, *numbers, *spec_char]

x = 0
password = ""

while x < char_amount:
    x +=1
    if x == 1:
        password += random.choice(list)
    else:
        password += random.choice(list2)

print("Your password is:",password)    
