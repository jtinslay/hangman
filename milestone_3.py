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