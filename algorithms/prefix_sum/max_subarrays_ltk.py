'''
Given an array of positive integers A
Given a positive integer k
Find the maximum size Z of subarray, such that all
subarrays of size Z have a sum of elements lte to k.
'''

# Naive approach is to test all possible sizes 1..N
# Since all elements are positive, prefix subarray is strictly increasing.
# Instead of traversing sequentially the range, we can do binary search

def bSearchForSize(prefixSum, n, k):
    '''Perfomrs binary search on possible subarray sizes 1..N
        Returns the biggest size Z such that all subarrays of 
        size Z have sums less than k'''
    ans = -1 # target to maximize (biggest size of subarray)

    def subarraySum(start, end):
        '''Computes the sum of the subarray ranging from start 
            to end-1 indices in original array'''
        return prefixSum[end] - prefixSum[start]
    
    left = 1
    right = n
    while left <= right:
        size = (left+right)//2 # middle index

        # For every subarray of this size
        for end_i in range(size, n+1):
            # displace starting and ending indices. 
            start_i = end_i - size
            if subarraySum(start_i, end_i) > k:
                end_i -= 1
                break
        end_i += 1
        if (end_i == n+1):
            # all subarray sums are less than k
            # we can try bigger size in upper half
            left = size+1
            ans = size
        else:
            # subarray sum exceeds k
            # look for smaller size in lower half
            right = size - 1
    
    return ans

def prefixSumOf(A):
    n = len(A)
    prefix = [0 for _ in range(n+1)]
    for i in range(n):
        prefix[i+1] = prefix[i] + A[i]
    return prefix


def findMaxSizeUnderK(A, n, k):
    """Returns the maximum subarray size Z,
    such that all subarrays of size Z have sum
    less than k"""
    prefixSum = prefixSumOf(A)
  
    # Perform binary search of size k among range 1..n
    return bSearchForSize(prefixSum, n, k)

A = [1, 2, 10, 4]
n = len(A)
k  = 14
# ans is 2
print(findMaxSizeUnderK(A, n, k))


# [1,2,3,4,5,6]
# should be an extra space
# [0,1,3,6,10,15,21]

# if we add extra elem in front, we must add to end
# sum(1,3) = [2,3,4] = psum[end+1] - psum[start] = psum[4] - psum[1] = 10-1=9
# sum(0,0) = [1] = psum[0+1] - psum[0] = 1 - 0 = 1

# sum(5,5) = [6] = psum[6] - psum[5] = 21 - 15 = 6