'''
Given an array of N integers (ranfging from 1 to 1,000,000,000)

For every number A[i] in the array; determine 
the number of contiguous subarrays that can be formed containing A[i] in 
the head or tail and where A[i] is the maximum number in that position.
'''

############# CORRECT SOLUTION 4 apr
'''
You are given an array arr of N integers. For each index i, you must determine 
the number of contiguous subarrays that fulfill the following conditions:
1. The value at index i must be the maximum element in the contiguous subarrays, and
2. These contiguous subarrays must either start from or end on index i.
'''
import math


def count_subarrays(a):
  # split count into two scenarios
  # extremes dont have any subarrays to their extreme side.
  
  N = len(a)

  # As basic premise: 
  # the subarrays to the right of i (start at i) are equal to the number of contiguous elements to the right smaller than a[i]
  # same can be said about subarrays to the left of i (end at i)
  # Then, make 2 passses: one l->r for counting subarrays ending at i, another l<-r for subarrays starting at i.
  
  # In l->r, for every position a[i], what info do we need? 
  # -x: num of items to the left less than a[i], 
  # -j: the index of last position to the left such that a[j] > a[i] (and j < i),
  # when we reach a smaller val, check its bester: a[j] and compare to a[i], add to the num of subarrays and then we continue moving to the lft
  # until we find a value that bests current a[i].
  
  L = [0 for _ in range(N)]  # L[i] num of elements to the left smaller than a[i]
  left_j = [-1 for _ in range(N)]  # index of closest element to the left larger than a[i]. -1 means none

  # i moves to the right and reuses the information of positions less than i
  for i in range(1,N):
    # Compare left neighbor to a[i]
    subarrays = 0
    j = i-1
    # j moves to the left, all the way to the first element larger than a[j]
    while j != -1 and a[i] > a[j]:
      subarrays = i - j  # add number of bested elements to the left of a[j]
      j = left_j[j]  # jump to next element larger than a[j], like a linked list
    
    if j == -1: # a[i] is largest of all elements to the left
      subarrays = i
    
    print("To left of", a[i], ":",subarrays)
    L[i] = subarrays
    left_j[i] = j  # element at a[j] is larger that a[i]. This data is used for next positions to the right
  

  # Do the same for subarrays starting at i: move i back to front, counting larger elements to the right of i
  R = [0 for _ in range(N)]
  right_j = [N for _ in range(N)]
  
  for i in range(N-2, -1, -1):
    subarrays=0
    j = i+1
    while j != N and a[i]  > a[j]:
      subarrays = j - i
      j = right_j[j]
    
    if j == N:
      subarrays = N - i - 1
    
    R[i] = subarrays
    right_j[i] = j

  
  # Every num has at least one contiguous subarray (itself), plus subarrays to the left and right of i
  ans = [1 + L[i] + R[i] for i in range(N)]

  return ans
  

############## ANALYSIS

# Time complexity:
# We traverse the same array (len N) twice.
# In every step, we look back: when direction -> we look at most at i elements; when direction <-, we look at most at N-1-i elements.
# Thus, we do something like O((N*N + N)/2) times 2, simplified: O(2N*N) = O(N^2)

# Space complexity:
# For both types of subarray (ending and starting), we keep two arrays of length N each. We use a final array for the answer.
# So space complexity is O(5N), we can optimize by reusing our two aux arrays on a given pass.


def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)