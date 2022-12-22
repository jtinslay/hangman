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
            for index, letter in enumerate(self.word.lower()):
                if letter == guess:
                    self.word_guessed[index] = letter

            self.num_letters -= 1

        else:
            self.num_lives -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"You have {self.num_lives} lives left.")

    def ask_for_input(self):
        print(self.word)

        while True:
            print("Guess a letter!")
            guess = input()

            if not len(guess) == 1 or not guess.isalpha():
                print("Invalid Letter. Please, enter a single alphabetical character.")

            elif guess in self.list_of_guesses:
                print("You already tried that letter!")

            else:
                self.check_guess(guess)

                self.list_of_guesses.append(guess)
                print(f"{self.num_letters} {self.word_guessed}")

                break


word_list = ["Apples", "Oranges", "Strawberries", "Blueberries", "Kiwis"]

hangman = Hangman(word_list)

hangman.ask_for_input()
