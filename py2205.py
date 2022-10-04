# codded by h4sski

'''
https://www.w3resource.com/python-exercises/basic/
1. Write a Python function that takes a sequence of numbers
and determines whether all the numbers are different
from each other.
'''

input = [1, 1, 3, 4, 4, 6, 7, 8, 9, 9, 33]

n, m = 0, 0

while n < len(input):
    m = n+1
    while m < len(input):
        if input[n] == input[m]:
            print(input[n], 'same as', input[m])
        m += 1
    n += 1

print('end of program')
