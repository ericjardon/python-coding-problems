import math


def getBillionUsersDay(growthRates):
  # We need to find T without having to sequentially generate all
  # values of num of users at a given t.
  
  # We probe t in an exponential fashion:
  # start at t=convenient value. Compute users; if too high, look in lower half,
  # if too low, duplicate t.
  
  lo = 1
  hi = 50
  TARGET = 1000000000
  
  while lo<=hi:
    t = lo + (hi-lo)//2
    users = 0
    i = 0
    # Avoid overflow with a while loop
    while i < len(growthRates) and users < TARGET:
      users += (growthRates[i] ** t)
      i += 1
    
    if users >= TARGET:  # try lower values of t
      hi = t - 1
    else:  
      lo = t + 1
      hi = hi*2
  
  # Binary search biased to the left. Lo will hold the first value that meets >= target
  # Alternatively we use an extra variable result that we set to mid every time we find a value >= target.
  # in the end, result would hold the last value that met condition. 
  # We are extending our search space as long as f(t) < 1Billion. We are splitting in half our distance to target at every iteration.
  return lo


# TIME: O(logN) where N is roughly number of values from 1 to our target X and possible overshoot. (Exponential overshoots)


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
  test_1 = [1.1, 1.2, 1.3]
  expected_1 = 79
  output_1 = getBillionUsersDay(test_1)
  check(expected_1, output_1)

  test_2 = [1.01, 1.02]
  expected_2 = 1047
  output_2 = getBillionUsersDay(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  