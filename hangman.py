import words, random

def hangman(score):

    word = random.choice(words.countries)
    word_lower = word.lower()
    guessed = ['_' if ch != ' ' else ' ' for ch in word]
    attempts = 5
    guessed_letters = set()

    print("Can you guess the Country?\n")
    print(''.join(guessed), '\n')

    while attempts > 0 and '_' in guessed:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1:
            print("\nPlease enter a single letter.")
            continue
        if not (guess.isalpha() or guess == "'" or guess =="-"):
            print("\nPlease enter a letter, apostrophe or hyphen.")
            continue
        if guess in guessed_letters:
            print("\nYou've already guessed that letter.\n")
            continue

        guessed_letters.add(guess)

        if guess in word_lower:
            for i, letter in enumerate(word_lower):
                if letter == guess:
                    guessed[i] = guess
            print("\n'{}' was a corect guess! Attempts left: {}".format(guess, attempts))
        else:
            attempts -= 1
            print("\n'{}' was an incorrect guess. Attempts left: {}".format(guess, attempts))

        print(''.join(guessed).capitalize())
        print('Guessed Letters: ', ', '.join(sorted(guessed_letters)), '\n')

    if '_' not in guessed:
        score.append_score(word, attempts)
        print("\nCongratulations! You won! The word was '{}'.".format(word))
        print('You had {} attempts remaining!'.format(attempts))
        score.display()
        score.leaderboard()
    else:
        print("\nGame over! The word was '{}'.".format(word))
        score.display()
        score.leaderboard()
        score.reset()