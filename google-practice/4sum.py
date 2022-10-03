from typing import List

def movePointer(l, r, nums, from_left):
    # Moves to next value different than current.
    # Assumes l, r within range. Assumes l > 0
    if from_left:
        val = nums[l]
        l += 1
        while l < r and nums[l] == val:
            l += 1
        return l
    else:
        val = nums[r]
        r -= 1
        while l < r and nums[r] == val:
            r -= 1
        return r

class Solution:
    # We don't care about indexes, since all 4-tuples need to be distinct
    # We can sort everything and start on values that are new.
    ans = []

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.ans = []
        nums = sorted(nums)
        if len(nums) < 4:
            return []
        
        self.findNSum(nums, 0, 4, [], target)

        return self.ans

    def findNSum(self, nums: List[int], index: int, n: int, partial: List[int], target: int):
        if n > 2: # n to sum
            # print("N to sum", n, "partial", partial)
            val = None
            for i in range(index, len(nums) - (n-1)): # find first unique value
                if nums[i] == val:
                    continue
                else:
                    val = nums[i]
                
                k = target - val

                self.findNSum(nums, i + 1, n - 1, [val] + partial, k)
        else:
            # print("N to sum 2, partial", partial)
            l = index
            r = len(nums)-1
            # Search the remaining array
            # print("start l", l)
            # print("start r", r)
            while l < r:
                # # print("s =", nums[l],"+",nums[r])
                s = nums[l] + nums[r]

                if s > target: # s should decrease
                    # move r to the left
                    r = movePointer(l, r, nums, False)
                elif s < target: # s should increase
                    # move l to the right
                    l = movePointer(l, r, nums, True)
                else:
                    self.ans.append(partial + [nums[l], nums[r]])
                    l += 1
                    r -= 1

x = Solution().fourSum([2,2,2,2,2], 8)
print(x)
x = Solution().fourSum([1,0,-1,0,-2,2], 0)
print(x)

# FAILS WITH 
# [1,2,3,4,1,2,3,4,1,3,4,2], 10