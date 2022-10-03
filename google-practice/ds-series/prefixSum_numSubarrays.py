from collections import defaultdict
from pprint import pprint
"""
Given an integer array return the total number of contiguous subarrays
that add up to a target number k.
You must provide a solution that is O(N) and constant space.
"""

def numSubarrays(list: list[int], k: int) -> int:
    N = len(list)

    # without prefix sum array
    ans = 0
    currSum = 0

    # Keep track of seen prefix sums (continuous sums from up to i)
    seen_sums = defaultdict(int) 
    seen_sums[0] = 1     # Lower bound: a sum of 0 is considered to have been "seen"
    print(list)
    print("k=",k)
    for num in list:
        currSum += num
        # If there exists a prefix sum currSum - k, 
        # it means there is a rightmost subarray that sums to k
        # since subArrayWithPrefix(x-k) + subArrayWithPrefix(k) = subArrayWithPrefix(currSum)
        complementSum = currSum - k
        print("--current Sum", currSum)
        print("currsum - k:", complementSum)
        print("seen times:", seen_sums[complementSum])
        ans += seen_sums[complementSum] # adds 0 if not seen
        print("ans now", ans)
        seen_sums[currSum] += 1 # increment counter of arrays having prefix of currSum.
        # different contiguous subarrays may add to currSum if we allow 0s or negative vals. 

    # Effectively we traverse the array once
    # we keep track of the number of subarrays that add up to a sum using a seen_sum counter
    # At every prefix sum, substract k and see if there are previous arrays that
    # add up to that sum (sum-k). Each of these end in an index less than i, call it i*. 
    # For every subarray adding up to (sum-k) that starts at 0 and ends in i*,
    # there is a rightmost part of that subarray starting at i*, ends at i that equals k
    return ans

# TES CASES
# print("ans", numSubarrays([1,0,1,1,0], 2)) # expect 5
# print("ans", numSubarrays([1,-2,2,1,-1], 2)) # expect 3
