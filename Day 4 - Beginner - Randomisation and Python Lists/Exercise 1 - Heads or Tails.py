# import random
# import my_module

# random_integer = random.randint(1,10)
# print(random_integer)

# print(my_module.pi)

# random_float = random.random()  #0.00000000 - 0.99999999...
# print(random_float)             #0.00000000 - 0.99999999...
# print(random_float * 5)         #0.00000000 - 4.99999999...

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
result = random.randint(0,1)

if result == 1:
    print("Heads")
else:
    print("Tails")