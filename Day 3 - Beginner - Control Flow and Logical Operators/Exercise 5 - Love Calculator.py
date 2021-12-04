# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# bill = 0

# if height >= 120:   # Greater than or equal to
#     print("You can ride the rollercoaster!")
#     age = int(input("What is your age? "))
#     if age < 12:
#         print("Child tickets are $5.")
#         bill = 5
#     elif age <= 18:
#         print("Youth tickets are $7.")
#         bill = 7
#     elif age >= 45 and age <= 55:
#         print("Everything is going to be ok. Have a free ride on us!")
#     else:
#         print("Adult tickets are $12.")
#         bill = 12
#     wants_photo = input("Do you want a photo taken? Y or N.")
#     if wants_photo == "Y":
#         #Add $3 to their bill.
#         bill += 3
#     print(f"Your final bill is ${bill}")
# else:
#     print("Sorry, you have to grow taller before you can ride.")


# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
l_n = name1.lower() + name2.lower()   # Both name combined with lower case.
score_n1 = l_n.count('t') + l_n.count('r') + l_n.count('u') + l_n.count('e') 
score_n2 = l_n.count('l') + l_n.count('o') + l_n.count('v') + l_n.count('e')

score = int(str(score_n1) + str(score_n2))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")

