from base import Player
import random
import time


class SemiRandomPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
        self.knowledge = {} #dictionary with the same format of the result plus the record 'letter not in word'
        self.letter_not_in_word = {[]} # format: list of    'letter': 'A'
                                       #                    'position': [1, 2, 3]
    
    def choose(self, i, letter_not_in_word):
        self.word_bank = self.reduceWordBank(self.word_bank, letter_not_in_word)
        attempt = random.choice(self.word_bank)
        print(f"Attempt #{i+1}: {attempt}")
        time.sleep(3)
        return attempt

    def __str__(self):
        return self.name
    
    #this function iterate on each letter of the knowledge so far and select 
    # all the words that match with the letter considered
    # For example: knowledge = 'A _ _ I O' 
    def reduceWordBank(self, word_bank, letter_not_in_word):
        reduced_word_bank = []
        for word in word_bank:
            for pos, char in word: #check the green ones first (with an eye on letters not in word)
                continue
        return reduced_word_bank