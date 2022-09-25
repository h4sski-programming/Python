#  coded by h5sski
'''
https://adriann.github.io/programming_problems.html
Write a guessing game where the user has to guess 
a secret number. After every guess the program tells 
the user whether their number was too large or too small. 
At the end the number of tries needed should be printed. 
It counts only as one try if they input the same number 
multiple times consecutively.
'''

import random

lower_range = 0
upper_range = 20
is_playing = True

while is_playing:
    print('Do you wnat to play? [ y / n ] ')
    play = input().lower()
    if play == 'n':
        is_playing = False
    elif play == 'y':
        number = random.randrange(lower_range, upper_range)
        is_wrong = True
        score = 0
        inp = int(input('Type a number '))
        while is_wrong:
            # inp = int(inp)
            if inp < number:
                inp = int(input('Too low, type again '))
                score += 1
            elif inp > number:
                inp = int(input('Too high, type again '))
                score += 1
            else:
                print('Correct! Your score =', score)
                is_wrong = False
    else:
        print('Not valid input, try again.')
    print('/ \ / \ / \ / \ / \ / \ / \ / \ ')
print('Thank you for game :)')