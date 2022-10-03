from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return max(nums)
        # We should do a traversal by robbing first house and not.
        dp = [-1] * len(nums)
        dpSkip = [-1] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        dpSkip[0] = 0
        dpSkip[1] = nums[1]

        # Every element except the last one
        for i in range(2, len(nums) - 1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            dpSkip[i] = max(dpSkip[i-1], dpSkip[i-2] + nums[i])

        dpSkip[-1] = max(dpSkip[-2], dpSkip[-3] + nums[-1])

        return max(dp[-2], dpSkip[-1])
    
# With path: 2,4,6,8,10,12,14 we get a max!
# problem is we have to force skipping first one
nums = [1,1,3,6,7,10,7,1,8,5,9,1,4,4,3] 
print(Solution().rob(nums))