#Modules to import
import random
import re

#Create the Hangman class
class Hangman: 

        #Initialise the attributes of the class
        def __init__(self, word_list, num_lives=5):

                #define the parameters
                self.word_list = word_list
                self.num_lives = num_lives
                self.word = random.choice(word_list)
                self.word_guessed = list(re.sub("[a-zA-Z]", "_", self.word))
                self.num_letters = self.word_guessed.count("_")
                self.word_list = ["strawberry", "kiwi", "papaya", "pineapple", "dragonfruit"]
                self.list_of_guesses = []


        #Check if the letter is in the word 
        def check_guess(self,guess):
	        guess_lower = guess.lower()
        	if guess_lower in self.word: 
                	        print("Good guess!", guess_lower, "is in the word.")
                        	char_index = [pos for pos, char in enumerate(self.word) if char == guess_lower]
                        	for index in char_index:
                        		self.word_guessed[index] = guess_lower
                        		print(self.word_guessed)  
                        	self.num_letters = self.word_guessed.count("_")   
        	else:   	
                        	self.num_lives = self.num_lives - 1
                        	print("Sorry,", guess_lower, "is not in the word.")        
                        	print("You have", self.num_lives,"lives left.")  



#function asks user to guess a letter
        def ask_for_input(self):
                while True: 
                        guess = input("Guess a letter: ")
                        if not guess.isalpha() or len(guess) > 1:
                                        print("Invalid letter. Please, enter a single alphabetical character.")
                        elif guess in self.list_of_guesses: 
                                        print("You already tried that letter!")
                        else: 
                                        self.list_of_guesses.append(guess)
                                        self.check_guess(guess=guess)


word_list = ["car", "boat", "bicycle"]

def play_game(word_list):
        num_lives=5
        game = Hangman(word_list=word_list, num_lives=num_lives)
        while True: 
                if game.num_lives == 0: 
                        print("You lost!")
                elif game.num_letters > 0: 
                        print(game.num_letters)
                        game.ask_for_input()
                elif game.num_letters == 0:
                        print("Congratulations! You won the game!")
                        return

play_game(word_list)

