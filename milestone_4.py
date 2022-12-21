import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives
        self.word = random.choice(word_list)

        self.word_guessed = ["_" for character in self.word]

        self.num_letters = len(set(self.word))
        self.list_of_guesses = []


word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

hangman = Hangman(word_list)
print(hangman.word)
print(hangman.word_guessed)
print(hangman.num_letters)

