from intelligent_player import IntelligentPlayer
from random_player import RandomPlayer
from semirandom_player import SemiRandomPlayer
from intelligent_player import IntelligentPlayer
from wordle import gameHandler
from human_player import HumanPlayer
from random_player import RandomPlayer
from settings import FILENAME, NUMBER_OF_MATCHES

#test

attempt_list = []

#while True:
for i in range(NUMBER_OF_MATCHES):
    fileName = FILENAME
    f = open(fileName)
    parole = f.read()
    f.close
    word_bank = [x.upper() for x in parole.split()]

    gh = gameHandler(word_bank, SemiRandomPlayer("Luca", word_bank))
    attempt = gh.play()
    attempt_list.append(attempt)
    '''
    if input('\nWant to play again with a new word? Type anything to keep playing, or type [q]uit to quit. ').upper().startswith('Q'):
        print('\nThanks for playing.\n')
        exit()
    '''
print(f'The run has concluded with a score of {float(sum(attempt_list)/len(attempt_list)):.4f}')