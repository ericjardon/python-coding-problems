"""A lapindrome is a string that split in the middle, the 2 halves
have same characters and same frequency of each character.
If string length is odd, ignore the middle character."""

# Given a string determine if it is a lapindrome
from collections import Counter
def isLapindrome(string):
    l = len(string)
    if l==1 or l==0:
        return True
    else:
        # split the string into two
        a = string[:l//2]       # first half, normal order
        b= string[-1:l-l//2 -1 :-1]     # second half, reversed (no need to reverse!)
    # Counter is a built in method that counts the occurrences of each character in a String
    return Counter(a) == Counter(b)

#T = int(input())
#for i in range(T):
    #s = input()
    #print("YES" if isLapindrome(s) else "NO")