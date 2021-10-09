# 1 kg -> 30m2 of grass
# Given price quote for a set of B bags (1..5) of weight Wi each and price Pi in coins.
# Given the measurements of all sides from each of the N (0..10^5) triangles. 
# Compute the minimum number of coins needed to buy enough seeds to cover missing area
# Return -1 if there is no way to fix the property

# -------- https://codeforces.com/gym/103274/problem/A

import math
import numpy as np
from collections import deque, queue

def getArea(sides):
    # Heron's Formula
    a, b, c = sides
    s = sum(sides)/2

    return (s*(s-a)*(s-b)*(s-c))**0.5


def solve(B, N, W, P, T):


    area = sum([getArea(sides) for sides in T])
    print("Total Area:", area)
    targetKg = math.ceil(area / 30.0)
    print("Required kg", targetKg)
    pass



B, N = [int(x) for x in input().split()]
print("B=",B,"N=", N)
weights = []
prices = []

for _ in range(B):
    w, p = [int(x) for x in input().split()]
    weights.append(w)
    prices.append(p)

print("Weights", weights)
print("Prices", prices)
triangles = []

for i in range(N):
    dims = [int(x) for x in input().split()]
    print(i, ":\t", end="")
    print("a, b, c = ", dims)
    triangles.append(dims)

print(solve(B, N, weights, prices, triangles))