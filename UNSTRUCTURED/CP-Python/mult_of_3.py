"""Build a particular int N from given input:
 We are given the first two digits from a total of K  of a
 certain number N. For every subsequent digit d_i, d_i must
 be equal to modulo 10 of the sum of all preceding digits.
 The task is to determine if N is a multiple of 3"""

def is_mult_of_3(k, d0, d1):
    # a k-digit N is multiple of 3 if the sum of its digit-wise modules of 3
    # are also a multiple of 3.
    # this is helpful because we don't want to concatenate strings
    # maybe map a function to an array of the digits
    s = d0 + d1
    mods = [d0%3, d1%3]
    for i in range(2, k):
        di = s%10
        s += di
        mods.append(di%3)

    return sum(mods)%3 == 0

# is too slow for very big k. Dynamic programming? something much easier to calculate?

def generateNum(k, d0, d1):
    sum = d0 + d1
    num = ""+ str(d0)+str(d1)
    for _ in range(2, k):
        di = sum%10
        sum += di
        num = num + str(di)
    print(num)

generateNum(4, 7, 1)
