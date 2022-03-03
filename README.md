# wordle-python
### A small python program that emulate the game wordle and implements a naive autosolver.

It has been provided 4 kind of players:
* Random Player: at each step choose one word in the word bank
* SemiRandom Player: play a random choice at every guess reduces the word bank. Every red letter discard all the words that contains that letter. Every yellow letter is batched in one list: then discard all the words that contains that letter in that position and keep all the words that contains the list of letter batched. Every green letter keep all the words that contains that letter in that position.
* Intelligent Player: like SemiRandom Player, but before guessing makes a statistics of the 5 most present letters for each position of the word to guess by using the remaining words in the word bank. Then it find a word that maximize the probability of the 5 letters
* Human Player: for playing yourself :)

The intelligent player now scores 3,53 on a 100 games run with the italian file.
