# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that takes a number and returns a list 
of its digits. So for 2342 it should return [2,3,4,2].
'''

number = 2342

def main(num):
    list = []
    num = str(num)
    for n in num:
        list.append(n)
    return list

if __name__ == '__main__':
    print(main(number))