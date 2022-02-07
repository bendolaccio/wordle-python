import random
import re
from termcolor import colored

ALLOWED_ATTEMPTS = 6
WORD_LENGTH = 5


f = open(r'PAROLE.txt')
parole = f.read()
f.close

word_bank = [x.upper() for x in parole.split()]

def validate(attempt, answer, current_alpha):
    result = ''
    s = list(answer)
    for pos, char in enumerate(attempt):
        if char == s[pos]: # Letter is correct and in right position
            result += (' ' + colored(char, 'green') + ' ')
            color = 'green'
            s[pos]= '0'
            "".join(s)
        elif char in s: # Letter is correct but in wrong position
            result += (' ' + colored(char, 'yellow') + ' ')
            color = 'yellow'
            answer = answer.replace(char, '0', 1)
            s = list(answer)
        else: # Letter is incorrect
            result += (' ' + char + ' ')
            color = 'red'
        current_alpha = current_alpha.replace(char, (colored(char, color)))  
    return current_alpha, result

def guess(answer):
    alphabet = ('\n\n   Q  W  E  R  T  Y  U  I  O  P   \n    A  S  D  F  G  H  J  K  L    \n      Z  X  C  V  B  N  M     \n\n')
    print('\nEnter your ' + str(ALLOWED_ATTEMPTS) + ' guesses. \n')
    for i in range(ALLOWED_ATTEMPTS):
        while True:
            print(alphabet)
            attempt = input('Attempt #' + str(i + 1) + ': ').upper()
            if len(attempt) == WORD_LENGTH and attempt in word_bank: # Ensures user input is valid
                break
            else:
                print(colored('\nNot in word bank.', 'red'))
        if attempt == answer: # Checks if user won
            return True
        else:
            alphabet, guess_result = validate(attempt, answer, alphabet)
            print(f"\n{guess_result}\n")
    return False
    
def main():
    print('\n\n\nI am thinking of a ' + str(WORD_LENGTH) + '-letter word. Can you guess in ' + str(ALLOWED_ATTEMPTS) + ' tries? \n')
    print('If a letter is in the right place, it will be ' + colored('green', 'green') + '.\n' +
    'If it is in the word but in the wrong place, it will be ' + colored('yellow', 'yellow') + '.\n' +
    'If it is not in the word, it will be ' + colored('red', 'red') + '.\n')
    while True:
        answer = random.choice(word_bank) # Picks a word for this turn
        #answer = 'OSMII' #used for debug with double
        if guess(answer):
            print(colored('\nCongratulations! You won!\n', 'green', attrs=['bold']))
        else:
            print('\nYou lost! The word was ' + colored(answer, 'green') + '\n')
        if input('\nWant to play again with a new word? Type anything to keep playing, or type [q]uit to quit. ').upper().startswith('Q'):
            print('\nThanks for playing.\n')
            exit()

main()
