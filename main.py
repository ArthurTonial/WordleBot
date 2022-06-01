import os


def read_words_file(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        return [(line.strip(), 0.0) for line in lines]


def initiate_dictionary():
    aux = {}
    for char in 'abcdefghijklmnopqrstuvwxyz':
        aux[char] = [0, 0, 0, 0, 0, 0]
    return aux


def calculate_letter_incidence():
    for word_score in words_scores:
        for i in range(len(word_score[0])):
            letters_chance[word_score[0][i]][i] += 1
            letters_chance[word_score[0][i]][-1] += 1


def score_words():
    for ws in range(len(words_scores)):
        aux = list(words_scores[ws])
        aux[1] = 0.0

        for pos in range(len(aux[0])):
            aux[1] += 2 * letters_chance[aux[0][pos]][pos]
            aux[1] += letters_chance[aux[0][pos]][-1]

        words_scores[ws] = tuple(aux)


def print_best_words():
    for i in range(min(10, len(words_scores))):
        print(f'#{i+1}\t{words_scores[i][0]}\t{words_scores[i][1]}')


def letter_not_in_the_word(letter):
    return [word_score for word_score in words_scores if letter not in word_score[0]]


def letter_in_wrong_place(letter, position):
    return [word_score for word_score in words_scores if letter in word_score[0] and letter != word_score[0][position]]


def letter_in_right_place(letter, position):
    return [word_score for word_score in words_scores if letter == word_score[0][position]]


if __name__ == '__main__':
    words_scores = read_words_file('wordle-allowed-guesses.txt')
    words_scores += read_words_file('wordle-answers-alphabetical.txt')
    sorted(words_scores)

    attempts = 0
    feedback = ''

    while attempts < 6 and feedback != '22222':
        os.system('cls')

        letters_chance = initiate_dictionary()

        calculate_letter_incidence()
        score_words()

        words_scores.sort(key=lambda x: x[1], reverse=True)
        print_best_words()

        guess = str(input(f'\nattempt {attempts + 1}: ')).lower()
        feedback = str(input('obtained result: '))

        if feedback != '22222':
            for i in range(len(feedback)):
                if feedback[i] == '0':
                    words_scores = letter_not_in_the_word(guess[i])
                if feedback[i] == '1':
                    words_scores = letter_in_wrong_place(guess[i], i)
                if feedback[i] == '2':
                    words_scores = letter_in_right_place(guess[i], i)

        attempts += 1

    if attempts == 6:
        print('FAIL')
    else:
        print('SUCCESS')
