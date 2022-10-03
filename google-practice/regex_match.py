# DOES NOT WORK

class Solution:
    """
    Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
        '.' Matches any single character.​​
        '*' Matches zero or more of the preceding element.
        The matching should cover the entire input string (not partial).
        It is guaranteed no consecutive * appear in string.
    """

    def findMatch(self, string, patt, i, j, c=None):
        # i <- current position in string
        # j <- current position in patt
        print("i", i)
        print("j", j)

        if i >= len(string) and j == len(patt):    # the string has been completely matched
            return True
        if j == len(patt):      # string could not match regex completely
            return False
        
        # check quantified c
        if c is not None:
            print("\t continue with ", c)
            if (c == "*" or string[i] == c) and self.findMatch(string, patt, i + 1, j, c):  # one or more
                return True            
            else:                                          # zero occurrences
                j += 1
                if j == len(patt): return False
                print("\t skip quantifier, new j -> ", patt[j+1])


        # quantified character match
        if patt[j].isupper() or patt[j] == "*":
            print("\t check any number of ", patt[j])
            return self.findMatch(string, patt, i, j, patt[j].lower())

        # single character match
        if patt[j] == string[i] or patt[j] == '.':
            print("\tmatch ", string[i], "in patt", patt[j])
            return self.findMatch(string, patt, i + 1, j + 1)

        print("\tno match")
        return False

    def isMatch(self, s: str, p: str) -> bool:
        # How to implement backtracking?
        # Try to match the regex with the given string.
        # Use recursion and backtracking.
        # When we have a *, try to match one char, then two, then three...
        # until a match is found.
        def compile(p):
            # Collapse any c* -> C. f c*c* then -> C. if .* then *
            def hasQuantifier(patt, j):
                if j + 1 < len(patt):
                    return patt[j+1] == '*'
                return False

            new_p = ""
            i = 0
            while i < len(p):
                if hasQuantifier(p, i):
                    quantified = p[i].upper() if p[i] != '.' else '*'  # encode .* into *
                    if len(new_p) > 0 and new_p[-1] == quantified:
                        pass
                    else:
                        new_p += quantified
                    i += 2
                else:
                    new_p += p[i]
                    i += 1
            return new_p

        # both s and p guaranteed non empty
        p = compile(p)
        print("compiled", p)
        return self.findMatch(s, p, 0, 0)


s = input("Enter s: ")
p = input("Enter p: ")
ans = Solution().isMatch(s, p)
print("Answer:", ans)
