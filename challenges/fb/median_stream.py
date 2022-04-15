import math
# Add any extra import statements you may need here
import heapq

# Add any helper functions you may need here


def findMedian(arr):
  # The median stands exactly at the middle of a sorted array of numbers.
  # This sorted array of numbers keeps increasing as we traverse arr.
  # we can keep trackof the middle element with two heaps: 
  # a max heap (left side) and a min heap (right side)
  N = len(arr)
  
  left = []  # max heap
  right = []  # min heap
  median = -1
  output = []
  
  for i in range(N):
    # compare arr[i] with median so we know where it is pushed to
    # compare heap lengths. If equal, median is the average of both roots.
    # if unequal, median is the root of larger heap.
    
    x = arr[i]
    if x < median:  # send to left
      heapq.heappush(left, -x)
    else:
      heapq.heappush(right, x)
    
    
    # We should balance out heap sizes when diff > 1.
    size_diff = len(right) - len(left)
    if size_diff > 1: # pop right and push to left
      heapq.heappush(left, -heapq.heappop(right))
    if size_diff < -1:  # pop left and push to right
      heapq.heappush(right, -heapq.heappop(left))
      
    #print("elems to left", len(left), 'max;',-left[0] if len(left) else -1)
    #print("elems to right", len(right),'min:',right[0] if len(right) else -1)
      
    if len(right) > len(left):  # right larger
      median = right[0]
    elif len(right) < len(left):  # left larger
      median = -left[0]
    else:
      median = int((right[0] - left[0])/2)  # substract left because its negative
    
    #print(f"{i}th median", median)
    output.append(median)
  
  return output





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
  arr_1 = [5, 15, 1, 3]
  expected_1 = [5, 10, 5, 4]
  output_1 = findMedian(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [2, 3, 4, 3, 4, 3]
  output_2 = findMedian(arr_2)
  check(expected_2, output_2)


  # Add your own test cases here
  