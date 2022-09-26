# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write three functions that compute the sum of the numbers 
in a list: using a for-loop, a while-loop and recursion. 
(Subject to availability of these constructs in your 
language of choice.)
'''

list_input = [1, 2, 3, 4, 5, 6, 7]

def for_loop(list):
    sum = 0
    for n in list:
        sum += n
    return sum

def while_loop(list):
    sum = 0
    i = 0
    while i < len(list):
        sum += list[i]
        i += 1
    return sum

def recursion_loop(list, step, sum):
    if step < len(list):
        sum += list[step] + recursion_loop(list, step+1, sum)
    return sum

def main(list):
    print('for loop\t\t', for_loop(list))
    print('while loop\t\t', while_loop(list))
    print('recursion loop\t\t', recursion_loop(list, 0, 0))

if __name__ == '__main__':
    main(list_input)