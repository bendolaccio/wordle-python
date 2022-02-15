from random_player import RandomPlayer
from semirandom_player import SemiRandomPlayer
from wordle import gameHandler
from human_player import HumanPlayer
from random_player import RandomPlayer
from settings import FILENAME

#test
fileName = FILENAME
f = open(fileName)
parole = f.read()
f.close
word_bank = [x.upper() for x in parole.split()]

gh = gameHandler(word_bank, SemiRandomPlayer("Luca", word_bank))
gh.play()