# coded by h4sski

'''
Write a program which will sort lelemtns in input list
descending. After that in ascending order.
'''

list = [3, 5, 10, 7]
list = [3, 5, 7, 5, 2, 10, 6, 8, 14, 6]
result = []

max = list[0]
temp_list = list.copy()
max = 100

n = 0

def finder_max(upper_limit, temp_l):
    m = 0
    m_position = 0
    for k in range(len(temp_l)):
        if temp_l[k] >= m and temp_l[k] <= upper_limit:
            m = temp_l[k]
            m_position = k
            n += 1
    return [m, m_position]

for i in range(len(list)):
    a = finder_max(max, temp_list)
    max = a[0]
    result.append(max)
    del temp_list[a[1]]

print(list)
print(result)
print(n)