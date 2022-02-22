# wordle-python
A small python program that emulate the game wordle and implements a naive autosolver.
The logic of the solver is to reduce, at every guess, the word bank.
Every red letter discard all the words that contains that letter.
Every yellow letter is batched in one list: then discard all the words that contains that letter in that position and keep all the words that contains the list of letter batched
Every green letter keep all the words that contains that letter in that position
