import numpy as np


def read_words_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [line.strip() for line in lines]


def initiate_dic():
    aux = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        aux[char] = [0, 0, 0, 0, 0, 0]
    return aux


def calculate_answers():
    for word in words_list:
        for i in range(len(word)):
            if word[i] not in letters_chance.keys():
                letters_chance[word[i]] = [0, 0, 0, 0, 0]
            letters_chance[word[i]][i] += 1
            letters_chance[word[i]][-1] += 1


def score_words():
    pass


def letter_not_in_the_word(letter):
    return [word for word in words_list if letter not in word]


def letter_in_wrong_place(letter, position):
    return [word for word in words_list if letter in word]


def letter_in_right_place(letter, position):
    return [word for word in words_list if letter == word[position]]


if __name__ == '__main__':
    words_list = read_words_file('wordle-allowed-guesses.txt')
    words_list += read_words_file('wordle-answers-alphabetical.txt')
    sorted(words_list)

    attempts = 0
    feedback = ''

    while attempts < 6 and feedback != '22222':
        letters_chance = initiate_dic()
        calculate_answers()



        # for i in letters_chance.keys():
        #     print(i + ': ', end='')
        #     print(letters_chance[i])

        guess = str(input()).lower()
        feedback = str(input())

        if feedback != '22222':
            for i in range(len(feedback)):
                if feedback[i] == '0':
                    words_list = letter_not_in_the_word(guess[i])
                if feedback[i] == '1':
                    words_list = letter_in_wrong_place(guess[i], i)
                if feedback[i] == '2':
                    words_list = letter_in_right_place(guess[i], i)

        attempts += 1

    if attempts == 6:
        print('FAIL')
    else:
        print('SUCCESS')