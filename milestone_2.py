# Hangman code

#Create a list of words

word_list = ["strawberry", "apple", "banana", "kiwi", "blueberry"]
print(word_list)

#Select a random word from the list

import random

word = random.choice(word_list)
print(word)

#User guesses a letter

guess = input("Guess a letter: ")

#Check that the letter is a valid input (one alphabetical guess)
import re

if re.match(r"^[a-zA-Z]",guess):
	if len(guess) == 1:
		print("That's a good guess")
	elif len(guess) > 1: 
		print("Guess one letter at a time")
else:
	print("Oops! That is not a valid input.")

