rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

import random

choice_img = [rock, paper, scissors]
while(1):
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors. "))
    if user_choice == 0 or user_choice == 1 or user_choice == 2:
        break
    else:
        print("Invalid input! Try again.")

print(choice_img[user_choice])

computer_choice = random.randint(0,2)

print(f"Computer chose: {choice_img[computer_choice]}2")

if ((user_choice == 2 and computer_choice == 1) or (user_choice == 1 and computer_choice == 0) or (user_choice == 0 and computer_choice == 2)):
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw.")
else:
    print("You lose!")