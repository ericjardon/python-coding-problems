# GCD of two ints a, b is the largest positive integer
# that can divide both.

# INPUT
# one or more test cases of the form 'a b'
# the program stops processing input when a and b are -1
# OUTPUT
# the gcd of the given a b.

def gcdOfTwo():
    while True:
        z = str(input()).split(" ")
        a = int(z[0])
        b = int(z[1])
        if (a == -1 and b==-1):
            break
        result = gcd(a, b)
        print(str(result))

def gcd(n, m):
    if m==0:
        return n
    else:
        return gcd(m, n%m)

# Find the gcd of three numbers:
# The GCD of three numbers is equal to
# the gcd between the GCD of any two of them and the third.
# This can be repeated for n numbers.

# INPUT
# 3 non negative integers, one per line
# OUTPUT
# the GCD of the three nums

def main():
    a = int(input())
    b = int(input())
    c = int(input())
    result = gcd(gcd(a,b), c)
    print(result)

main()