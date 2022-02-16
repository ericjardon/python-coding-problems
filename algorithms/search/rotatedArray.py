'''
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
'''

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Find pivot index k with binary search: first elem larger than nums[-1]
        if not nums: return -1
        # Largest element should be nums[-1]
        biggestElem = nums[-1]
        
        if target == biggestElem: return len(nums) - 1 
        
        lo = 0
        pivot = len(nums) - 1
        
        while lo <= pivot:    # loobiggestElem for first val x < biggestElem
            mid = lo + (pivot - lo)//2
            if nums[mid] <= biggestElem:
                # search in lower half
                print("Search in lower half")
                pivot = mid - 1
            else:
                print("Found elem bigger than", biggestElem)
                # push left bound up
                lo = mid + 1
        
        # lo and pivot will cross each other in two scenarios
        # a. lo pushed up: pivot still holds the index previous to last element smaller than biggestElem
        # b. pivot crossed lo: means we moved left until finishing the array

        print("pivot index", pivot)
        if pivot == -1:
            lo = 0
            pivot = len(nums) - 1
            # Normal binary search
        else:
            # check ranges
            if nums[0] <= target <= nums[pivot]:
                print("target to the left of pivot")
                lo = 0
                hi = pivot
            else:
                print("target to right of pivot")
                lo = pivot + 1
                hi = len(nums) - 1
        
        print("Search in array", lo, hi)
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if  target < nums[mid]:
                # search in lower half
                hi = mid - 1
            elif target > nums[mid]:
                lo = mid + 1
            else:
                # push left bound up
                break
        
        if lo > hi: 
            print("array exhausted")
            return -1
        
        return mid
        
                
target = 3
nums = [3,1]
        
Solution().search(nums, target)