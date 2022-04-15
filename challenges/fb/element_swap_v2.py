import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

def swap(a, i, j):
  a[i], a[j] = a[j], a[i]
  return

def findMinArray(arr, k):
  N = len(arr)
  # As long as k allows, 
  # for every position i, push the smallest -attainable- element in i+1...N to position i.
  
  # Use a mapper to keep track of position of next smallest
  
  # ~ Variant of insertion sort ~
  # Attainability of an element means its distance is lte to k.
  # We can move k elements forward and note the smallest element and its distance. 
  # Swap current i with smallest attainable j, and substract j-i from k
  
  i = 0
  while k>0 and i<N-1:
    # place smallest attainable in i
    min_att = arr[i]
    min_pos = i
    j = i+1
    
    while j<N and j-i<=k:
      if arr[j] < min_att:
        min_att = arr[j]
        min_pos = j
      j += 1
    
    # Everything is pushed to the right. This is less expensive than slicing.
    for j in range(min_pos, i, -1):
      swap(arr, j, j-1)
      k -= 1
    #print("seq", arr)
    
    i += 1
  
  return arr
  
    
      
    




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
  n_1 = 3
  arr_1 = [5, 3, 1]
  k_1 = 2 
  expected_1 = [1, 5, 3]
  output_1 = findMinArray(arr_1,k_1)
  check(expected_1, output_1)

  n_2 = 5
  arr_2 = [8, 9, 11, 2, 1]
  k_2 = 3
  expected_2 = [2, 8, 9, 11, 1]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)
  
    # Add your own test cases here
  n_2 = 5
  arr_2 = [5,4,3,2,1]
  k_2 = 7
  expected_2 = [1,2,5,4,3]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)

  # Add your own test cases here
  