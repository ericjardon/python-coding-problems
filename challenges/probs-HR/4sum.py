



def fourSum(nums, target):
    """Solution passing pointers instead of slices"""
    def recurseSum(nums, i_start, k, ans_so_far, N_to_sum, results):
        if (len(nums)-i_start) < N_to_sum or N_to_sum < 2 or k < nums[0]*N_to_sum or k > nums[-1]*N_to_sum:  
            return
        if N_to_sum == 2:
            left, right = 0, len(nums) - 1
            while left < right:
                # If we found target
                if nums[left] + nums[right] == k:
                    results.append( ans_so_far + [nums[left], nums[right]] )
                    left += 1
                    right -= 1
                    # Skip repeated values
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while right > left and nums[right] == nums[right+1]:
                        right -= 1
                    # left and right could converge to the same index

                elif nums[left] + nums[right] < k:  # increase smaller term
                    left += 1
                else:   # decrease larger term
                    right -= 1
        
        else: # cases N>2
            for i in range(i_start, len(nums) - N_to_sum + 1):
                # For every unique starting value
                if i==0 or (i>0 and nums[i-1] != nums[i]):
                    # add to answer so far
                    recurseSum(nums, i+1, k-nums[i], ans_so_far+[nums[i]], N_to_sum-1, results)
    
    results = []
    nums = sorted(nums)
    recurseSum(nums, 0, target, [], 4, results)
    return 


### challenge: can you make it iterative?


#### LEGACY ANSWER: USING A COUNTER DICTIONARY OF TALLIES OF EVERY CHARACTER, BUT RETURNS REPEATED ANSWERS

from typing import List
from collections import Counter
class TallySolution:
    def twoSum(self,tally, k):
        # Given an array of nums, possibly repeated,
        # return all the unique pairs that add up to k
        answers = []
        seen = set()
        for val in tally.keys():
            complement = k - val
            if complement not in seen and complement in tally:
                if val != complement and tally[val] > 0 \
                    or val == complement and tally[val] > 1:
                    seen.add(val)
                    answers.append([val, complement])

        # The answers returns can be appended to any caller who is loking for k = val+complement
        return answers

    def threeSum(self,tally, k):
        answers = []
        seen = set()
        for val in tally.keys():
            # For every remaining value
            if tally[val] > 0:
                tally[val] -= 1 # take this val   
                complement = k - val  # find if complement exists as 2Sum with remaining tally  
                if complement not in seen:      
                    for pairs in self.twoSum(tally, complement):
                        # for every possible pair adding up to complement, create an answer for 3Sum
                        if pairs[0] in seen:
                            answers.append([val] + pairs)

                # place this value back
                tally[val] += 1
        return answers

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        tally = Counter(nums)
        answers = []
        for val in tally.keys():
            tally[val] -= 1 
            complement = target - val
            for triplets in self.threeSum(tally, complement):
                answers.append([val] + triplets)
            tally[val] += 1
        
        return answers
            
if __name__=="__not_main__":
    #s = Solution.fourSum()
    test3 = [2,2,2,2,5,1,-7,1,15]
    target3 = 8

    test2 = [1, 3, 1, -4, 0, 8,1,1,1,1,1,1,1,1,1,1]
    target = 4
    t = Counter(test2)
    print(TallySolution().threeSum(t, target))



### 
# https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)




### GENERALIZED 2SUM: answer not my own

def findNSum(nums, target, N, result, results):
    '''
    Recursive generalized N sum, reducing N every time, and slicing array
    results are accumulated in a shared array.
    nums: a sorted list of numbers
    results: pass by reference array that stores the global list of results.
    target: the value for which to find an Nsum
    result: the accumulated sum up to now
    '''

    # Base cases: if no more numbers to use or we reach 1Sum
    if len(nums) < N or N < 2: return

    # Early termination
    if target < nums[0]*N:  
        # any possible N sums onward exceed target
        return
    if target > nums[-1]*N:
        # largest value is not enough to reach target
        return
    
    # Normal 2-sum: two pointer approach w/sorted array
    if N == 2:
        left, right = 0, len(nums) - 1
        while left < right:
            # If we found target
            if nums[left] + nums[right] == target:
                results.append( result + [nums[left], nums[right]] )
                left += 1
                right -= 1
                # Skip repeated values
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while right > left and nums[right] == nums[right+1]:
                    right -= 1
                # left and right could converge to the same index

            elif nums[left] + nums[right] < target:  # increase smaller term
                left += 1
            else:   # decrease larger term
                right -= 1
        
    # For all other cases N>2
    else:
        # For every value up to the i-N position (we may stop earlier)
        for i in range(0, len(nums) - N + 1):
            
            if i==0 or \
                i > 0 and nums[i-1] != nums[i]:
                # if we've just started or value nums[i] is seen for the first time
                remainingNums = nums[i+1:]  # our search space is reduced
                newTarget = target - nums[i]
                resultSoFar = result + [nums[i]]
                findNSum(remainingNums, newTarget, N-1, resultSoFar, results)
        # every possible answer starts with a different 
        # value in the array so we guarantee uniqueness

# To solve 4-Sum:
results = []
nums = [int(x) for x in input().split()]
target = int(input("target:"))
findNSum(nums=sorted(nums), target=target, N=4, result=[], results=results)
print( results )