import random
import re
from termcolor import colored
from settings import ALLOWED_ATTEMPTS, WORD_LENGTH

class gameHandler(object):
    def __init__(self, word_bank, player):
        self.player = player
        self.word_bank = word_bank
        self.attempt = 0
        self.letter_not_in_word = {}
        self.letter_in_word = {}

    def populateLetterNotInWord(self, char, pos, color):
        #refactor red
        if color == 'red':
            if f'{char}' in self.letter_in_word:
                if len(self.letter_in_word[f'{char}'])!=0: #red after green BUG HERE IF 0Y0RG (REINI word to guess, RISII word guessed)
                    if f'{char}' not in self.letter_not_in_word:
                        self.letter_not_in_word[f'{char}']= []
                    if len(self.letter_in_word[f'{char}']) <= len(self.letter_not_in_word[f'{char}']): # red after green and yellow
                        self.letter_not_in_word[f'{char}'].append(pos)
                        self.letter_not_in_word[f'{char}'].sort()
                    else: #red only after green, not yellow
                        self.letter_not_in_word[f'{char}'] = [0, 1, 2, 3, 4]
                        for position in self.letter_in_word[f'{char}']:
                            self.letter_not_in_word[f'{char}'].remove(position)
                else:   #red after yellow
                    if f'{char}' not in self.letter_not_in_word:
                        self.letter_not_in_word[f'{char}']= []
                    self.letter_not_in_word[f'{char}'].append(pos)
                    self.letter_not_in_word[f'{char}'].sort()
            else: #straight red
                self.letter_not_in_word[f'{char}'] = [0, 1, 2, 3, 4]

        if color == 'yellow':
            if f'{char}' not in self.letter_not_in_word:
                self.letter_not_in_word[f'{char}']= []
            self.letter_not_in_word[f'{char}'].append(pos)
            self.letter_not_in_word[f'{char}'].sort()
        
        if color == 'green':
            #now we should add the fact that EVERY OTHER letter is not in that position
            for i in range(65, 91):
                if f'{chr(i)}' != char: # only other letters
                    if f'{chr(i)}' not in self.letter_not_in_word:
                        self.letter_not_in_word[f'{chr(i)}'] = []
                    if pos not in self.letter_not_in_word[f'{chr(i)}']:
                        self.letter_not_in_word[f'{chr(i)}'].append(pos)
                    self.letter_not_in_word[f'{chr(i)}'].sort()

        
        # a green letter does not exclude the presence of another same green letter
        # the knowledge about that letter 'not in' a place must not be deleted
    
    def populateLetterInWord(self, char, pos, color):
        if color == 'yellow':
            if f'{char}' not in self.letter_in_word:
                self.letter_in_word[f'{char}'] = []
        if color == 'green':
            if f'{char}' not in self.letter_in_word:
                self.letter_in_word[f'{char}'] = []
            if pos not in self.letter_in_word[f'{char}']:    
                self.letter_in_word[f'{char}'].append(pos)
        self.letter_in_word[f'{char}'].sort()

    #input:
    # - answer
    # - attempt
    # - alphabet
    #output
    # - new alphabet (colored)
    # - dictionary pos:color and final entry attempt:string
    def validate(self, attempt, answer, current_alpha):
        # result will be a dictionary with:
        # - string with the attempt
        # - len(WORD_LENGTH) other entries: [pos:color]
        result = {
            "attempt_result" : attempt
        }
        
        answer_s = list(answer)
        attempt_s = list(attempt)
        #first check if there are letters in right position and replace them in order to not consider them twice
        for pos, char in enumerate(attempt):
            if char == answer_s[pos]: # Letter is correct and in right position
                #replace char with 0 in answer
                
                result[str(pos)] = 'green'
                color = 'green'
                answer_s[pos]= '0'
                answer = "".join(answer_s)

                #replace char with 0 in attempt so this character will not be checked again in the yellow/red cycle
                attempt_s[pos] = '0'
                attempt = "".join(attempt_s)

                current_alpha = current_alpha.replace(char, (colored(char, color))) 

                self.populateLetterInWord(char, pos, 'green')
                self.populateLetterNotInWord(char, pos, 'green')
        #then check for the yellow letters: correct letters, but in wrong positions
        #it must be done in two separate cycles otherwise some yellow can be displayed instead of some green
        for pos, char in enumerate(attempt):
            if char == '0': #green already checked and replaced
                continue
            elif char in answer_s: # Letter is correct but in wrong position
                result[str(pos)] = 'yellow'
                color = 'yellow'
                answer = answer.replace(char, '0', 1)
                answer_s = list(answer)
                self.populateLetterInWord(char, pos, 'yellow')
                self.populateLetterNotInWord(char, pos, 'yellow')
                
            else: # Letter is incorrect
                result[str(pos)] = 'red'
                color = 'red'
                self.populateLetterNotInWord(char, pos, 'red')
            current_alpha = current_alpha.replace(char, (colored(char, color)))  
        return current_alpha, result
    
    #simple function used to print the attempt with the right colors
    def printResult(self, resultDictionary):
        result = list(resultDictionary['attempt_result']) #i only need a string with the right length
        for pos, char in enumerate(resultDictionary['attempt_result']):
            if resultDictionary[str(pos)] == 'green':
                color = 'green'
                
            elif resultDictionary[str(pos)] == 'yellow':
                color = 'yellow'
                
            else:
                color = 'white'
                
            result[pos] = colored(char, color)
        print(f"\n{''.join(result)}\n")

    # for every attempt calls the validate function and do work on the result
    def guess(self, answer, alphabet):
        for i in range(ALLOWED_ATTEMPTS):
            while True:
                print(alphabet)
                attempt = self.player.choose(i, self.letter_not_in_word)
                if len(attempt) == WORD_LENGTH and attempt in self.word_bank: # Ensures user input is valid
                    break
                else:
                    print(colored('\nNot in word bank.', 'red'))
            if attempt == answer: # Checks if user won
                self.attempt = i
                return True
            else:
                alphabet, guess_result = self.validate(attempt, answer, alphabet)
                #very important: update the knowledge of the player
                self.player.update_knowledge(self.letter_not_in_word, self.letter_in_word)
                self.printResult(guess_result)
        self.attempt = i+1
        return False
    
        
    def play(self):
        print('\n\n\nI am thinking of a ' + str(WORD_LENGTH) + '-letter word. Can you guess in ' + str(ALLOWED_ATTEMPTS) + ' tries? \n')
        print('If a letter is in the right place, it will be ' + colored('green', 'green') + '.\n' +
        'If it is in the word but in the wrong place, it will be ' + colored('yellow', 'yellow') + '.\n' +
        'If it is not in the word, it will be ' + colored('red', 'red') + '.\n')

        alphabet = ('\n\n   Q  W  E  R  T  Y  U  I  O  P   \n    A  S  D  F  G  H  J  K  L    \n      Z  X  C  V  B  N  M     \n\n')
        print('\nEnter your ' + str(ALLOWED_ATTEMPTS) + ' guesses. \n')

        while True:
            answer = random.choice(self.word_bank) # Picks a word for this turn
            #answer = 'CIOFI' #used for debug
            if self.guess(answer, alphabet):
                print(colored('\nCongratulations! You won!\n', 'green', attrs=['bold']))
                break
            else:
                print('\nYou lost! The word was ' + colored(answer, 'green') + '\n')
                break
        return self.attempt