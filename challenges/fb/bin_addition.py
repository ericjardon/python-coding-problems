'''
Implement binary addition of two strings.
For example "101101" and "111101" equal "1101010"
You cannot use any type conversion, operate only with strings.
'''


def binaryAddition(A, B):
    # reverse both bit strings to read from least to most significant
    A = A[::-1]
    B = B[::-1]

    i = 0
    ans = ''  # string builder
    carry = False

    # Traverse the strings from least to most significant bits
    while i < len(A) and i < len(B):
        # next digit is the sum of a and b bits + carry.
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


    # Catch up loops to capture the rest of significant bits
    # remember to use the carry bit

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
    
    # Add last carry!
    if carry:
        ans += '1'
    
    # The string was built left to right, so the answer is the reverse of this.
    return ans[::-1]

# O(N) where N is the length of larger string. We do three reverse operations which are O(N), but O(4N) ~ O(N)

a = '10'
b = '1'
# a = '0'
# b = '0'

print(binaryAddition(a,b))