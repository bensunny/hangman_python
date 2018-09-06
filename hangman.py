import string

import random
WORDLIST = 'wordlist.txt'


def get_random_word(min_word_length):
    words = []
    with open(WORDLIST, 'r') as f:
        for word in f:
            if '(' in word or ')' in word:
                continue
            word = word.strip().lower()
            if len(word) != min_word_length:
                continue
            words.append(word)
    return random.choice(words)


def get_num_attempts():
    while True:
        num_attempts = input("""
        How many incorrect attempts would you like? 
        must be between 1 and 25: """)

        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print('{} is not an integer between 1 and 25'.format(num_attempts))
        except ValueError:
            print('{} is not an integer'.format(num_attempts))


def get_min_word_length():
    while True:
        print('')
        min_word_length = input('please enter the length of word you\'d like, must be between 3 and 17: ')

        try:
            min_word_length = int(min_word_length)
            if 3 <= min_word_length <= 17:
                return min_word_length
            else:
                print('{} is not an integer between 3 and 17'.format(min_word_length))
        except ValueError:
            print('{} is not an integer'.format(min_word_length))


def get_display_word(word, idxs):
    if len(word) != len(idxs):
        raise ValueError(' length of word and indices must be the same')
    displayed_word = ' '.join([letter if idxs[i] else '_' for i, letter in enumerate(word)])
    return displayed_word.strip()


def get_next_letter(remaining_letters):
    if len(remaining_letters) == 0:
        raise ValueError('There are no remaining letters')
    while True:
        next_letter = input('Choose the next letter: ').lower()
        if len(next_letter) != 1:
            print('{} is not a single character'.format(next_letter))
        elif next_letter not in string.ascii_lowercase:
            print('{} is not a letter'.format(next_letter))
        elif next_letter not in remaining_letters:
            print('{} has been guessed before'.format(next_letter))
        else:
            remaining_letters.remove(next_letter)
            return next_letter


def play_hangman():
    print('Starting a game ...')
    attempts_remaining = get_num_attempts()
    min_word_length = get_min_word_length()

    print('selecting a word ...')
    word = get_random_word(min_word_length)
    print()

    idxs = [letter not in string.ascii_lowercase for letter in word]
    remaining_letters = set(string.ascii_lowercase)
    wrong_letters = []
    word_solved = False

    while attempts_remaining > 0 and not word_solved:
        print('Word: {}'.format(get_display_word(word, idxs)))
        print('Attempts remaining: {}'.format(attempts_remaining))
        print('previous Guesses: {}'.format(' '.join(wrong_letters)))

        next_letter = get_next_letter(remaining_letters)

        if next_letter in word:
            print('{} is in the word!'.format(next_letter))

            for i in range(len(word)):
                if word[i] == next_letter:
                    idxs[i] = True
        else:
            print('{} is not in the word'.format(next_letter))
            attempts_remaining -=1
            wrong_letters.append(next_letter)

    if False not in idxs:
        word_solved = True
        print()

        print('The word is {}'.format(word))

    if word_solved:
        print('Congratz!')
    else:
        print('')
        print('Better luck next time\n')
        print('The word is {}'.format(word))

    try_again = input('would you like to try again? [y/n}: ')
    return try_again.lower() == 'y'

if __name__ == '__main__':
    while play_hangman():
        print()


