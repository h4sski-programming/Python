# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that checks whether an element 
occurs in a list.
'''

def is_in_list(elem, list):
    response = False
    for i, e in enumerate(list):
        if e == elem:
            print(i, e)
            return True
    return response


def main():
    list_original = [1, 4, 'ab', 67, 3]
    element_4 = 4
    element_ab = 'ab'
    element_qwe = 'qwe'
    print(is_in_list(element_4, list_original))
    print(is_in_list(element_ab, list_original))
    print(is_in_list(element_qwe, list_original))


if __name__ == '__main__':
    main()