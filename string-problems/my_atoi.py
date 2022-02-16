from math import ceil

class Solution:
    MAX_INT = 2**31 - 1
    MIN_INT = -(2**31)
    
    def myAtoi(self, s: str) -> int:
        N = len(s)
        i = 0
        # Ignore whitespace
        while i <  N and s[i] == ' ':
            i += 1
        
        if i >= N: return 0
        
        if s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else 1
            i += 1
        else:
            sign = 1
        
        # Incrementally build the integers
        ans = 0
        
        while i < N and s[i].isnumeric():
            # check overflow
            d = int(s[i])
            if (ans > self.MAX_INT // 10) or (ans == self.MAX_INT//10 and d > 7):
                return 2**31 - 1
            if (ans < ceil(self.MIN_INT / 10) or (ans == ceil(self.MIN_INT/10) and d > 8)):
                return -(2**31)
            
            ans *= 10
            ans += d*sign
            i += 1
        
        return ans
        
            
        
        