import math
# Add any extra import statements you may need here


# Add any helper functions you may need here

# With Sliding Window Technique we can achieve this in O(N) time
def min_length_substring(s, t):
  
  # Edge cases
  if len(t) > len(s): return -1
  
  # Create counter for s and t
  chars_s = set(s)
    
  required = {}
  for c in t:
    if c not in chars_s: return -1  # early stop
    required[c] = required.get(c,0) + 1
    
  # Sliding Window
  n_chars_left = len(required)  # unique characters to match
  l = 0
  r = 0  # window length is l,r inclusive
  
  min_length = len(s)+1
  
  # required tells us the required characters contained in our substring
  while r < len(s):
    # Extend window: r pointer forward
    c = s[r]
    if c in required:  # required[r] tells us how many chars of r we are missing
      required[c] -= 1
    
      if required[c] == 0:  # we have all occurrences of c we need
        n_chars_left -= 1
    
    
    if n_chars_left == 0:  # we found a substring
      print("found", s[l:r+1])
      min_length = min(min_length, r-l+1)
      
    # Reduce window: l pointer forward
    # if substring found, trim non-required chars from the left
    while n_chars_left == 0:
      c_ = s[l]
      if c_ in required:
        required[c_] += 1
        
        if required[c_] > 0:
          n_chars_left += 1
          # annotate new window length
          print("reduced", s[l:r+1])
          min_length = min(min_length, r-l+1)
      l += 1
          
    
    r += 1
  
  return -1 if min_length > len(s) else min_length
  

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

#   s1 = "dcbefebce"
#   t1 = "fd"
#   expected_1 = 5
#   output_1 = min_length_substring(s1, t1)
#   check(expected_1, output_1)
  
#   s2 = "adobecodebanc"
#   t2 = "abc"
#   expected_2 = 4
#   output_2 = min_length_substring(s2, t2)
#   check(expected_2, output_2)

#   s2 = "nonenonenonenone"
#   t2 = "neo"
#   expected_2 = 3
#   output_2 = min_length_substring(s2, t2)
#   check(expected_2, output_2)

#   s2 = "afjddlbsnlskc"
#   t2 = "abc"
#   expected_2 = len(s2)
#   output_2 = min_length_substring(s2, t2)
#   check(expected_2, output_2)

#   s2 = "eeeeeeeeeeeeeeeeeeee"
#   t2 = "abc"
#   expected_2 = -1
#   output_2 = min_length_substring(s2, t2)
#   check(expected_2, output_2)
  
  s2 = "xyzzzzefhfhfzebrazz"
  t2 = "zzzebra"
  expected_2 = len(t2)
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

  # Add your own test cases here
  