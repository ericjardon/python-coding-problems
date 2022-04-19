import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
from collections import deque

def place(table, end, guest):
  if end == -1:
    pair = table[-1]
    table.append(guest)
    return abs(guest - pair)
  
  else:
    pair = table[0]
    table.appendleft(guest)
    return abs(guest - pair)

def minOverallAwkwardness(arr):
  # array of heights. Guests are 1-indexed.
  
  # Awkwardess[i] = abs(heigh[i] - height[j])
  # Due to circular table, there are N adjacencies among N guests.
  # AwkwardnessOverall = max(awkwardness) among the N pairs
  
  # For a given list of guests, determine the minimum possible max awkwardness.
  
  # We cannot simply sort because the last pair (N:1) will have biggest difference.
  # Instead, we can pick the max value and sit the next two tallest around him, 
  # and for the rest of the guests, place the next tallest in the bigger end.
  
  max_awk =  -1
  table = deque()
  
  arr.sort()  # min length is 3
  
  table.append(arr.pop())  # max height guest
  while arr:
    # pop next and place in the tallest end
    if table[0] > table[-1]:
      awk = place(table, 0, arr.pop())
    else:
      awk = place(table, -1, arr.pop())
    
    max_awk = max(awk, max_awk)
  
  return max_awk
  











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  arr_1 = [5, 10, 6, 8]
  expected_1 = 4
  output_1 = minOverallAwkwardness(arr_1)
  check(expected_1, output_1)

  arr_2 = [1, 2, 5, 3, 7]
  expected_2 = 4
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)

  # Add your own test cases here
  arr_2 = [2, 2, 2]
  expected_2 = 0
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)
  
  arr_2 = [7,7,7,7,1]
  expected_2 = 6
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)
  
  arr_2 = [1,2,3,4,5,6]
  expected_2 = 2
  output_2 = minOverallAwkwardness(arr_2)
  check(expected_2, output_2)