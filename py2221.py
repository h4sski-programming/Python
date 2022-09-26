# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that concatenates two lists. 
[a,b,c], [1,2,3] → [a,b,c,1,2,3]
--------------------------------------------------------
Write a function that combines two lists by alternatingly 
taking elements, e.g. [a,b,c], [1,2,3] → [a,1,b,2,c,3].
'''

list_a = ['a', 'b', 'c']
list_1 = [1, 2, 3]

def concatenate_lists(first, second):
    for n in second:
        first.append(n)
    return first

def combine_lists(first, second):
    list_output = []
    if len(first) > len(second):
        l = len(first)
    else:
        l = len(second)
    for i in range(l):
        list_output.append(first[i])
        list_output.append(second[i])
    return list_output

def main():
    print(concatenate_lists(list_a.copy(), list_1))
    # I coppied list_a to have it NOT-modified for second function
    print(combine_lists(list_a, list_1))

if __name__ == '__main__':
    main()