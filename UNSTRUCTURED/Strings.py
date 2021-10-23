from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    # We get a variable amount of strings <=200, each of length <=200
    # Longest common prefix can be at most as long as the shortest string
    minlength = 200
    for string in strs:
        minlength = min(minlength, len(string))

    lcp = ""
    if len(strs) > 0:
        for i in range(minlength):
            # Check if the ith letter is present in every string of strs
            letter = strs[0][i]
            common = True
            for s in strs:
                if s[i] != letter:  # if a string doesn't have the ith element
                    common = False
                    break       # the rest cannot be part of the lcp
            if common:
                lcp += letter   # if it is common we can add it safely to the lcp
            else:
                break
    return lcp


def longestPalindrome(s: str) -> str:
    n = len(s)
    if n < 1: return ""
    ans = s[0]
    #for startIdx in range(n - 1):
    startIdx = 0
    while (startIdx < n-1):
        endIdx = n - 1  # always begin with last pos
        print("Current start index ", startIdx, s[startIdx])
        foundPal = False
        while (startIdx < endIdx and endIdx-startIdx+1 > len(ans)):     # don't check if remaining string is smaller than ans
            # try same start, different ends each time
            print("Checking from ", startIdx, "to", endIdx)
            i = startIdx
            j = endIdx
            if s[i] == s[j]:
                print("Match", s[i], "at:", i, j, "start matching.")
                # start matching possible pal
                while (i < j and s[i] == s[j]):  # finds pals of len >1
                    print(s[i],"==",s[j])
                    i += 1
                    j -= 1
                print("Matching ends:", i, j)
                if i >= j:  # found palindrome, pointers might overpass each other
                    print("found palindrome", s[startIdx:endIdx+1])
                    if len(s[startIdx:endIdx + 1]) > len(ans):
                        ans = s[startIdx:endIdx + 1]
                    foundPal = True
                    startIdx = j
                    break # everything from start to index i is matched; we don't need to check the rest
            endIdx -= 1 # try with another end Index
            print("Try next end Index:", endIdx)
        if not foundPal:
            startIdx += 1
    return ans

if __name__ == "__main__":
    s = "abcdefgmaa"
    print(s)
    print("ANSWER:", longestPalindrome(s))