"""
In this case, * is <any> character <any> number of times.
"""
class Solution:
    def findMatch(self, string, patt, i, j):
        # i <- current position in string
        # j <- current position in patt

        if i >= len(string):  # the string has been completely matched
            return True
        if j >= len(patt):   # string could not match regex completely
            return False

        if patt[j] == "." or string[i] == patt[j]:
            return self.findMatch(string, patt, i + 1, j + 1)

        elif patt[j] == "*":
            # Zero or more characters until either is exhausted
            for positions in range(0, len(string) - i + 1):
                if self.findMatch(string, patt, i + positions, j + 1):
                    return True

        return False

    def isMatch(self, s: str, p: str) -> bool:
        # How to implement backtracking?
        # Try to match the regex with the given string.
        # Use recursion and backtracking.
        # When we have a *, try to match one char, then two, then three...
        # until a match is found.

        return self.findMatch(s, p, 0, 0)
