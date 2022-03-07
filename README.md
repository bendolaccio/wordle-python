# wordle-python
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

## Results

The semirandom player scores 3,83 on a 100 games run with the italian file.
The intelligent player now scores 3,53 on a 100 games run with the italian file.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
