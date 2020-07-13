# Python3-Hangman
A simple Python3 hangman game.  

## Dependencies and Installation
Just one non-standard package is required:

* **[RandomWords](https://pypi.org/project/RandomWords/)** - This is used to auto-generate / re-generate the wordlist.txt file for the script to use.

This can be installed using pip or pip3 by running the command below in your scripts environment:

```
pip3 install RandomWords
```


## Program Flow
The program flow is as follows:

1. Define number of permitted incorrect attempts [1-25].
2. Define a minimum word length [4-16].
3. The program randomly generates a new wordlist upon each run, and on the first one creates a wordlist if it does not exist.
4. The program selects a suitable word based on the user's input for (2.).
5. The game commences - with number of attempts remaining shown along with previous letter guesses by the player.
6. The desired word is hidden with ****** and becomes unhidden as the player guesses a correct letter.
7. This program runs infinitely allowing the player to continously play whether they win or lose.

