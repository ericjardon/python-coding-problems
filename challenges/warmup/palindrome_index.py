def palindromeIndex(s):
    # Brute Force
    def isPalindrome(st):
        return st == st[::-1]
    n = len(s)
    if isPalindrome(s):
        return -1
        
    for i in range(n):
        temp = s[:i] + s[i+1:]
        print(temp, end=" ")
        res = isPalindrome(temp)
        print(res)
        if res:
            return i
    
    return -1


(print(palindromeIndex("anitaxatina")))