import math
# Add any extra import statements you may need here
from collections import deque

# Add any helper functions you may need here
def argsort(seq):
  return sorted(range(len(seq)), key=seq.__getitem__, reverse=True)

'''
For x iterations:
1. Pop x elements from the front of queue (or, if it contains fewer than x elements, pop all of them)
2. Of the elements that were popped, find the one with the largest value (if there are multiple such elements, take the one which had been popped the earliest), and remove it
3. For each one of the remaining elements that were popped (in the order they had been popped), decrement its value by 1 if it's positive (otherwise, if its value is 0, then it's left unchanged), and then add it back to the queue
'''

# N > x always

def simpleFind(arr):
    maxVal = -2
    maxPos = -1
    for (i,x) in enumerate(arr):
        if arr[i] > maxVal:
            maxVal = arr[i]
            maxPos = i+1
    return maxPos 

def findPositions(arr, x):
  # What if x == 1? return first max elem's position
  

  N = len(arr)
  if x == 1:
    return [simpleFind(arr)]

  if x==N:
    return [i+1 for i in argsort(arr)]
  
  N = len(arr)
  ans = []
  
  # Use 2 queues that move together
  # values and original index positions
  q = deque(arr)
  posq = deque([i+1 for i in range(N)])
  
  while q and len(ans) < x :
    # Pop x elements and pick largest
    size = len(q)
    tempq = []
    tempposq = []
    maxVal = -2
    maxPos = -1
    # Pop x elements or full queue 
    i = 0
    while i < x and i < size:
      tempq.append(q.popleft())
      tempposq.append(posq.popleft())
      
      if tempq[-1] > maxVal:
        maxVal = tempq[-1]
        maxPos = tempposq[-1]
      
      i += 1
    #print("tempvals", tempq)
    #print("temppos", tempposq)
    ans.append(maxPos)
    #print("answer", ans)
    
    # Push x-1 elements back
    for val, index in zip(tempq, tempposq):
      if val == maxVal and index == maxPos:  # append everything except max element
        continue
      q.append(max(0, val-1))
      posq.append(index)
    
    # repeat
    
  
  return ans



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

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
  n_1 = 6
  x_1 = 5
  arr_1 = [1, 2, 2, 3, 4, 5]
  expected_1 = [5, 6, 4, 1, 2]
  output_1 = findPositions(arr_1, x_1)
  check(expected_1, output_1)

  n_2 = 13
  x_2 = 4
  arr_2 = [2, 4, 2, 4, 3, 1, 2, 2, 3, 4, 3, 4, 4]
  expected_2 = [2, 5, 10, 13]
  output_2 = findPositions(arr_2, x_2)
  check(expected_2, output_2)

  # Add your own test cases here
  n_3 = 3
  x_3 = 3
  arr_3 = [3,5,4]
  expected_3 = [2,3,1]
  output_3 = findPositions(arr_3, x_3)
  check(expected_3, output_3)

  n_4 = 4
  x_4 = 1
  arr_4 = [3,3,3,3]
  expected_4 = [1]
  output_4 = findPositions(arr_4, x_4)
  check(expected_4, output_4)

