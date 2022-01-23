'''
Given two strings s and t of length N, find the maximum number of possible matching pairs in strings s and t after swapping exactly two characters within s.
A swap is switching s[i] and s[j], where s[i] and s[j] denotes the character that is present at the ith and jth index of s, respectively. The matching pairs of the two strings are defined as the number of indices for which s[i] and t[i] are equal.
Note: This means you must swap two characters at different indices.

'''

import math
# Add any extra import statements you may need here
from collections import defaultdict

# Add any helper functions you may need here


def matching_pairs(s, t):
  # Count number of matching pairs
  
  # Get indexes for every character
  # Find indexes where there is a mismatch
  
  # If there are zero mismatches, we must check everything
  N = len(s)
  matches = set()
  mismatches = set()
  indexes_s = defaultdict(list)
  for i in range(N):
      if s[i] != t[i]:
        mismatches.add(i)
      else:
        matches.add(i)
        
      indexes_s[s[i]].append(i)
    
  # Can we swap to gain a match?
  for mx in mismatches:
    target = t[mx]
    # find an index j : s[j] == t[mx] and t[j] == s[mx]
    for j in indexes_s[target]:
      if t[j] == s[mx]:
        # We can swap and get matches + 2 if j is in mismatches, +1 otherwise
        return len(matches) + (2 if j in mismatches else 1)
  
  # Can we swap to stay the same?
  # a) swap mismatches
  if len(mismatches) > 1:
    # swap two mismatches between them
    return len(matches) 
  
  # b) swap repeated characters between them
  for i in matches:
    if len(indexes_s[s[i]]) > 1:
      # Can swap same character with its own
      return len(matches)

  
  # Less than two mismatches: cannot swap without losing a match
  return len(matches) - 2 + len(mismatches)
  
  



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
  s_1, t_1 = "abcde", "adcbe"
  expected_1 = 5
  output_1 = matching_pairs(s_1, t_1)
  check(expected_1, output_1)

  s_2, t_2 = "abcd", "abcd"
  expected_2 = 2
  output_2 = matching_pairs(s_2, t_2)
  check(expected_2, output_2)

  # Add your own test cases here
  