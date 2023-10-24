""
A game of Hangman

A word is randommy chosen from a list of words
""

#Modules to import
import random
import re

#Create the Hangman class
class Hangman: 

""" Hangman Class with all the functions to play Hangman """


        #Initialise the attributes of the class
        def __init__(self, word_list, num_lives=5):
"""The class requires a list of words (word_list), and number of lives (num_lives, default=5) """

                #define the parameters
                self.word_list = word.list
                self.num_lives = num_lives
                self.word = random.choice(word_list)
                self.word_guessed = list(re.sub("[a-zA-Z]", "_", self.word))
                self.num_letters = self.word_guessed.count("_")
                self.num_lives = 5
                self.word_list = ["strawberry", "kiwi", "papaya", "pineapple", "dragonfruit"]
                self.list_of_guesses = []


        #Check if the letter is in the word 
        def check_guess(self.guess):
        """"The function takes the letter provided by the user, and checks if it is in the random_word. It then replaces the placeholder "_" with the letter and returns the full word with all the correctly guessed letters and placeholders for the letters still to be guessed """
        guess_lower = guess.lower()
                if guess_lower in self.word: 
                        print("Good guess! {guess} is in the word.")


#function asks user to guess a letter
        def ask_for_input():
        """Prompt user to provide a single letter as a guess for the word """
                while True: 
                        guess = input("Guess a letter: ")
                                if not guess.isalpha() or len(guess) > 1:
                                        print("Invalid letter. Please, enter a single alphabetical character.")
                                elif guess in self.list_of_guesses: 
                                        print("You already tried that letter!")
                                else: 
                                        self.list_of_guesses.append(guess) and check_guess(guess)
