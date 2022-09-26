#coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that returns the elements on odd 
positions in a list.
'''

list_input = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

def main(list):
    temp_list = []
    for i, element in enumerate(list):
        if i%2 != 0:
            temp_list.append(element)
    return temp_list


if __name__ == '__main__':
    print(main(list_input))