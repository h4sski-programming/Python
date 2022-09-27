# coded by h4sski
'''
https://adriann.github.io/programming_problems.html
Write a function that merges two sorted lists into a new 
sorted list. [1,4,6],[2,3,5] → [1,2,3,4,5,6]. You can do this 
quicker than concatenating them followed by a sort.
-------------------------------------------------------------
Write a function that rotates a list by k elements. 
For example [1,2,3,4,5,6] rotated by two becomes [3,4,5,6,1,2]. 
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?
'''

list_a, list_b = [1,4,6], [2,3,5]
list_ab = []

def merge_and_sort():
    list_return = []
    for a, b, in zip(list_a, list_b):
        if a < b:
            list_return.append(a)
            list_return.append(b)
        else:
            list_return.append(b)
            list_return.append(a)
    return list_return

def rotate_func(rot, list):
    list_rotated = []
    for i in range(rot, len(list) + rot):
        if i < len(list):
            list_rotated.append(list[i])
        else:
            list_rotated.append(list[i-len(list)])
    return list_rotated

def main():
    list_ab = merge_and_sort()
    print(list_ab)
    print(rotate_func(2, list_ab))

if __name__ == '__main__':
    main()