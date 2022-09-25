# codded by h4sski

'''
https://www.w3resource.com/python-exercises/basic/
2. Write a Python program to create all possible 
strings by using 'a', 'e', 'i', 'o', 'u'. 
Use the characters exactly once. 
'''

input = ['a', 'e', 'i', 'o', 'u']
string = ''

for letter in input:
    string += letter
print(string)

'''
i = 0
string = ''
while i < len(input):
    j = i+1
    string = input[i]
    print(string)
    while j < len(input) and j > i:
        if i != j:
            string += input[j]
            k = i+1
            while k < len(input) and k != j:
                string += input[k]
                print(string)
                k += 1
        j +=1
    i += 1
'''

'''
pass throu all elements

'''