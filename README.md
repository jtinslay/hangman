
# Hangman

Hangman is a classic game in which a player thinks of a word and the other player tries to guess that word within a certain amount of attempts.

This is a Python implementation of the Hangman game, where the computer thinks of a word and the user tries to guess it. 

## Milestone 1
- The GitHub repository is setup

## Milestone 2
- A list of 5 possible fruits is defined and one is selected at random through the use of the random module as the word for the user to guess.
- The user is then asked to enter a character. The user input is validated to check if it is a single alphabetic character. If the user input validation fails, the program exits with an error message. If the user input validation passes, the program exits with a message stating that the user input was valid.

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

- Output when an invalid letter is input, and then when the program is run again with a valid alphabetical letter as input

![Milestone 2 command line output](milestone_2_command_line_output.png)

## Milestone 3
Two functions, ask_for_input and check_guess are implemented.

Through a while loop, the ask_for_input function continuously runs, waiting for a valid input character guess from the user. A valid input character is defined as a single alphabetical character. After a valid character is input, the function calls the check_guess function.

The check_guess function checks if the guess is in the chosen word and prints a message telling the user if the guess was correct or not.

The program is run by calling the ask_for_input function.

```python
import random

word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

word = random.choice(word_list).lower()
print(word)

def check_guess(guess):
    if guess.lower() in word:
        print(f"Good guess! {guess} is in the word")
    else:
        print(f"Sorry, {guess} is not in the word. Try again")

def ask_for_input():
    while True:
        print("Type a letter: ")
        guess = input()

        if len(guess) == 1 and guess.isalpha():
            break
        else:
             print("Please, enter a single alphabetical character.")

    check_guess(guess)

ask_for_input()

```
