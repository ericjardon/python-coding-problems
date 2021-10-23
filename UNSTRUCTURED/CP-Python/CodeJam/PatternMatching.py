"""
Pattern: a string consists of uppercase & asterisks (*) meaning 'any string'.
Name: a string consists of only uppercase letters.

Pattern matches a Name if you can replace every asterisk with any string
and obtain m.

Given N patterns of which at least 1 character is an english letter,
can you find one name that matches all of the patterns?
If it is not possible report so.
"""
## TEST SET 1: Only one (*) for each Pi, i.e. the leftmost.
class TestSet1:
    def readPatterns(self, N):
        P = []
        for _ in range(N):
            P.append(input())
        return P

    def matchPatterns(self, P):
        P.sort(key=lambda x: len(x))
        # nlogn operation could be linear if we just pick largest
        w = P[0]
        for i in range(1, len(P)):
            commonidx = len(P[i]) - len(w) + 1
            print(P[i][commonidx:], "==", w[1:])
            if P[i][commonidx:] != w[1:]:
                return '*'
            w = w.replace('*', P[i][:commonidx])
            print("w=", w)
        return w[1:]

    def main(self):
        for tcase in range(int(input())):
            P = self.readPatterns(int(input()))
            w = self.matchPatterns(P)
            print("Case #{}: {}".format(tcase + 1, w))
# This problem forces the answer to have a certain, fixed suffix.
# We check whether the patterns introduce any conflicting requirements for it.
# Pick the largest suffix of the N patterns. There exists a valid answer if and only if
# all the other suffixes are itself suffixes of L. (L is itself a suffix of L).
# Check every other string against L, starting at the end of both and stepping backwards,
# until we find a discrepancy or run out of letters. IF there is ever a discrepancy,
# there is no answer. Otherwise, we know that L itself is the shortest possible answer.

## TEST SET 2: Exactly one character, is an asterisk. Any index
class TestCase2:
    """We can divide the given patterns in 3 subsets:
    1. Start with asterisk -- require a fixed suffix
    2. End with asterisk -- require a fixed prefix
    3. Asterisk in the middle -- both of these requirements
    We can split the problem into the suffix requirement and prefix requirement.
    Then, apply the strategy from TestSet1: Once for prefix constraints,
    Another for the suffix constraints. If you concatenate both results
    you get the General result. """
    def findMaxLen(self, strings):
        max = ""
        for s in strings:
            if len(s) > len(max):
                max = s
        return max

    def fixedPrefix(self, endPatts, middlePatts):
        # transform middlePatts into endPatts -> trim all after *
        middlePatts = [p.split('*')[0] for p in middlePatts]    # remove asterisks
        endPatts.extend(middlePatts)
        print("Extended endpatts:", endPatts)
        L = self.findMaxLen(endPatts)  # remove ending *
        print("L:", L)
        def isPrefix(A, B):
            #Check is B is prefix of A. len(B) <= len(A)
            for i in range(len(B)):
                if A[i] != B[i]:
                    print(B, "is NOT prefix of", A)
                    return False
            print(B, "is prefix of", A)
            return True
        for p in endPatts:
            if not isPrefix(L, p):
                print("Returning None")
                return None     # no possible answer for all
        print("Returning L:",L)
        return L    # return without asterisk

    def fixedSuffix(self, startPatts, middlePatts):
        # transform middlePatts into startPatts -> trim all before *
        middlePatts = [p.split('*')[1] for p in middlePatts]    # remove asterisks
        startPatts.extend(middlePatts)
        print("Extended startPatts:", startPatts)
        L = self.findMaxLen(startPatts)

        def isSuffix(A, B):
            # Check if B is a suffix of A. len(B) <= len(A)
            for i in range(1, len(B)+1):
                if A[-i] != B[-i]:
                    print(B, "is NOT suffix of",A)
                    return False
            print(B, "is suffix of",A)
            return True

        for p in startPatts:
            if not isSuffix(L, p):
                return None
        print("Returning L:",L)
        return L

    def matchPatterns(self, P):
        startwith = list()
        endwith = list()
        middlewith = list()
        for patt in P:
            if patt[0] == '*':
                startwith.append(patt[1:])      # no asterisk
            elif patt[-1] == '*':
                endwith.append(patt[:-1])       # no asterisk
            else:
                middlewith.append(patt)         # includes asterisks, removed later

        print(startwith)
        print(middlewith)
        print(endwith)

        fixed_prefix = self.fixedPrefix(endwith , middlewith)
        fixed_suffix = self.fixedSuffix(startwith , middlewith)
        print("Prefix: '{}'".format(fixed_prefix))
        print("Suffix: '{}'".format(fixed_suffix))
        if fixed_prefix is not None and fixed_suffix is not None:
            return fixed_prefix + fixed_suffix
        return '*'      # else, no answer satisfies all patterns

    def main(self):
        for tc in range(int(input())):
            P = list()
            for p in range(int(input())):
                P.append(input())
            print("Case #{}: {}".format(tc+1, self.matchPatterns(P)))


