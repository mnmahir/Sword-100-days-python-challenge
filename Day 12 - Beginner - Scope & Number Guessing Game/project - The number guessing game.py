import random
import os
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)

def play_game():
    answer = random.randint(1,100)
    difficulty = None
    guess = None
    guessed = []
    while(difficulty != 'easy' and difficulty != 'hard'):
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if difficulty == 'easy':
            tries = EASY_LEVEL_TURNS
        elif difficulty == 'hard':
            tries = HARD_LEVEL_TURNS
        else:
            print("Invalid input.")

    clearConsole()

    while(guess != answer and tries != 0):
        print("I'm thinking of a number between 1 and 100.")
        print(f"You have {tries} attempt(s) remaining to guess the number.")
        print(f"Guessed: {guessed}")
        guess = int(input("Make a guess: "))
        clearConsole()
        if guess in guessed:
            print("Number already guessed.")
        else:
            guessed.append(guess)
            tries -= 1
            if guess > answer:
                print("TOO HIGH!")
            elif guess < answer:
                print("TOO LOW!")
            else:
                print("You are right!")
        if tries == 0:
            clearConsole()
            print(f"Game over! The correct number is {answer}")

print(logo)
print("Welcome to the Number Guessing Game!")
play_game()