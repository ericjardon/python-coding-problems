# Given an array of n integers, find if there are 3 distinct elements such that
# a + b + c = 0 and return all such triplets.
from typing import List
# Note since you need all possible triplets, you can do an exhaustive search.
# The catch is to only include in answer no duplicate triplets

# how do we avoid duplicate triplets? keep track of triplets already added.
# identify a triplet's identity by its initial pair of smallest two numbers.
def threeSum(nums: List[int]) -> List[List[int]]: # solution is O(n^3)
    if len(nums) < 3:
        return []
    sol = list()
    seen = set()
    for a in range(len(nums)):
        for b in range(a+1, len(nums)):
            curr = [nums[a], nums[b]] if nums[a] < nums[b] else [nums[b], nums[a]]
            for c in range(b+1, len(nums)):
                print(nums[a],"+",nums[b],"+", nums[c],"=", nums[a] + nums[b] + nums[c])
                if nums[a] + nums[b] + nums[c] == 0:
                    if nums[c] < curr[0]:
                        key = (nums[c],curr[0])
                    elif nums[c] > curr[-1]:
                        key = (curr[0], curr[1])
                    else:
                        key = (curr[0], nums[c])
                    if key not in seen:
                        seen.add(key)
                        sol.append([nums[a], nums[b], nums[c]])
    return sol
## SOLUTION IS TOO SLOW!!! DEVELOP A ONE-PASS SOLUTION

def threeSum_fast(nums:List[int]) -> List[int]:
    # For every distinct value in the array, perform two-sum. A-HA!
    if len(nums) < 3:
        return []
    ans = list()
    vals = set()
    answered = set()        # holds every value that has been used for any triplet.

    def twoSum(i: int, target: int):
        # searches in the subarray starting at i+1 for the indices of the two numbers that add up to target
        print(", find two Sum of ",target,"from index", i+1)
        seen = set()       # dictionary of values val: index
        for j in range(i+1, len(nums)):
            print("current:", nums[j])
            seen.add(nums[j])
            comp = target - nums[j]
            if comp in seen:     # nums[j], nums[seen[comp]] and nums[i] are a valid triplet, check if it has not been used yet
                print("possible",nums[i], "+",comp,"+", nums[j],"=0")
                print("complement",comp," in seen")
                if nums[i] in answered and nums[j] in answered and comp in answered:        # does not work. Three different triplets' elements could 'make' one triplet
                    print("current triplet already answered")
                    continue
                answered.add(nums[i])
                answered.add(nums[j])
                answered.add(comp)
                print("add triplet:", [nums[i], comp, nums[j]])
                ans.append([nums[i], comp, nums[j]])
            else:
                print("next")


    for i in range(len(nums)-2):
        if nums[i] not in vals:
            print("New val:",nums[i], end=" ")
            vals.add(nums[i])
            twoSum(i, -nums[i])     # find two numbers that added up equal the negative value of nums[i]
    return ans


nums = [-1,0,1,2,-1,-4,3,7,1,6,-9,1,-2,-10,1]       # failds to find all
#nums = [3,0,-2,-1,1,2]
print("Res",threeSum_fast(nums))


from math import factorial
def nchoosek(n,k):
    return factorial(n) / (factorial(k)*factorial(n-k))
