from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = [] # list of triplets

        # For every number, find a pair of numbers in the remaining array
        # which sum to that number. AVOID DUPLICATES

        def twoSum(k, arr):
            # Appends to ans all pairs of numbers that add up to target: [target, a, b]
            # Assume array is sorted!
            print("twoSum", k, arr)
            target = -k
            l = 0
            r = len(arr) - 1

            while l<r:
                print("try", l, ":", r, end=" ->")
                s = arr[l] + arr[r]
                print("sum", s)

                if s == target:
                    sol = [k, arr[l], arr[r]]
                    print("found", sol)
                    result.append(sol)

                    # move left ptr to next diff number
                    l += 1
                    while l < len(arr)  and arr[l-1] == arr[l]:
                        l += 1
                    # move right ptr to next diff number
                    r -= 1
                    while r >= 0 and arr[r+1] == arr[r]:
                        r -= 1

                elif s < target:
                    # Increase l
                    l += 1
                else: # s > 0
                    # Decrease r
                    r -= 1
                
        nums.sort()
        print(nums)
        i = 0
        bound = len(nums) - 2

        while i < bound:
            twoSum(nums[i], nums[i+1:])
            i += 1
            while (i < bound and nums[i-1] == nums[i]):
                i += 1

        return result
    
nums = [1,-1,-1,0]

ans = Solution().threeSum(nums)
print(ans)
