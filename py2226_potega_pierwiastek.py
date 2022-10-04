# coded by h4sski

import random
from re import A

MIN = 2
MAX = 10


def get_rand(up):
    return random.randrange(MIN, up)


def potega(w):
    a = get_rand(MAX)
    mistake = 0
    while True:
        v = int(input(f'{a}^{w} = '))
        v_correct = a ** w
        if v == v_correct:
            break
        else:
            mistake += 1
            print('  Zle, jeszcze raz:')
    return mistake


def pierwiastek(w):
    if w == 3:
        a = get_rand(4)
    else:
        a = get_rand(MAX)
    mistakes = 0
    while True:
        v_correct = a ** w
        # print(f'{a}^{w} = {v_correct}')
        v = int(input(f'Pierwiastek {w} stopnia z {v_correct} = '))
        if v == a:
            break
        else:
            mistakes += 1
            print('Zle, jeszcze raz:')
    return mistakes


def main():
    mistakes = 0
    wykladnik = random.choice([2, 3])
    for _ in range(10):
        r = random.choice(['p', 'p'])       # q for sqrt()
        if r == 'p':
            mistakes += potega(wykladnik)
        else:
            mistakes += pierwiastek(wykladnik)
    print()
    print(f'Popoelniles {mistakes} bledow.')


main()
