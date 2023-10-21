# Hangman code

#Create a list of words

word_list = ["strawberry", "apple", "banana", "kiwi", "blueberry"]
print(word_list)

#Select a random word from the list

import random

random_word = random.choice(word_list)
print(random_word)

#User guesses a letter

user_letter_guess = input("Guess a letter: ")

#Check that the letter is a valid input - alphabetical and a single letter
import re

if re.match(r"^[a-zA-Z]",user_letter_guess):
	if len(user_letter_guess) == 1:
		print("That's a good guess")
	elif len(user_letter_guess) > 1: 
		print("Guess one letter at a time")
else:
	print("Oops! That is not a valid input.")

