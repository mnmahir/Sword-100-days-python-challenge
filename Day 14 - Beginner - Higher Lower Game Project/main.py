import random
import os
from re import A
from art import logo,vs
from game_data import data


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

# Generate Question
def generate_question():
    a = b = data[random.randint(0,len(data)-1)]
    while b == a:
        b = data[random.randint(0,len(data)-1)]
    return a,b

# Check which is higher
def higher(a, b):
    if a.get('follower_count') > b.get('follower_count'):
        return 'A'
    else:
        return 'B'

# Game Start
def play_game():
    cont_play = True
    score = 0
    print(logo)
    while(cont_play == True):
        compare, against = generate_question()
        print(f"A: {compare.get('name')}, a {compare.get('description')}, from {compare.get('country')}")
        print(vs)
        print(f"B: {against.get('name')}, a {against.get('description')}, from {against.get('country')}")
        print("=======================================================================")
        user_input = input("Who has more followers? Type 'A' or 'B': ")
        
        answer = higher(compare, against)
        if ((user_input == 'A' or user_input == 'a') and answer == 'A'):
            score += 1
        elif ((user_input == 'B' or user_input == 'b') and answer == 'B'):
            score += 1
        else:
            cont_play = False
            clearConsole()
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            return
        clearConsole()
        print(logo)
        print(f"You are Right! Current Score: {score}")

play_game()