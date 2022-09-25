# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that returns the largest element 
in a list.
'''

list = [3, 5, 7, 5, 2, 10, 6, 8, 4, 6]
list = [3, 5, 7, 5, 2, 10, 6, 8, 14, 6]

position = 0
max = list[position]

for i in list:
    if max < i:
        max = i
print(max)