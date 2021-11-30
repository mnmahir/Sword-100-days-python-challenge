# print(8 / 3)
# print(round(8 / 3))
# print(round(8 / 3, 2))

# print(8 // 3)   # Floor division - will automatically convert to integer (ie if 2.123 will become 2)

# # f-String (f-string will do all the converting behind the scene)
# score = 10
# height = 1.7
# isWinning = True
# print(f"your score us {score}, your height is {height}, you are winning is {isWinning}")
# print(f"1 + 2 is {1+2}")

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
days = 365
weeks = 52
months = 12
left = 90 - int(age)25
print(f"You have {left * days} days, {left * weeks} weeks, and {left * months} months left.")

