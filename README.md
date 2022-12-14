
# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is a Python implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1
- The GitHub repository is setup

## Milestone 2
- A list of 5 possible fruits is defined and one is selected at random through the use of the random module as the word for the user to guess.
- The user is then asked to enter a letter. The user input is validated to check if it is a single alphabetic letter. If the user input validation fails, the program exits with an error message. If the user input validation passes, the program exits with a message stating that the user input was valid.

```python
import random

word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

word = random.choice(word_list)

print(word)

print("Please enter a letter from the alphabet:")
guess = input()

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
```

- Output when an invalid letter is input, and then when the program is run again with a valid alpthabetical letter as input

![Milestone 2 command line output](milestone_2_command_line_output.png)