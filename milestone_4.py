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


