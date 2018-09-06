import string

import random

wordlist = 'wordlist.txt'

#Choosing length of word for game

def get_random_word(length_of_word):
    words = []
    with open(wordlist, 'r') as f:

        for word in f:
            if '(' in word or ')' in word:
                continue

            word = word.strip().lower()

            if len(word) == length_of_word:
                words.append(word)

        return random.choice(words)

def num_of_attempts():

    while True:
        num_attempts = input('Please enter the number of attempts you\'d like, must be between ...')

        try:
            num_attempts = int(num_attempts)
            if 1 <= num_attempts <= 25:
                return num_attempts
            else:
                print('Attempts must be in specified range')
        except ValueError:
            print('{} is not an integer'.format(num_attempts))

def get_word():

    while True:
        length_of_word = input('Please enter the length of word you\'d like, mist be between... :  ')

        try:
            length_of_word = int(length_of_word)
            if 3 <= length_of_word <= 17:
                return length_of_word
            else:
                print('must be between ...')
        except ValueError:
         print('{} must be an integer'.format(length_of_word))

word = 'number'

