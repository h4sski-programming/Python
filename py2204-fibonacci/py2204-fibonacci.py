# coded by h4sski
#  Fibonacci
# An = An-1 + An-2



def getFibonacci (n):
    a1 = 0
    a2 = 1
    a = 0
    i = 2
    while i<n:
        a = a1 + a2
        a1 = a2
        a2 = a
        i += 1
    return a
        

print(getFibonacci(3))
print(getFibonacci(4))
print(getFibonacci(5))
print(getFibonacci(6))
print(getFibonacci(7))

print(getFibonacci(50))
print(getFibonacci(300))