import random

def hangman():
    words = ['python', 'hangman', 'programming', 'developer', 'challenge', 'computer', 'function', 'variable']


    word_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6
    word_completion = '_' * len(word_guess)

    print("Welcome to Hangman!")
    print("You have", max_incorrect_guesses, "incorrect guesses allowed.")

    while incorrect_guesses < max_incorrect_guesses and '_' in word_completion:
        print("\nCurrent word:", ' '.join(word_completion))
        print("Guessed letters:", ' '.join(guessed_letters))
        guess = input("Please guess a letter: ").lower()


        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue


        if guess in guessed_letters:
            print("You have already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)

        if guess in word_guess:
            print("Good guess!")

            word_completion = ''.join([letter if letter in guessed_letters else '_' for letter in word_guess])
        else:
            incorrect_guesses += 1
            print("Incorrect guess. You have", max_incorrect_guesses - incorrect_guesses, "guesses left.")

    if '_' not in word_completion:
        print("\nCongratulations! You've guessed the word:", word_guess)
    else:
        print("\nSorry, you've run out of guesses. The word was:", word_guess)



if __name__ == "__main__":
    hangman()