# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that tests whether a string is a palindrome.
'''

string_1 = 'madam'
string_2 = 'nurses run'
string_3 = 'abcd'

def main(str):
    str = str.replace(' ', '')
    half_string = len(str) / 2
    for i, char in enumerate(str):
        if i < (half_string - 1):
            if char != str[-i - 1]:
                return False
    return True


if __name__ == '__main__':
    print(string_1, main(string_1))
    print(string_2, main(string_2))
    print(string_3, main(string_3))