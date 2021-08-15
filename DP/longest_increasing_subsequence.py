'''
LONGEST INCREASING SUBSEQUENCE

A subsequence is a set of elements of an array, not necessarily contiguous.
Given an Array of integers, find the maximum lenght of a subsequence
where every subsequent element is strictly larger than the preceding one.

Hint:
The length of the L.I.S ending at index i is equal to 1 + the 
L.I.S. ending anywhere before i.

BASE: at every position, LIS is at least length=1
'''


def longest_increasing_subsequence(Arr, n):

    LIS = [1 for _ in range(n)]  # stores the length of LIS ending at index i

    # For every element in array
    for i in range(n):
        current = Arr[i]

        # For every element preceding index i
        for j in range(0, i):
            precedent = Arr[j]
            candidate_length = LIS[j] + 1
            if precedent < current and candidate_length > LIS[i]:
                LIS[i] = candidate_length

    return max(LIS)


print("Enter space separated values of the array:")
arr = [int(x) for x in input().split()]
print(longest_increasing_subsequence(arr, len(arr)))
