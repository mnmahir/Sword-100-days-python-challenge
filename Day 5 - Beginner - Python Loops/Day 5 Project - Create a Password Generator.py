#Password Generator Project
from operator import ge
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# gen_pass = ""
# for i in range(nr_letters):
#     gen_pass += letters[random.randint(0,len(letters) - 1)]   # gen_pass += random.choice(letters)
# for i in range(nr_numbers):
#     gen_pass += numbers[random.randint(0,len(numbers) - 1)]
# for i in range(nr_symbols):
#     gen_pass += symbols[random.randint(0,len(symbols) - 1)]
# print (gen_pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# gen_pass = ""
# for i in range(nr_letters + nr_numbers + nr_symbols):
#     sel = random.randint(0,2)
#     if nr_letters != 0 and sel == 0:
#         gen_pass += letters[random.randint(0,len(letters) - 1)]
#         nr_letters -= 1
#     if nr_numbers != 0 and sel == 1:
#         gen_pass += numbers[random.randint(0,len(numbers) - 1)]
#         nr_numbers -= 1
#     if nr_symbols != 0 and sel == 2:
#         gen_pass += symbols[random.randint(0,len(symbols) - 1)]
#         nr_symbols -= 1
# print (gen_pass)

#Better method
gen_pass = []
for i in range(nr_letters):
    gen_pass.append(random.choice(letters))
for i in range(nr_numbers):
    gen_pass += random.choice(numbers)          # Same method with append.
for i in range(nr_symbols):
    gen_pass.append(random.choice(symbols))

random.shuffle(gen_pass)

password = ""
for char in gen_pass:
    password += char

print (f"Your password is: {password}")