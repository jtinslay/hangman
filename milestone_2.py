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
    

