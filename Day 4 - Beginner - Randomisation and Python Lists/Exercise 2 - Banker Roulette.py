# states_of_malaysia = ["Kuala Lumpur", "Selangor", "Penang"]

# print(states_of_malaysia[0])    # First in list
# print(states_of_malaysia[-1])   # Last in list

# states_of_malaysia[0] = "Kedah"
# print(states_of_malaysia[0])

# states_of_malaysia.append("Kuala Lumpur")
# print(states_of_malaysia[-1])

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
print(f"{names[random.randint(0,len(names)-1)]} is going to buy the meal today!")

person_who_will_pay = random.choice(names)
print(person_who_will_pay + " is going to buy the meal today!")