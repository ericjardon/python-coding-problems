'''
We have N different apps with different user growth rates. At a given time t, measured in days, 
the number of users using an app is g^t (for simplicity we'll allow fractional users), 
where g is the growth rate for that app. These apps will all be launched at the same time and 
no user ever uses more than one of the apps. We want to know how many total users there are when 
you add together the number of users from each app.
After how many full days will we have 1 billion total users across the N apps?
'''

import math
# Add any extra import statements you may need here

# TIME: 
# let M be the number of growth rates.
# Let N be the size of our search space.
# Technically, our search space is unbounded. we can assume the size of input search space is constant; and it is 1...MAX_VIABLE_POWER
# We do a 'try' operation by checking current value of t and performing the sum of g^t over all M -> O'(M)
# How many 'try' operations? our search space is bounded at first and continues to increase by a constant factor. 
# (this is called exponential search: first find a range that meets a condition; then binary search on that range)
# We do both binary and exponential search at the same time (which is a little bit slower than doing so separately)
# The cost of binary search is O(logN). We have to do how many binary searches until space is exhausted and range is amplified? 
# logN*O(logN)*O(M) = M(log(N))^2

# More efficiently, we can always double the hi pointer.
# Even more efficiently, duplicate our search space until we meet the condition f(t) > 1 billion. Until then, we binary search the space
# between last t and current t.  --> exponential search operation is done on space: 1...X where X is the first number that meets condition.
# To get there, our step to get there is multiplied by twice every time. So if we had to take N steps, then with exp search we are reducing 
# remaining distance by half. So its logN. Then, binary search also takes logM. where L is the size of range between t_i-1 and t_i.
# hence, overall complexity is logN*logL ? times the loop over the sum: logN*logL*M

def getBillionUsersDay(growthRates):
  # We can binary search for the first number of days
  # when we reach 1 billion users
  lo = 1
  hi = 100
  
  while lo <= hi:
    mid = lo + (hi-lo)//2
    # find sum of users at this day
    users = sum([r**mid for r in growthRates])  # can optimize space complexity by getting rid of this array and do a loop instead
    
    if users >= 10**9:
      hi = mid - 1
    else:
      lo += 1
      if lo > hi:  # push upper boundary upwards
        hi = hi*2
  
  return lo

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
  