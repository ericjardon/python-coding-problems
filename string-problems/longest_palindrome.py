'''
Given a string, return the longest palindrome contained in the string.

'''


def longestPalindrome(string):

    n = len(string)

    if not n:
        return ""

    ans = s[0]

    start = 0

    while (start < n-1):
        # Check up to last position
        end = n-1

        foundPalindrome = False
        possibleLen = end - start + 1
        while (start < end and possibleLen > len(ans)):

            if string[start] == string[end]:
                # If start and end match, start palindrome search
                i = start
                j = end

                while (i < j and s[i] == s[j]):
                    i += 1
                    j -= 1

                if i >= j:
                    # palindrome found from start to end
                    candidate = string[start:end+1]
                    if len(candidate) > len(ans):
                        ans = candidate
                    foundPalindrome = True
                    start = j
                    break
            # try from same start to new end = end-1
            end -= 1
            possibleLen = end - start + 1

        # try from new start = start+1
        if not foundPalindrome:
            start += 1

    return ans


# SLIDING WINDOW / GREEDY APPROACH
def fasterPalindromeSubstring(s:str)->str:
    # slicing is O(n+k) where N is length of string and k is length of slice
    # check if the whole is a palindrome
    print("String:", s)
    if s==s[::-1]:
        return s
    N = len(s)
    start = 0
    maxlen = 1  # maintains the length to best on every iteration

    for i in range(1, N):
        # Try substrings ending at i, with length max_length+1 and max_length+2
        print('>',i, 'maxlen', maxlen)
        left = i - maxlen
        right = i + 1  # add 1 so it includes char at right

        s1 = s[left:right]
        print('\ts1', s1)
        s2 = s[left-1:right]  
        print('\ts2', s2)

        if s1 == s1[::-1]:  # s1 is a palindrome larger than max_len
            start = left
            maxlen += 1
        
        # We use a second try, s2, to improve if past iteration was not palindromic
        elif left-1 >= 0 and s2 == s2[::-1]:  # s2 is a palindrome lerger than maxlen by 2
            start = left-1
            maxlen += 2

        # Since we keep our current best in maxlen, we can only check palindromes that may 
        # be better than our last.
        # Every iteration we check string that end at i with lengths maxlen+1 and maxlen+2 if available.
        # Our window is of size maxlen+1, +2! and our step is 1 by 1 (for loop) 
        #
        # !! This works because of the nature of palindromes: they are recursively palindromic so once
        # we find a small palindrome we can continue increasing it adding characters to its sides:
        # to the right with i, and to the left with our s2 which probes 1 char back from previous try
        # s1 checks that palindrome actually starts at l, while s2 checks that our previous palindrome can
        # be extended!!!

    return s[start:start+maxlen]


if __name__ == "__main__":
    # s = "amamaromamoraaaaaaaaaa"
    # print(longestPalindrome(s))
    a = "abbax"
    b = "theconanocsubus"

    print(fasterPalindromeSubstring(b))
