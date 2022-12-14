
while True:
    print("Type a letter: ")
    guess = input()
    if len(guess) == 1 and guess.isalpha():
        break
    else:
        print("Please, enter a single alphabetical character.")
