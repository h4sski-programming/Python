# codded by h4sski

'''
https://www.w3resource.com/python-exercises/basic/
12. Write a Python program to create all possible 
permutations from a given collection of distinct numbers.
'''


'''
Factorial of the lenght of the list.
Then devide it by list lenght and fulfill each part with first character.
Then each of sub list we can treat as the first / original one.
'a', 'b', 'c'
3! = 6
6 / 3 = 2
a,   a,   b,   b,   c,   c
ab,  ac,  ba,  bc,  ca,  cb
abc, acb, bac, bca, cab, cba
'''

# nums = [1, 2, 3, 4]
# nums_len = len(nums)
# perm = ''
# perm_list = []

# for i in range(nums_len):
#     perm = str(nums[i])
#     for j in range(nums_len):
#         if str(nums[j]) not in str(perm):
#             perm += str(nums[j])
#     perm_list.append(perm)
    # perm += str(nums[i])
    # perm_list.append(perm)
    
# print(perm_list)

import fractions
from math import factorial


print('------------------')

'''
list = ['a', 'b', 'c', 'd']
list_len = len(list)
step = 1
perm = ''
perm_list = []

for i in range(list_len):
    perm = list[i]
    for step in range(list_len):
        if list[step] not in perm:
            perm += list[step]
    for step in range(0, list_len, -1):
        if list[step] not in perm:
            perm += list[step]
    perm_list.append(perm)

for i in range(0, list_len, -1):
    perm = list[i]
    for step in range(0, list_len, -1):
        if list[step] not in perm:
            perm += list[step]
    perm_list.append(perm)
    
    
print(perm_list)
'''


print('------------------')

'''
Factorial of the lenght of the list.
Then devide it by list lenght and fulfill each part with first character.
Then each of sub list we can treat as the first / original one.
'a', 'b', 'c'
3! = 6
6 / 3 = 2
a,   a,   b,   b,   c,   c
ab,  ac,  ba,  bc,  ca,  cb
abc, acb, bac, bca, cab, cba
'''

'''list = ['a', 'b', 'c', 'd']
list = ['a', 'b', 'c']
list_len = len(list)
permutations = []
num_permutations = factorial(list_len)

# first fulfill of the permutations list
for i in range(num_permutations):
    permutations.append('')

for char in range(list_len):
    if char > 0 and char < list_len:
        print(list[char])
        for position in range(int(num_permutations / char), int(num_permutations / char + 1)):
            print(position)
            permutations[position].append('a')


def function(temp_permutations):
    num_of_permutations = factorial(list_len)
    # print(list_len, num_of_permutations, permutations)
    for i in range(list_len):
        for j in range(int(num_of_permutations / list_len)):
            temp_permutations.append(list[i])'''


list = ['a', 'b', 'c', 'd']
list = ['a', 'b', 'c']
org_numbers = [1, 2, 3]
list_len = len(list)
permutations = []


# def resolve(numbers):
#     result_solution = [[]]
#     for n in numbers:
#         sub_solution = []
#         for solution in result_solution:
            
#     return result_solution


# nie rozumiem tego rozwiazania ...




# print(permutations)
print(resolve(org_numbers))

'''
What do I can pass to function?
/ temp list of permutations (sub list from previous iteration)
    / global list of permutations, but we can pass worst and last position
    of the sub-list
/ input list, can be decreasd by already used characters
/ 
'''



print('------------------')

def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

my_nums = [1,2,3]
print("Original Cofllection: ",my_nums)
print("Collection of distinct numbers:\n",permute(my_nums))