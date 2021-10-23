from typing import List

def primesUpToN(n: int) -> List[int]:
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    nums = set()
    for i in range(2, n):
        nums.add(i)
    # Sieve of Erasthotenes approach.
    # Remove all multiples of p : p lower than sqrt(n)
    p = 2
    while (p*p <= n):   # p takes values up to sqrt(n)
        k = 0
        while (p*p + k*p < n):
            nums.discard(p*p + k*p)     # unlike remove(), discard doesn't raise error
            k += 1
        p += 1

    return list(nums)

from math import sqrt, floor        # something wrong
def countPrimes(n: int) -> List[int]:
    # Implements the sieve of erasthotenes
    # Returns count of prime nums less than n
    # Discard from primer all multiples of p : p < sqrt(n)
    numbers = [x for x in range(n)]

    for p in range(2, floor(sqrt(n))):
        if numbers[p] != 0:  # has not been discarded
            j = p*p
            while j <= n:
                numbers[j] = 0  # discard j
                j = j + p

    res = list()
    for p in range(2, n):   # copy back all nonzero numbers
        if numbers[p] != 0:
            res.append(p)
    return res

def comparison():
    print("Eric")
    print( primesUpToN(15) )
    print("cP")
    print( countPrimes(15) )

comparison()