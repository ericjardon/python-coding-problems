## PROBLEM 4 Largest Palindrome Product
def largestPalindrome() -> int:
    """find the largest palindrome number obtained from the product of two 3-digit nums"""
    def isPalindrome(num):
        return str(num) == str(num)[::-1]
    ans = 10201
    # brute force: find every possible product i,j of numbers with 3 digits
    for i in range(999, 100, -1):
        for j in range(999, 100, -1):
            if isPalindrome(i*j) and i*j > ans:
                ans = i*j
    return ans

## PROBLEM 5 Smallest Multiple of natural numbers up to 20
def smallestMultiple(N) -> int:
    """Return the smallest positive number that is evenly divisible by all numbers from 1 to N"""
    primes = [2, 3, 5, 7, 11, 13, 17, 19]   # primes up to N
    def get_prime_factors(n):
        """Returns a list of the prime factors of any n>1"""
        factors = list()
        for p in primes:        # might present a problem for numbers N>20
            while(n%p==0):
                factors.append(p)
                n = n/p
        return factors

    ans = []        # list of factors included in answer
    for num in range(2, N+1):
        print("num:", num)
        for f in ans:       # reduce num by every possible divisor in our factors list
            if num%f==0:
                num = num/f
        print("quotient remaining:", num)
        if num>1:
            ans.extend(get_prime_factors(num))      # append the prime factors of quotient to the list
        print(ans)

    multiple = 1
    for f in ans:       # answer is the product of all factors in our list
        multiple *= f
    return multiple     # for N=20: 232792560 CORRECT


## PROBLEM 6 SUM SQUARE DIFFERENCE
def squareDifference(N) -> int:
    """Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum."""
    # Find sum of squares
    sum_of_squares=0
    for i in range(1,N+1):
        sum_of_squares += i*i
    square_of_sum = ((N*(N+1))/2)**2
    return square_of_sum - sum_of_squares

## PROBLEM 7
from math import sqrt, floor
def Nthprime(N) ->int:
    """Find the 10,0001st prime number"""
    primes = [2]
    p = primes[-1] + 1
    count = 1
    while count<N: # calculate n-1 more primes
        bound = floor(sqrt(p))  # for 3, it is 1
        i=0
        isPrime = True
        while (i < len(primes) and primes[i] <= bound):    # while it is indivisible by every prime
            if p%primes[i]==0:
                isPrime = False
                break
            i += 1      # try dividing by every prime
        if isPrime:
            primes.append(p) # current number p is not divisible by any previous prime
            p = primes[-1] + 1
            count += 1
        else:
            p += 1
    return primes[-1]       # for N= 10,001 ans=104743 CORRECT

## PROBLEM 8
from functools import reduce
largeNum = '''73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450'''
def largestAdjProduct(number: str, N: int):
    """Given a 1000-digit number as a string, find the largest product
        achieved with N=13 adjacent digits and return it"""
    number = number.replace('\n', '')
    digits = number[:N]     # length N
    maxProd = reduce(lambda a,b: a*b, [int(x) for x in digits])
    LEN = len(number)
    for startIdx in range(1, LEN-N+1):
        digits = number[startIdx:startIdx+N]
        prod = reduce(lambda a, b: a * b, [int(x) for x in digits])
        maxProd = max(maxProd, prod)

    return maxProd      # for N=13, 23514624000 CORRECT

# PROBLEM 9
def pythagoreanTriplet():
    """A pythagorean triplet is a set of numbers a<b<c such that a^2+b^2=c^2.
        Find the triplet for which a+b+c = 1000"""
    # We can choose to only vary a and b, and substract c from 1000 to check correctness
    # stop when the square root of a*a + b*b is 1000-a-b

    # min value for a is 0, max val is 1000
    for a in range(1001):   # a takes the values 0 to 1000
        b_plus_c = 1000-a
        for b in range(b_plus_c):
            c = b_plus_c - b
            if a*a + b*b == c*c and a<b and b<c:
                print("{} + {} + {} = {}".format(a, b, c, a + b + c))
                return (a,b,c)

