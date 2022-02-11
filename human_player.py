from termcolor import colored
from settings import WORD_LENGTH
from base import Player

class HumanPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
        self.knowledge = {}
    
    def choose(self, i, letter_not_in_word):
        """Ask the user to choose the word"""
        while True:
            attempt = input('Attempt #' + str(i + 1) + ': ').upper()
            if len(attempt) == WORD_LENGTH and attempt in self.word_bank: # Ensures user input is valid
                break
            else:
                print(colored('\nNot in word bank.', 'red'))
        return attempt
    
    def update_knowledge(self, result):
        self.knowledge = result

    def __str__(self):
        return self.name
