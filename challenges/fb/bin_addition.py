'''
Implement binary addition of two strings.
For example "101101" and "111101" equal "1101010"
You cannot use any type conversion, operate only with strings.
'''


def binaryAddition(A, B):
    A = A[::-1]
    B = B[::-1]

    i = 0
    ans = ''
    carry = False

    # Traverse the strings from least to most significant bits
    while i < len(A) and i < len(B):
        s = int(A[i]=='1') + int(B[i]=='1') + int(carry)

        if s == 0:
            ans += '0'
            carry = False
        
        if s == 1:
            ans += '1'
            carry = False

        if s == 2:
            ans += '0'
            carry = True
        
        if s == 3:
            ans += '1'
            carry = True
        
        i += 1

    while i < len(A):
        s = int(A[i]=='1') + int(carry)
        if s == 0:
            ans += '0'
        if s == 1:
            ans += '1'
            carry = False
        if s == 2:
            ans += '0'
            carry = True
        i += 1

        
    while i < len(B):
        s = int(B[i]=='1') + int(carry)

        if s == 0:
            ans += '0'
        if s == 1:
            ans += '1'
            carry = False
        if s == 2:
            ans += '0'
            carry = True
        i += 1
    
    # Add last carry
    if carry:
        ans += '1'
    
    return ans[::-1]


a = '10'
b = '1'
# a = '0'
# b = '0'

print(binaryAddition(a,b))