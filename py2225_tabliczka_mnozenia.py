# coded by h4sski
import random


min = 3
max = 10


def get_random():
    return random.randrange(min, max)


def mnozenie(mistakes):
    a = get_random()
    b = get_random()
    while True:
        c = int(input(f'{a} * {b} = '))
        c_correct = a * b
        if c == c_correct:
            break
        else:
            mistakes += 1
            print('Zle, jeszcze raz:')
    return mistakes


def dzielenie(mistakes):
    a = get_random()
    b = get_random()
    while True:
        c = int(input(f'{a*b} : {a} = '))
        c_correct = b
        if c == c_correct:
            break
        else:
            mistakes += 1
            print('Zle, jeszcze raz:')
    return mistakes


def main():
    mistakes = 0
    for _ in range(10):
        r = random.choice(['m', 'd'])
        if r == 'm':
            mistakes = mnozenie(mistakes)
        else:
            mistakes = dzielenie(mistakes)
    print(f'Popoelniles {mistakes} bledow.')


main()
