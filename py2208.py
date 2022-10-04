# codded by h4sski

'''
https://www.w3resource.com/python-exercises/basic/
1. Write a Python program to check the sum of three
elements (each from an array) from three arrays is
equal to a target value. Print all those three-element
combinations.
'''

x = [10, 20, 20, 20]
y = [10, 20, 30, 40]
z = [10, 30, 40, 20]
target = 70

for a in x:
    for b in y:
        for c in z:
            sum = a+b+c
            if sum == target:
                print(a, b, c, 'sum =', sum)
