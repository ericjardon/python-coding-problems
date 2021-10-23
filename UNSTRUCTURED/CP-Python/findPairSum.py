"""Given an array of sorted integer numbers and an integer X,
 find if there is a pair of numbers in the array such that
  their sum is equal to X in linear time"""
from random import choice

def find_pair_in_sorted(A, x):
    i = 0
    j = len(A)-1
    while i<j:
        s = A[i] + A[j]
        if s == x:
            return True
        elif A[i] + A[j] < x:   # if sum is too small, increment smaller num
            i += 1
        else:   # if sum is too large, decrease larger num
            j -=1
    return False    # worst case is O(n)

"""And if the Array is not sorted? Still linear time"""
def find_pair_not_sorted(A, x):
    table = {}  # store the number : complement pairs in a hash set (dictionary)
    for num in A:
        if x-num not in table:
            table[num] = 1
        else:
            return True
    return False

n=5
A = [choice(range(1,n+1)) for _ in range(n)]
print(A)
n = int(input("Sum: "))
print(find_pair_not_sorted(A, n))