import math
from collections import deque

N = int(input()) # numCandy

print("0", end="")
seen = set()
seen.add(1)
bound = math.floor((math.sqrt(N)))

upper = deque()
for i in range(2, bound+1):
    if (N%i == 0):
        print(f" {i-1}", end="")
        seen.add(i)
        q = int(N/i)
        if (q != i and q not in seen):
            upper.appendleft(q)

for x in upper:
    print(f" {x-1}", end="")

print(f" {N-1}", end="")
