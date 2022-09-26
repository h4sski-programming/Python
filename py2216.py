# coded by h4sski
'''
https://pynative.com/python-exercises-with-solutions/
Exercise 9: Modify the element of a nested list inside the following list
Change the element 35 to 3500
Given:
list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]
Expected Output: -
[5, [10, 15, [20, 25, [30, 3500], 40], 45], 50]
'''

list1 = [5, [10, 15, [20, 25, [30, 35], 40], 45], 50]

def is_same_as(list, number, new_number):
    for element in list:
        if type(element) != type(2):
            is_same_as(element, number, new_number)
        else:
            if element == number:
                print(element, type(element), new_number)
                element = new_number
                print(element)

is_same_as(list1, 35, 3500)

print(list1)

