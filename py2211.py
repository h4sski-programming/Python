# coded by h4sski
'''
https://pynative.com/python-exercises-with-solutions/
Exercise 2: Read text file into a variable and replace 
all newlines with space
Given: Assume you have a following text file (sample.txt).
Line1
line2
line3
line4
line5
Expected Output:
Line1 line2 line3 line4 line5
'''

file_input = open('py2211_input.txt', 'r')
print(file_input.read())
output_string = ''

# for line in file_input:
#     if line != '':
strint_input = str(file_input.read())
s = strint_input.replace('\n', ' ')
output_string += s

output_string = str(file_input.read())
output_string = output_string.replace('i', ' ')

print(output_string)
# file_output = open('py2211_output.txt', 'w')
# file_output.write(output_string)
# file_output.close()

a = 'qwerqwerqwer'
b = a.replace('q', 'Q')
# print(a, b)