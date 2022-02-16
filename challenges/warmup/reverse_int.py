MAX_INT = 2**31 - 1
MIN_INT = -(2**31)

from math import ceil

class Solution:
   
    def reverse(self, x: int) -> int:
        # To reverse a string we can push all of its elements
        # to a stack and then pop them all in order.
        # Or alternatively, pushing every last digit of the string one by one
        # into a stack, and the stack will read in reverse (bottom - up)
        
        # We actually don't need extra memory, we can build
        # the reverse number with arithmetic
        
        rev = 0
        # Pop the last digit and 'append' to rev
        if x > 0:
            while x != 0:
                last_digit = x%10  # least-significant digit
                # Check overflow:
                if rev > MAX_INT//10 or (rev == MAX_INT//10 and last_digit > 7) :  
                    return 0
                rev = rev*10  # make space for new digit
                rev += last_digit
                x = x//10
                #print('rev', rev)
        else:
            while x != 0:
                last_digit = (-x)%10
                #print('last digit', last_digit)
                if rev < ceil(MIN_INT/10) or (rev == ceil(MIN_INT/10) and last_digit > 8):  # overflow
                    return 0
                
                rev = rev*10  # make space
                rev -= last_digit
                x = -(-x//10)
                #print('rev', rev, 'x=', x)
                
        return rev
        