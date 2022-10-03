def numBits(n): # O(logN)
    # Find the minimum power of 2 that is larger or equal to N.
    if n < 2:
        return 1

    for i in range(n+1):
        if 2**i > n:
            return i

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = 10**9 + 7        
        # f(n) is f(n-1) * 2 ** offset + n
        # Can we do dp? this problem scream tabulation
        
        if n == 1:
            return 1
        
        # dp = [-1 for _ in range(n+1)] # MLE, careful. Use instead two slots!
        prev = 1
        curr = None
        # dp[1] = 1
        # dp[2] = 6
        
        for i in range(2, n+1):
            offset = numBits(i)
            # Multiply previous result by 2**number of bits needed for n
            curr = (prev * 2**offset) + i
            prev = curr # i+1
        
        return curr%MODULO
        # TIME LIMIT EXCEEDED. Improve numbits?

## Make it better
class Solution2:
    def concatenatedBinary(self, n: int) -> int:
        MODULO = 10**9 + 7        
    
        if n == 1:
            return 1
        ans = 1
        # dp[1] = 1
        # dp[2] = 6
        
        for i in range(2, n+1):
            offset = i.bit_length()
            # Multiply previous result by 2**number of bits needed for n
            ans = (ans * 2**offset) + i

        return ans%MODULO
        # still stupid slow. WHY?