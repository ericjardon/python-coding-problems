def bSearch(arr, k, bounds=None):
    if not arr:
        return -1
    if bounds is None:
        lo = 0
        hi = len(arr) - 1
    else:
        lo, hi = bounds
    
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

def findPivot(arr, first):
    # returns the index of minimum element in shifted sorted array
    lo = 0
    hi = len(arr) - 1
    # Slight weakness is that we don't check the last pair. If no min is found, assume is the last index.
    while lo <= hi:
        mid = lo + (hi - lo)//2
        if mid == 0:
            return len(arr) - 1 # assume last index is min
        # Find the value whose predecessor is larger than it
        if arr[mid -1] > arr[mid]:
            return mid
        # Pair is in order.
        # If current value is greater than first, we are on the left side of shift
        # If current value is smaller than first, we are on the right side of shift
        elif arr[mid] < first:  # move left
            hi = mid
        else:                   # move right
            lo = mid + 1

    return -1

from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # the array is rotated if not (first < last)
        if len(nums) < 2:
            return 0 if target in nums else -1
    
        if not (nums[0] < nums[-1]):
            # Find pivot index. and bSearch in whichever half may contain target.
            pivot = findPivot(nums, nums[0]) # finds index of min number
            return max(bSearch(nums, target, (0, pivot-1)), bSearch(nums, target, (pivot, len(nums)-1)))
        else:
            return bSearch(nums, target)