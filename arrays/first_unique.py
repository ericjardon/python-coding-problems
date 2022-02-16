class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        seen = set()
        duplicated = set()     
        
        for c in s:
            if c in seen:
                duplicated.add(c)
            else:
                seen.add(c)
        
        for i, c in enumerate(s):
            if c not in duplicated:
                return i
        
        return -1