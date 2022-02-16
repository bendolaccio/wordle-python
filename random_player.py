from base import Player
import random
import time


class RandomPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
        self.letter_not_in_word = {}
        self.letter_in_word = {}
    
    def choose(self, i, letter_not_in_word):
        attempt = random.choice(self.word_bank)
        print(f"Attempt #{i+1}: {attempt}")
        time.sleep(3)
        return attempt
    
    def update_knowledge(self, letter_not_in_word, letter_in_word):
        self.letter_not_in_word = letter_not_in_word
        self.letter_in_word = letter_in_word

    def __str__(self):
        return self.name