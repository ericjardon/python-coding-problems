'''
You are given two strings s and t. 
You can select any substring of string s and rearrange the characters of the selected substring. 
Determine the minimum length of the substring of s such that string t is a substring of the selected substring.
'''
import math
# Add any extra import statements you may need here
from collections import Counter

# Add any helper functions you may need here
def checkSubstr(chars_s, chars_t):
  # Receives two counter dictionaries
  for c, count in chars_t:
    if c not in chars_s or chars_s[c] < count:
      return False

  return True

def updateRemaining(chars_t, total, added=None, removed=None):
  if added and added in chars_t and chars_t[added]>0:  # number of characters remaining to fill
    chars_t[added] -= 1
    total -= 1
  if removed and removed in chars_t:  # update count for a character we removed for substring
    chars_t[removed] += 1
    total += 1
  return total

def min_length_substring(s, t):
  # Substring in s can be rearranged however we want
  # find a function that returns true when t is a substring of s
  
  # Objective: to achieve at least same occurrences of t in our substring s
  # s must be as small as possible, so it is at least of length len(t)
  # t is a recipe of (characters->count) that we must match
  
  N = len(s)
  min_l = len(t)
  if min_l==1:
    return 1 if t in s else -1
  
  print("S length", N)
  print("T length", min_l)
  if N < min_l: return -1
  
  # For every possible substr length, 
  # for every possible start index
  # keep track of the characters in our substring that meet those in t
  
  for length in range(min_l, N+1):
    
    chars_t = Counter(list(t))  # target we must meet in our substring
    total = len(t) # number of characters to meet
    for c in s[:length]:
      total = updateRemaining(chars_t, total, added=c) # substract characters we already have
      
    if total <= 0: 
      return length
    
    for start_i in range(1, N-length):
      # Moving window of length min_l
      #print(f"subs [{start_i},{start_i+length - 1}]")
      substring = s[start_i:start_i+length] 
      #print(" ",substring)
      
      updateRemaining(chars_t, total, added=s[start_i+length-1], removed=s[start_i-1])
      
      if total <= 0: 
        return length
      
  return -1

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
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  s2 = "murxxxxxxcielassssssssssgo"
  t2 = "murcielago"
  expected_2 = len(s2)
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  s2 = "gogogo"
  t2 = "og"
  expected_2 = 2
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)
  
  s2 = "understatement"
  t2 = "n"
  expected_2 = 1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  