class TestCase3:
    """At least one asterisk is present in every string.
        Generalizing the solution from Test Set 2, we know that every pattern prescribes a prefix for the
        resulting word (the letters before the first *) and a suffix for the resulting word (the letters after the last *).
        Allowing for empty prefixes and suffixes means we get one prefix, one suffix for every pattern.
        However, what about the middle part??
        Suppose we have a pattern with more than 2 asterisks. It may look like this
            X*M1*M2*...*Mk*Y
            where M1, M2 are non trivial substrings in the middle, bounded by kleene stars *.
            After ensuring that X is prefix of P and Y is suffix of S, all that remains is to
            ensure that M1*M2*...*Mk is present in the outpur word, strictly between P and S.
        """

    def isSuffix(self, A, B):
        # Check if B is a suffix of A. len(B) <= len(A)
        for i in range(1, len(B) + 1):
            if A[-i] != B[-i]:
                return False
        return True
    def isPrefix(self, A, B):
        # Check is B is prefix of A. len(B) <= len(A)
        for i in range(len(B)):
            if A[i] != B[i]:
                return False
        return True
    def findMaxLen(self, words):
        max = ""
        for w in words:
            if len(w) > len(max):
                max = w
        return max

    def commonPrefix(self, preWords):
        L = self.findMaxLen(preWords)
        for p in preWords:
            if not self.isPrefix(L, p):
                return None
        return L

    def commonSuffix(self, endWords):
        L = self.findMaxLen(endWords)
        for p in endWords:
            if not self.isSuffix(L, p):
                return None
        return L

    # 1. Find common prefix P of all patterns.
    # 2. Find common suffix S of all patterns.
    # 3. Find midwords of all patterns and concatenate them.
    # 4. Return P + M..M + S
    def matchPatterns(self, P):
        # Every element of P has at least 1 asterisk.
        # If the split array has len>2, we have a midword.
        prewords = list()
        midwords = list()
        endwords = list()
        for patt in P:
            words = patt.split('*')
            if len(words)>2:
                # We have midwords of the form *M1*M2*M3*
                M = ''.join(words[1:-1])       # add every subword except the first and last (pre and end)
                midwords.append(M)
            prewords.append(words[0])
            endwords.append(words[-1])

        P = self.commonPrefix(prewords)
        if P is None: return '*'
        S = self.commonSuffix(endwords)
        if S is None: return '*'

        return P + ''.join(midwords) + S


    def main(self):
        for tc in range(int(input())):  # input T
            P = list()
            for p in range(int(input())):   # input N
                P.append(input())
            print("Case #{}: {}".format(tc+1, self.matchPatterns(P)))

if __name__ == '__main__':
    TestCase3().main()
"""
6
5
a*c*e
*b*d*
asa*
a*c*elton
*haha*
2
**Q**
*A*
2
A*C*E
*B*D
2
A*C*E
*B*D*
2
CODE*
*JAM
4
H*O
HELLO*
*HELLO
HE*
"""

