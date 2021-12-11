#Step 1 

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

import random

def check_letter_exist(word, letter):
    for i in range(len(word)):
        if word[i] == letter:
            print("Right")
        else:
            print("Wrong")

chosen_word = random.choice(word_list).lower

guess_letter = input("Guess a letter: ")

check_letter_exist(chosen_word, guess_letter)