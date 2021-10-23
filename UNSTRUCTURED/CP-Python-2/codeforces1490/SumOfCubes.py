# Given a positive integer x. Determine if it's representable
# as the sum of the cubes of another two positive integers.

# FORMALLY: check if there are two integers a,b both >=1 such that
# a**3 + b**3 = x
import math
# Note: cubes for this problem are always positive.
def sumOfCubes(x: int) -> bool:
    cubes = set()
    bound = math.ceil(x**(1./3))
    #print("root:", bound)
    for i in range(1, bound+1):
        cube = i*i*i
        cubes.add(cube)
        if (x - cube) in cubes:
            return True
    return False


for t in range(int(input())):
    if sumOfCubes(int(input())):
        print("YES")
    else:
        print("NO")
