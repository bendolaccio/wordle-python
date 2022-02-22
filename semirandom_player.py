from base import Player
import random
import time


class SemiRandomPlayer(Player):
    def __init__(self, name, word_bank):
        self.name = name
        self.word_bank = word_bank
        self.letter_in_word = {}        # format: 'A' : [1,3,5]
        self.letter_not_in_word = {}    # format: 'A' : [1,3,5]
                                        #         'B' : [1,3,4,5]

    def choose(self, i, letter_not_in_word):
        print(f'Length of word_bank = {len(self.word_bank)}')
        self.word_bank = self.reduceWordBank(self.word_bank, self.letter_not_in_word, self.letter_in_word)
        print(f'Length of word_bank reduced = {len(self.word_bank)}')
        if len(self.word_bank) == 0:
            print('ERROR')
            quit
        attempt = random.choice(self.word_bank)
        #attempt = input('Attempt #' + str(i + 1) + ': ').upper() #used for a test
        print(f"Attempt #{i+1}: {attempt}")
        time.sleep(3)
        return attempt

    def __str__(self):
        return self.name
    
    def checkLettersNotInWord(self, word_bank, letter_not_in_word):
        newWordBank = word_bank
        if len(letter_not_in_word.keys())!=0:
            result = []
            for letter in letter_not_in_word.keys():
                positions = letter_not_in_word[letter]
                for pos in positions:
                    temp = [word for word in word_bank if word[pos] == letter] #find all the words that contains that letter in that position
                    result.extend([word for word in temp if word not in result]) # copy in result without duplicates
            newWordBank = [word for word in word_bank if word not in result] #create a new list with all the words of word_bank without words in res
            print(f'Word bank reduced of {len(word_bank)-len(newWordBank)} words by elimination')
        return newWordBank
    
    def checkLettersInWord(self, word_bank, letter_in_word): #only purpose, for now, is to filter words that contains yellow letters
        newWordBank = word_bank
        if len(letter_in_word.keys())!=0:
            result = []
            yellow_letters = []
            for letter in letter_in_word.keys():
                '''
                if len(letter_in_word[letter]) == 0: # so if it's a yellow letter with position unknown
                    temp = [word for word in word_bank if letter in word]
                    result.extend([word for word in temp if word not in result]) # copy in result without duplicates
                '''
                if len(letter_in_word[letter]) == 0: # so if it's a yellow letter with position unknown
                    yellow_letters.append(letter)
            if len(yellow_letters) != 0:
                temp = [word for word in word_bank if all(x in word for x in yellow_letters)] #extracts words that contains ALL yellow letters at once. Not one or another
                result.extend([word for word in temp if word not in result])
                newWordBank = [word for word in word_bank if word in result]
            print(f'Word bank reduced of {len(word_bank)-len(newWordBank)} words by keeping only words with yellow letters')
        return newWordBank
    
    #this function iterate on each letter of the knowledge so far and select 
    # all the words that match with the letter considered
    def reduceWordBank(self, word_bank, letter_not_in_word, letter_in_word):
        reduced_word_bank = self.checkLettersNotInWord(word_bank, letter_not_in_word)
        reduced_word_bank = self.checkLettersInWord(reduced_word_bank, letter_in_word)

        return reduced_word_bank
    
    def update_knowledge(self, letter_not_in_word, letter_in_word):
        self.letter_not_in_word = letter_not_in_word
        self.letter_in_word = letter_in_word