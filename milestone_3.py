import random

word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

word = random.choice(word_list)
print(word)

while True:
    print("Type a letter: ")
    guess = input()
    if len(guess) == 1 and guess.isalpha():
        if guess.lower() in word.lower():
             print(f"Good guess! {guess} is in the word")
        else:
             print(f"Sorry, {guess} is not in the word. Try again")
    else:
        print("Please, enter a single alphabetical character.")
