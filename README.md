# Python3-Hangman
A simple Python3 hangman game.  

The program flow is as follows:

1. Define number of permitted incorrect attempts [1-25]
2. Define a minimum word length [4-16]
3. The program randomly generates a new wordlist upon each run, and on the first one creates a wordlist if it does not exist.
4. The program selects a suitable word based on the user's input for (2.)
5. The game commences - with number of attempts remaining shown along with previous letter guesses by the player.
6. The desired word is hidden with ****** and becomes unhidden as the player guesses a correct letter.
7. This program runs infinitely allowing the player to continously play whether they win or lose. Although, it does not support exiting via ^C when run within the IDE.