## PROBLEM 10
def sumOfPrimes(N):
    """Find the sum of all primes below N=2,000,000"""
    sum = 2
    primes = [2]
    for n in range(3, N): # we already know 2M is not prime
        bound = floor(sqrt(n))  # for 3, it is 1
        isPrime = True
        i=0
        while (i < len(primes) and primes[i] <= bound):    # check divisibility by primes <= _sqrt(n)_
            if n%primes[i]==0:
                isPrime = False
                break
            i += 1      # try dividing by every prime
        if isPrime:
            sum += n
            primes.append(n) # current number p is not divisible by any previous prime
    print(primes)
    print("sum = ",sum)
    return sum      # for N=2,000,00 ans=142913828922 CORRECT


class Problem11:
    """Given a 20x20 grid, return the largest product along 4 adjacent numbers
        In vertical, horizontal or diagonal position"""
    rawGrid = '''\
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48'''

    def convertGrid(self, rawGrid: str):
        grid = list()
        lines = rawGrid.splitlines()
        for line in lines:
            grid.append(line.split(' '))
        return grid
    def printGrid(self, grid):
        print("start grid:")
        for row in grid:
            print(row)
        print("\t end grid")

    def max_in_rows(self, grid, n=4):
        maxProd = 0
        rLen = len(grid[0])     # 20 in base problem
        for r in range(rLen):        # index of row
            for startIdx in range(rLen-n+1):    # check every 4 positions in the row
                digits = [int(grid[r][c]) for c in range(startIdx, startIdx+n)]     # col index varies; horizontal array
                prod = reduce(lambda a,b: a*b, digits)
                maxProd = max(maxProd, prod)
        print("max in rows:", maxProd)
        return maxProd

    def max_in_cols(self, grid, n=4):
        maxProd = 0
        Len = len(grid)     # assuming square grid
        for c in range(len(grid[0])):     # index of column
            for startIdx in range(Len-n+1):     # check every 4 positions in the column
                digits = [int(grid[r][c]) for r in range(startIdx, startIdx+n)]   # row index varies; vertical array
                prod = reduce(lambda a,b: a*b, digits)
                maxProd = max(maxProd, prod)
        print("max in columns:", maxProd)
        return maxProd

    def max_in_crossDown(self, grid, n=4):  # \
        # Identify possible possible start index for the diagonal \.
        # Traverse row by row, column by column, only those start indices that allow a 4-digit diagonal
        Len = len(grid)
        maxProd=0
        for r in range(Len-n+1):
            for c in range(Len-n+1):    # for every possible start index
                digits = [int(grid[r+i][c+i]) for i in range(n)]    # r increasing, c increasing
                prod = reduce(lambda a,b: a*b, digits)
                maxProd = max(maxProd, prod)
        print("max in crossDown diagonals:", maxProd)
        return maxProd

    def max_in_crossUp(self, grid, n=4):
        # Identify every possible start index for the diagonal /
        Len = len(grid)
        maxProd=0
        for r in range(Len-n+1):
            for c in range(n-1, Len):
                digits = [int(grid[r+i][c-i]) for i in range(n)]   # r increasing, c decreasing
                prod = reduce(lambda a,b: a*b, digits)
                maxProd = max(maxProd, prod)
        print("max in crossUp diagonasl:", maxProd)
        return maxProd

    def maxProductGrid(self, grid, n=4):
        maxProd = 0
        maxProd = max(max(max(max(maxProd, self.max_in_rows(grid)),self.max_in_cols(grid)),
                          self.max_in_crossUp(grid)), self.max_in_crossDown(grid))
        return maxProd          # for base problem input ans=70600674 CORRECT


if __name__=="__main__":
    x=1

