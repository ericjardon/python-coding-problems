'''

'''

# My solution (times out, O(n^2))
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        def sumFromiToj(i,j,presum):
            if i==0:
                return presum[j-1]
            #print(f"{sumFromiToj(0,j,presum)} - {sumFromiToj(0,i,presum)}")
            return sumFromiToj(0,j,presum) - sumFromiToj(0,i,presum)
        
        N = len(nums)
        # Presum
        presum = [x for x in nums]
        for i in range(1, N):
            presum[i] = nums[i] + presum[i-1]
        
        #print("Presum:", presum)
        ans = 0
        for i in range(N):
            for j in range(i+1, N+1): # should always be greater than i
                s = sumFromiToj(i, j, presum)
                #print("i", i, "j", j, "equals", s)
                ans += 1 if s == k else 0
        
        return ans

# Faster solution
class Solution:
    from collections import defaultdict
    
    def subarraySum(self, nums: List[int], k: int) -> int:
        N = len(nums)
        accum = 0
        # A map counting how many times a cumulative sum has been reached in traversing the array
        sums = defaultdict(int)
        sums[0] = 1 
        # first cumulative sum is zero, before the first element
        
        count = 0
        for j in range(N):
            accum += nums[j]
            # a subarray that sums to k exists if sum[j] - sum[i] = k; 
            # hence we look for sum[i]: (sum[j] - k) 
            if accum - k in sums:
                count += sums[accum - k]