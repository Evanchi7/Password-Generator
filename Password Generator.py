import random

digits = int(input("How many digits do you want your password to include?: "))

characters = "abcdefghijklmnopqrstuvwxyz1234567890"

password = " "
for c in range(digits):
    password += random.choice(characters)
print(password)



