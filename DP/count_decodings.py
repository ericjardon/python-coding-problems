'''
PROBLEM: Count Decodings of a sequence of Digits

Given a positive number, map its digits to the corresponding alphabet
in the mapping table as follows: [(1,A),(2,B),..] etc. 

Return the total num of decodings possible.
For example, 123 maps to "ABC" (1,2,3), "LC" (12,3), and "AW" (1,23)

----
Approach:
    We have two options to map: take one digit or take two digits.
    Any single digit can be mapped to a letter.
    Pairs of digits can be mapped to a letter if 10<=x<=26
    We can use a table or memo to store the number of encodings for 
    the number ending at position N.

Recurrence Relation:
    encodings(n) = encodings(n-1)*mappable(number[n]) + encodings(n-2)*mappable(number[n-2:])
    where encodings(1) = 1 and encodings(0) = 1
'''


def countDecodings(x: int, method: str = 'tabulation') -> int:

    def countRec(number: str, memo: dict = {}) -> int:
        n = len(number)   # position where we are in original string

        # One or no digits left after recursing, we count as 1 encoding
        if n < 2:
            return 1

        # If the number of encodings for this string length hasn't been calculated
        if n not in memo:
            decodings = 0

            # A) Take single digit
            single_last_digit = int(number[-1])

            # If the single last digit is mappable to a letter
            if single_last_digit > 0:  # 1-9 can be mapped
                decodings += countRec(number[:-1], memo)

            # B) Take the last two digits
            pair_digits = int(number[n-2:])

            # If the pair is mappable to a letter
            if 10 <= pair_digits <= 26:
                decodings += countRec(number[:n-2], memo)

            # Store the result for this given amount of digits
            memo[n] = decodings

        return memo[n]

    def tabulation(number: str) -> int:

        dp = [0 for _ in range(len(number))]

        # Base cases
        dp[0] = 1
        dp[1] = 1

        # For every position in the number string
        for n in range(2, len(number)):
            decodings = 0

            # if last Single digit is mappable
            if int(number[-1]) > 0:
                # Add decodings from removing single digit
                decodings += dp[n-1]

            # if last Pair of digits is mappable
            if 10 <= int(number[n-2] + number[n-1]) <= 26:
                # Add decodings from removing the two digits
                decodings += dp[n-2]

            # Save the result for position n to table
            dp[n] = decodings

        # Return decodings of full length
        return dp[len(number) - 1]

    def enhancedCountDecodings(number: str) -> int:
        def isMappable(num: int):
            return 0 < num < 27

        N = len(number)
        if N < 2:
            return N  # 0 or 1 encodings if length is 0 or 1

        decodings_at_n = [0 for _ in range(N)]
        decodings_at_n[0] = 1
        decodings_at_n[1] = 1
        for n in range(2, N):
            decodings = 0
            single = int(number[-1])
            pair = int(number[n-2] + number[n-1])
            if isMappable(single):
                decodings += decodings_at_n[n-1]
            if isMappable(pair):
                decodings += decodings_at_n[n-2]

            decodings_at_n[n] = decodings

        return decodings_at_n[N-1]

    # DRIVER FUNCTION
    numberstring = str(x)

    if method == 'tabulation':
        return tabulation(numberstring)

    if method == 'memoization':
        return countRec(numberstring)

    if method == 'enhanced':
        return enhancedCountDecodings(numberstring)

    else:
        raise ValueError('method must be tabulation or memoization')


if __name__ == "__main__":
    number = ['2432342142143641235342316549']
    ans = [432]

    for i in range(len(ans)):
        t = countDecodings(number[i], 'tabulation')
        m = countDecodings(number[i], 'memoization')
        e = countDecodings(number[i], 'enhanced')

        print(f"Memo: {m}, Tab: {t}, Enhanced: {e}")
        if (m == ans[i] and m == t and t == e):
            print("Test passed")
        else:
            print("Error: expected 432")
