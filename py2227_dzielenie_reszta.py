# coded by h4sski

import random


def get_rand(down, up):
    return random.randrange(down, up)


def check_correct(a=None, rest=None, v=None, r=None):
    if a == v and rest == r:
        print(f'  Correct!')
        return True
    print(f'  Wrong, try again:')
    return False


def main():
    down, up = 2, 10
    for _ in range(10):
        a = get_rand(down, up)
        b = get_rand(down, up)
        product = a * b
        rest = get_rand(0, b)
        # print(f'{product + rest} / {b} = {a}, reszta {rest}')
        # print(f'{b} * {a} = {b*a}')
        statement = False
        while not statement:
            v = int(input(f'{product + rest} / {b} = '))
            r = int(input('reszta = '))
            statement = check_correct(a, rest, v, r)


if __name__ == '__main__':
    main()
