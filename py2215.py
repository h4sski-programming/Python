# coded by h4sski
'''
https://pynative.com/python-exercises-with-solutions/
Exercise 7: Print the following number pattern
1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5
'''

n = 5

for i in range(n):
    s = str(i+1)
    string = ''
    for j in range(n-i, 0, -1):
        string += s + " "
    print(string)