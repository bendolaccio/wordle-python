# Wordle-python
### A small python program that emulate the game wordle and implements an intelligent autosolver

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install termcolor.

```bash
pip install termcolor
```

## Usage

The player that you want to use must be declared in main.py
```python
gh = gameHandler(word_bank, SemiRandomPlayer("A name", word_bank))
```
Instead of `SemiRandomPlayer` it can be used:
* `RandomPlayer`
* `IntelligentPlayer`
* `HumanPlayer`

Change the settings in `settings.py` if necessary, then:
```bash
python3 main.py
```

## Description

It has been provided 4 kind of players:
* Random Player: at each step choose one word in the word bank
* SemiRandom Player: play a random choice and at every guess reduces the word bank. Every red letter discard all the words that contains that letter. Every yellow letter is batched in one list: then discard all the words that contains that letter in that position and keep all the words that contains the list of letter batched. Every green letter keep all the words that contains that letter in that position.
* Intelligent Player: the logic of reduction of word bank is the same of SemiRandom Player, but before guessing it makes a statistics of the 5 most present letters for each position of the word to guess by using the remaining words in the word bank. Then it find a word that maximize the probability of the 5 letters
* Human Player: for playing yourself :)

## Ideas
The idea behind the Intelligent Player is to try to maximize the reduction of the word bank. The perfect guess, in that hypothesis, is a word that contains the most likely letter in each position. The Intelligent Player assign a score at every letter of each position and choose the word that maximize the medium score.
Example:

![image](https://user-images.githubusercontent.com/10921226/157059511-de30beb5-a2b4-46d9-841d-ab6a3f8690d0.png)

The word choosen is ORARI (that has 3 green letters):

![image](https://user-images.githubusercontent.com/10921226/157059618-8876d543-08f0-45b1-949c-f2f858322ff6.png)


## Results

The semirandom player scores 4,830 on a 1000 games run with the italian file.
The intelligent player now scores 4,325 on a 1000 games run with the italian file (no testing with penalized repetition for now).
Intelligent player with penalized repetition scores 4,280 on a 100 games run with the italian file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
