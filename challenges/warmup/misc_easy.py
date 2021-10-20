#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    ampm = s[-2:]
    
    h, m, s = s[:-2].split(":")
    
    if ampm=="PM":
        if int(h) != 12:
            h = str(int(h)+12)
        return ":".join([h,m,s])
                    
    if h=="12":
        h = "00"
    
    return ":".join([h,m,s])
    

# if __name__ == '__main__':
#     #fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     s = input()

#     result = timeConversion(s)
#     print(result)


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    nums = set(a)
    seen = set()
    for n in a:
        if n in seen:
            nums.remove(n)
        else:
            seen.add(n)
    
    return nums.pop()
    

def diagonalDifference(arr):
    '''returns the absolute difference between the sum of the
        diagonals of a square matrix'''
    n = len(arr)
    diag1 = sum([arr[i][i] for i in range(n)])
    diag2 = sum([arr[i][n-i-1] for i in range(n)])
    
    return abs(diag1-diag2)
    

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)
    print(result)
