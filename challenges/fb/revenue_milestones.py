'''
we want to know on what days Facebook hits certain revenue milestones. 
Given an array of the revenue on each day (1-based), and an array of milestones 
Facebook wants to reach, return an array containing the days on which 
Facebook reached every milestone.

That is, return the day where we first reached revenue k.
'''

import math
# Add any extra import statements you may need here

# Add any helper functions you may need here
def bSearch(A, target):
  
  lo = 0
  hi = len(A)-1
  
  # Find first occurrence that is larger or equal to target
  while lo <= hi:
    mid = lo + (hi - lo)//2
    if A[mid]>=target:
      # Continue moving mid to the left until interval closed
      hi = mid - 1
    else:
      # As long as we are less than target, we move lo forward
      # Lo will eventually stop at the first value that is larger or equal
      lo = mid + 1 
  
  if lo >= len(A): # Strictly increasing array so if we never find a value gte target, it's not there
    return -1
    
  return lo
      
  

def getMilestoneDays(revenues, milestones):
  # Perform binary search on the summed array
  # For every milestone we binary search for the day where sum is >=revenue
  N = len(revenues)
  accumulated = [r for r in revenues]
  for i in range(1,N):
    accumulated[i] = revenues[i] + accumulated[i-1]
  
  print(revenues)
  print(accumulated)
  ans = []
  for k in milestones:
    i = bSearch(accumulated, k)
    ans.append(i+1 if i != -1 else -1)
  
  return ans
  
  
  
  
  

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

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
  revenues_1 = [100, 200, 300, 400, 500]
  milestones_1 = [300, 800, 1000, 1400]
  expected_1 = [2, 4, 4, 5]
  output_1 = getMilestoneDays(revenues_1, milestones_1)
  check(expected_1, output_1)

  revenues_2 = [700, 800, 600, 400, 600, 700]
  milestones_2 = [3100, 2200, 800, 2100, 1000] 
  expected_2 = [5, 4, 2, 3, 2]
  output_2 = getMilestoneDays(revenues_2, milestones_2)
  check(expected_2, output_2)

  # Add your own test cases here
  