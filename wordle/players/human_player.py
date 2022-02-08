from players import Player
from termcolor import colored
from wordle.settings import WORD_LENGTH

class HumanPlayer(Player):
    def __init__(self, name):
        self.name = name
    
    def choose(self, board, i):
        """Ask the user to choose the word"""
        while True:
            attempt = input('Attempt #' + str(i + 1) + ': ').upper()
            if len(attempt) == WORD_LENGTH and attempt in self.word_bank: # Ensures user input is valid
                break
            else:
                print(colored('\nNot in word bank.', 'red'))
        return attempt
    
    def __str__(self):
        return self.name
