
"""Given two sorted arrays of size m and n respectively. Return the median of both.
    Challenge: The runtime complexity should be log(m+n)
    m, n are both between 0 and 1000, m+n are always larger than 1"""

from typing import List

# O(n+m) Solution
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    # Merge the array and return the middle position if len%2==1.
    # else, return the average between the n//2 and n//2+1 positions
    n = len(nums1)
    m = len(nums2)
    merged = [0 for _ in range(n+m)]
    i, j, k = 0, 0, 0
    while (i < n and j < m):
        if nums1[i] < nums2[j]:
            merged[k] = nums1[i]
            i += 1
        else:
            merged[k] = nums2[j]
            j+=1
        k += 1

    while (i < n):
        merged[k] = nums1[i]
        i += 1
        k += 1
    while (j < m):
        merged[k] = nums2[j]
        j += 1
        k += 1

    if (n+m)%2==1:
        return merged[(n+m)//2]
    else:
        return ( merged[(n+m)//2] + merged[(m+n)//2 - 1] )/2.0


# O(log(n+m)) Solution:
    # Since we want a log algorithm, that basically means we are somehow applying binary search.
    # What are we searching for? the point of partition that separates the total number of elements
    # in equal halves & maintains sorted order.

def findMedianLog(nums1: List[int], nums2: List[int]) -> float:
    # We do not need to merge both arrays. We can find the value that separates the theoretically merged array in equal halves.
    # We do this by estimating a halfway value using binary search on the shorter array.
    if len(nums2) < len(nums1):
        nums1, nums2 = nums2, nums1     # we want nums1 to be the shorter one
    totLen = len(nums1) + len(nums2)
    half = totLen // 2
    lo, hi = 0, len(nums1)-1
    while True:
        # Find mid indices in both arrays
        mid1 = lo + (hi-lo)//2      # calculate midpoint avoiding overflows
        mid2 = half - (mid1+1) - 1  # based on remaining items of total half after substracting items in nums1 partition

        # Get the values that separate the partition in each array
        left1 = nums1[mid1] if mid1>-1 else float("-inf")                # if left elem is out of bounds default to a min val
        left2 = nums2[mid2] if mid2 > -1 else float("-inf")
        right1 = nums1[mid1+1] if mid1 < len(nums1) else float("inf")    # if right elem is out of bounds, default to max value
        right2 = nums2[mid2+1] if mid1 < len(nums1) else float("inf")

        if left1 <= right2 and left2 <= right1:     # partition is correct, all elems in left are smaller than elems on right
            if totLen%2:   # Odd number of elements
                return min(right1, right2) # the true middle is the smaller element of the two on the right
            else:          # Even number of elems, average the middle two elems
                return (max(left1, left2) + min(right1, right2)) / 2.0      # larger of the left ones is adjacent to the smaller of the right ones

        elif left1 > right2:    # need less elements from array 1 -> move midpoint backward
            hi = mid1-1
        else:                   # left 2 may be larger than right 1, we need more elems for array1 -> move midpoint forward
            lo = mid1+1