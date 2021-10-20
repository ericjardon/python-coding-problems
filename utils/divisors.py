from math import sqrt

def divisorsOf(x):
    divisors = []
    i = 1
    while i <= sqrt(x):
        if (x % i == 0):

            if (x / i == i):
                divisors.append(i)
            else:
                # let x = 100,
                # 4 * 25 = 100, both 4 and 25 are divisors
                divisors.append(i, x/i)
        i += 1
    return divisors