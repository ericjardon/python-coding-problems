from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        
        # Modularize: implement twoSum; A is sorted
        def twoSum(A, k, ans):
            l = 0
            r = len(A) - 1
            
            while l < r:
                s = A[l] + A[r]
                if s > k:
                    r -= 1
                    while r > 0 and A[r-1] == A[r]:
                        r -= 1
                elif s < k:
                    l += 1
                    while l < len(A)-1 and A[l+1] == A[l]:
                        l += 1
                else:
                    ans.append([A[l], A[r], -k])
                    l += 1
                    r -= 1
        
        ans = []
        nums.sort()
        i = 0
        N = len(nums)
        # careful with indexes
        for i in range(N-2):
            if nums[i+1] == nums[i]:
                continue
            k = 0 - nums[i]
            twoSum(nums[i:], k, ans)
                    
        return ans

ans = (Solution().threeSum([-1,0,1,2,-1,-4]))
print(ans)