import random

word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]
print(word_list)

word = random.choice(word_list)

print(word)

guess = input()

if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    5
