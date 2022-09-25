# coded by h4sski
'''
https://pynative.com/python-exercises-with-solutions/
Exercise 1: Reverse each word of a string
Given:
str = 'My Name is Jessa'
Expected Output
yM emaN si asseJ
'''

str = 'My Name is Jessa'
s = str.split(" ")
new_str = ''
for a in s:
    b = ''
    for i in range(len(a)-1, -1, -1):
        b += a[i]
    new_str += b + ' '

print(str, s)
print(new_str)