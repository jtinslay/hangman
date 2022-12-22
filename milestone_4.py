import random

class Hangman:
    def __init__(self, word_list, num_lives = 5):
        self.word_list = word_list
        self.num_lives = num_lives

        self.word = random.choice(word_list)
        self.word_guessed = ["_" for _ in range(len(self.word))]

        self.num_letters = len(set(self.word))
        self.list_of_guesses = []

    def check_guess(self, guess):
        guess = guess.lower()

        if guess in self.word.lower():
            print(f"Good guess! {guess} is in the word.")

    def ask_for_input(self):

        while True:
            print("Guess a letter!")

            guess = input()
            print(f"guess {guess}")

            if not len(guess) == 1 or not guess.isalpha():
                print("Invalid Letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                    print("You already tried that letter!")

            else:
                self.check_guess(guess)
                print(f"guess {guess}")

                self.list_of_guesses.append(guess)
                print(self.list_of_guesses)



word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

hangman = Hangman(word_list)
print(hangman.word)
print(hangman.word_guessed)
print(hangman.num_letters)

hangman.ask_for_input()
