from random_player import RandomPlayer
from semirandom_player import SemiRandomPlayer
from wordle import gameHandler
from human_player import HumanPlayer
from random_player import RandomPlayer
from settings import FILENAME

#test
while True:
    fileName = FILENAME
    f = open(fileName)
    parole = f.read()
    f.close
    word_bank = [x.upper() for x in parole.split()]

    gh = gameHandler(word_bank, SemiRandomPlayer("Luca", word_bank))
    gh.play()

    if input('\nWant to play again with a new word? Type anything to keep playing, or type [q]uit to quit. ').upper().startswith('Q'):
        print('\nThanks for playing.\n')
        exit()