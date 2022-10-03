"""
Given an array of integers, 
find the longest CONTIGUOUS subarray 
where the absolute difference between any two elements 
is less than or equal to 1.

Return the length of longest subarray.
"""
from typing import List

def pickingNumbersContiguous(a: List[int]):
    # sliding window
    # keep a pointer to the beginning of subarray
    # extend as far as the subarray is valid or when wen reach EOD.
    # when we reach an invalid number, update starting pointer accordingly
    # pointer should move to the first element in the array that is within the new 
    # number's range. How do we move start_i accordingly?
    # we can push start_i forward until new number is valid.
    # In the worst case, we will make 2N pushes for an N length array
    if len(a) < 2:
        return len(a)
    
    maxLen = 1
    start_i = 0
    end_i = 0

    # when an array is len 2, it can accept more values on either end. If it has 3, it is locked.
    def validSubArray(lo, hi, val):
        range = abs(hi - lo)
        if range == 2:
            return lo <= val <= hi
        elif range < 2:
            return abs(hi - val) < 2 and abs(lo - val) < 2
        else:
            raise Exception("subarray range > 2")

    hi = a[0]
    lo = a[0]
    while start_i < len(a):
        end_i = start_i
        # While the absolute difference in subarray is still 1 
        while end_i < len(a) and validSubArray(lo, hi, a[end_i]):
            maxLen = max(maxLen, end_i - start_i + 1)
            lo = min(lo, a[end_i])
            hi = max(hi, a[end_i])
            
# =========== PICKING NUMBERS 2: NON-CONTIGUOUS ARRAYS

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#
from collections import defaultdict

def pickingNumbers(array):
    # Subarray need not be contiguous
    # Keep a map of "pairs", 
    # where key x represents the closed interval x and x+1
    # and value is the number of instances in the array
    # For every value we encounter, update both x and x+1 counts.
    
    counts = defaultdict(int)
    
    for val in array:
        counts[val] += 1
        counts[val+1] += 1
    print(counts)
    return max(counts.values())
        

