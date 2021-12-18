'''
Given a sorted array ``digits`` 
you can write numbers using any digit as many times as you want. 
Given an upper limit integer N.

Return the number of positive integers that can be generated that are less than or equal to N.
'''
from typing import List
from functools import cache

# @cache
# def fact(x):
#     if x < 2:
#         return 1
#     return x * fact(x-1)

# def nChooseK(n, k): # if there were no repetition
#     return 1.0* fact(n) / (fact(k) * fact(n-k))

class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        # https://leetcode.com/problems/numbers-at-most-n-given-digit-set/solution/
        pass    

    def atMostNGivenDigitSetEric(self, digits: List[str], n: int) -> int:
        # A simple hack: comparison between string digits (digit chars)
        if digits == []:
            return 0
        _digits = digits

        # decompose n into its digits 
        rem = n
        n_digits = []
        while rem>0:
            rem, last_digit = divmod(rem, 10)
            n_digits.append(last_digit)

        n_digits = n_digits[::-1]
        max_d = len(n_digits)

        digits = [int(x) for x in digits]

        ans = 0

        # --- Permutations for numbers with less digits
        for num_length in range(max_d-1, 0, -1):
            ans += len(digits)**num_length
        print("With less digits", ans)
        
        
        # --- Permutations for numbers with same number of digits
        
        # When leading digit < leading digit of n
        i = len(digits) - 1
        while i > -1 and int(digits[i]) >= n_digits[0]:
            i -= 1
        # 
        print(f"{i+1} digits are smaller than leading digit of n: {n_digits[0]}")
        if (i+1):
            print("With smaller leading digit", (i+1) * (len(digits)**(len(n_digits) - 1)))

            ans += (i+1) * (len(digits)**(len(n_digits) - 1))

        else:
            print("With smaller leading digit", 0)

        # When same leading digits. 
        if n_digits[0] in digits:
            # We can write numbers with same digit at starting position as n
            possible = 1
            # How many digits can we place at every other position? 
            # When Only up to the real digit in n
            for position in range(1, len(n_digits)):
                d = 0
                while d < len(digits) and digits[d] <= n_digits[position]:
                    d += 1
                possible *= d  # d digits can be placed at position
            print("With same leading digit", possible)
            ans += possible
                
        return ans
        # For some intractable reason, last input is incorrect


digits = ["1","3","5","7"]; n = 100
digits = ["1","4","9"]; n = 1000000000
digits = ["7"]; n = 8
digits = ["1", "2", "3"]; n = 21 
digits= ["1","2","3","4","6","7","9"]; n=333  # expected: 171

x = Solution().atMostNGivenDigitSetEric(digits, n)
print(x)