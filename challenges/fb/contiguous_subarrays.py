'''
Given an array of N integers (ranfging from 1 to 1,000,000,000)

For every number A[i] in the array; determine 
the number of contiguous subarrays that can be formed containing A[i] in 
the head or tail and where A[i] is the maximum number in that position.
'''

# Find the number of arrays (i.e. num of values less than) where i starts, right[i]
# Find number of arrays where i ends, left[i]
# Total is (left[i] + 1) * (right[i] + 1)

# we can maybe do this in two passes, one for right and another for left?

def count_subarrays_INCORRECT(arr):
    '''Counts only strictly increasing subarrays'''
    N = len(arr)

    left = [0] * N
    right = [0] * N

    for i in range(1, N):
        # traverse to the left to form left[i]

        # if element to the left is gte, no subarrays to the left are possible
        if arr[i-1] >= arr[i]:
            left[i] = 0
        # if element to the left is smaller, num of subarrays to the left are
        # previous element's number of subarrays + 1
        else:
            left[i] = left[i-1] + 1

    for i in range(N-2, -1, -1):
        # traverse from the right to form right[i]
        if arr[i+1] >= arr[i]:
            right[i] = 0
        else:
            right[i] = right[i+1] + 1
    
    # Combine left and right to form total num of subarrays
    print(left)
    print(right)
    ans = [0] * N
    print()
    for i in range(N):
        ans[i] = left[i] + right[i] +1 
    
    return ans



############# CORRECT SOLUTION

import math
# Add any extra import statements you may need here


# Add any helper functions you may need here


def count_subarrays(a):
  # Write your code here
  # split count into two scenarios
  # extremes dont have any subarrays to their extreme side.
  
  N = len(a)

  # Two passses: one for counting subarrays ending at i, another for starting at i.
  
  # For every position, what info do we need? -x: items to the left less than a[i], -j: the index of closest position bigger than a[i].
  # when we find a smaller left value, check its -j, compare to a[i], add to the num of subarrays and then we continue moving to the lft
  # until we find a value that bests current a[i].
  
  L = [0 for _ in range(N)]
  left_j = [-1 for _ in range(N)]
  for i in range(1,N):
    # Compare left neighbor to a[i]
    subarrays = 0
    j = i-1
    
    while j != -1 and a[i] > a[j]:
      subarrays = i - j  # add number of bested elements to the left of a[j]
      j = left_j[j]  # update a[j]
    
    if j == -1: # a[i] is largest of all elements to the left
      subarrays = i
    
    print("To left of", a[i], ":",subarrays)
    L[i] = subarrays
    left_j[i] = j
  
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
  

##############


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