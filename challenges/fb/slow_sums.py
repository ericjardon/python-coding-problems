import math
# Add any extra import statements you may need here


# Add any helper functions you may need here
import heapq
# heapq module is a min-heap. to make a max-heap we use negatives.

def getTotalTime(arr):
  # We could try to always pick the two largest elems
  # we could use a heap and pop twice, push the sum once until heap empty
  arr = [-x for x in arr]  # no zeroes in input guaranteed
  
  heapq.heapify(arr)
  penalty = 0
  while len(arr) > 1:
    a = -(heapq.heappop(arr))
    b = -(heapq.heappop(arr))
    #print("add",a,"+",b)
    s = a+b
    penalty += s
    heapq.heappush(arr, -s)
  
  return penalty
  ##NOTE: an alternate solution is to sort first, pop twice and append the sum
  # for every tail element we add the sum to total. : penalty = penalty + (penalty+tail)
  # pop and add it to the penalty. 

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
  arr_1 = [4, 2, 1, 3]
  expected_1 = 26
  output_1 = getTotalTime(arr_1)
  check(expected_1, output_1)

  arr_2 = [2, 3, 9, 8, 4]
  expected_2 = 88
  output_2 = getTotalTime(arr_2)
  check(expected_2, output_2)
  
  arr_3 = [1,1,2,3,4,5]
  expected_3 = 9+12+14+15+16
  output_3 = getTotalTime(arr_3)
  check(expected_3, output_3)
  
  
  arr_3 = [50, 2,1,50]
  expected_3 = 100+102+103
  output_3 = getTotalTime(arr_3)
  check(expected_3, output_3)

  # Add your own test cases here
  