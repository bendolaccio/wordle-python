from base import Player
import random
import time


class RandomPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
    
    def choose(self, alphabet, word_bank, i):
        attempt = random.choice(word_bank)
        print(f"Attempt #{i+1}: {attempt}")
        time.sleep(3)
        return attempt

    def __str__(self):
        return self.name