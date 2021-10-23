"""The Z function takes in an integer number N and returns the number of trailing zeroes of
    it's factorial. It has been demostrated that it is an always-increasing function."""
import math
def zfunction(n):
    # Zeroes are proportional to the number of factors '5' in the factorial.
    # Any multiple of 5 contains 1 five
    # Any multiple of 25 contains 2 fives
    # Any multiple of 125 contains 3 fives and so on...
    # when we only divide n by 5, there may still be powers of 5 remaining in the factors.
    # the solution is two iteratively divide by increasing powers of 5, this will give us the total number
    # of fives contained in the factors of Num
    zeroes = 0
    i = 1
    while (5**i <= n):
        zeroes += math.floor(n / 5**i)
        i += 1

    return zeroes



# testing factorial with numbers from 1 to 21 reveals a pattern: the amount of trailing zeros is
# proportional to the number of factors "5" and "2" that are added to the product.
# everytime we have a pair of factors 5 and 2, the number of zeroes increases by 1.

def fact(n, memo={}):
    if n==1 or n==0:
        return 1
    else:
        result = n * fact(n-1, memo)
        memo[n] = result
    return result


def main():
    try:
        T = int(input())
        for _ in range(T):
            n = int(input())
            print(zfunction(n))
    except:
        pass

print(fact(25))

def zfunctionEric(n):
    zeroes=0
    fives=[5]
    for f in range(5, n+1, 5):
        if (f/5 in fives):
            # is a power of 5
            zeroes += gSum(len(fives))
        else:
            zeroes +=1
    return zeroes

def gSum(n):
    return ((n+1)*n)/2


# unsolved