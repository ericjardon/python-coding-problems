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


if __name__ == "__main__":
    s = "amamaromamoraaaaaaaaaa"
    print(longestPalindrome(s))
