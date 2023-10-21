# Code for milestone3 from AiCore: Hangman game

#import random word

random_word="strawberry"

## Check if input letter is in the word: 

def check_guess(guess):
        guess_lower_case = guess.lower()
        if guess in random_word: 
                print(f'Good guess! {guess} is in the word.')
        elif guess not in random_word:
                print(f'Sorry, {guess} is not in the word. Try again.')




## Ask for user input

def ask_for_input():
		while True: 
			guess = input("Guess a letter: ")
			if len(guess) == 1 and guess.isalpha() == True: 
				check_guess(guess)
			else: 
				print("Invalid letter. Please, enter a single alphabetical character.")
ask_for_input()


