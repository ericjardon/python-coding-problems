"""
>Nesting of Parenthesis: susbtring occurring between two parenthesis
>Nesting depth: of a position p in a string is the number of pairs of
matching parentheses that enclose that position p.
>Matching Parentheses: either () every parenthesis in their nesting also matches.

Given a digit String S, return a modified version of the string
    of minimal length such that every digit d is enclosed by d pairs of parenthesis"""

def binNestingDepth(S: str) -> str:
    """Takes a binary string. with len >0. Simply surrounds every digit d with d pairs of parenthesis,
    grouping identical values"""
    if len(S) == 1:
        if int(S) == 1:
            return '('+S+')'
        else:
            return S
    ans = ""
    i=0
    while i < (len(S) - 1):
        group = S[i]       # identify groups of same type digits
        j = i + 1       # fast pointer to look ahead of i
        while (j < len(S) and S[j] == group[0]):
            group += group[0]     # concatenate identical digits
            j+=1
        ans += '('*int(group[0]) + group + ')'*int(group[0])
        # times 1 because we know d is 1
        i = j       # let i catch up with j
    if i == len(S) - 1:     # last character was not appended
        print("Careful to add last")
        ans +=  '('*int(S[-1]) + S[-1] + ')'*int(S[-1])
    return ans

# Explanation: we can traverse the string in linear time, knowing which parenthesis to insert before every digit.
# The type (opening/closing) and amount of parentheses to insert before every digit is determined by the difference
# between the digit d and how many opening parenthesis are before it. We can use this information to either
# open up the necessary parenthesis or close the surplus ones.
# With the count, we insert no parentheses if d is exactly the same as the previous digit.
# This solution leverages the idea that an opening parenthesis here can be reused for any digit to the right

def nestingDepth(S: str) -> str:
    # Insert the minimum amount of parenthesis such that every digit d
    # in the string is enclosed by exactly d pairs of parenthesis.
    count = 0       # tracks count of open parenthesis left to close.
    ans = ""        # we build upon this string and return it
    for i in range(len(S)):     # for every digit of S
        # Before we append a digit, look at how many and what parenthesis we can insert to its left
        d = int(S[i])
        print(S[:i+1] + '*' + S[i+1:])
        # Compare current digit with amount of open parentheses.
        # This difference determines the type (+/-) and amount (abs value) of parentheses to insert before digit
        # If d larger, we can't fit d within current nest. Open as many ( parenthesis as the difference and increment count of open parenth
        # If d is smaller, it fits in current nest so we can insert as many closing ) parenthesis as the difference and decrease count of open parenth

        times = abs(d - count)      # how many times for our loop
        # we could set up two different loops separated by ifelse given by d-count>0, or we can check in every iteration.
        # the sign will not change for a given loop. Here we use a single loop
        for p in range(times):
            #print("Loop for",times,"times")
            if d-count < 0:     # d < open parentheses, we have to close parenthesis until we have d open parenthesis remaining after insertion
                ans += ')'
                #print("ans:",ans)
                #print("count:", str(count-1))
                count -= 1
            else:   # d > open parenthesis, open necessary parentheses for d so we have d open parentheses after isnerting
                # note: d-count is never 0. It's always either positive or negative
                ans += '('
                #print("ans:",ans)
                #print("count:", str(count+1))
                count += 1
        #print("append digit")
        #print(ans + S[i])
        ans += S[i]

    for p in range(count):  # close remaining parenthesis after last digit
        ans += ')'

    return ans

def inefficientMain():
    # An inefficient but fun solution
    # This problem can be solved by replacement only.
    # Every digit can be replaced by "digit*( + digit + digit*)"
    # Then reducing the result by eliminating all instances of ')('. [you'll find there are no )( in valid answers]
    for testcase in range(int(input())):
        rawStr = ''.join([int(x)*'(' + x + int(x)*')' for x in str(input())])
        print(rawStr)
        for _ in range(9):  # why 9? because there are at most 9 surplus pairs of parentheses
            rawStr = rawStr.replace(')(', '')
            print(rawStr)

        print ("Case #{}: {}".format(testcase+1, rawStr))

#if __name__ == "__main__":
def efficientMain():
    T = int(input())
    # S  = 342164343
    for t in range(1, T+1):
        S = input()
        S_ = nestingDepth(S)
        print(f"Case #{t}:", S_)

inefficientMain()