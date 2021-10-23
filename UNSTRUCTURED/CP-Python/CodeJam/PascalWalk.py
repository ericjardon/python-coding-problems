"""
A Pascal Triangle consists of an infinite num of rows, and increasing number of integers per row.
Let (r,k) be the kth position from the left in the rth row.
Both r and k are 1-based indexes.
Rules:
- The r-th row has r integers (row length).
- For every row, the numbers at (r,1) and (r,r) are 1 (edge positions).
- A num at pos (r,k) is equal to the sum  of (r-1, k-1) and (r-1, k) for every k: [2,k-1]
* we can generate one using DP, stored in a map with keys r and val [k1, k2, k3...]]

Pascal Walk: a sequence of positions: (r1, k1), (r2, k2), ..., (rs, ks), such that:
- Every subsequent position is adjacent to the previous one in the triangle.
- e.g. from (r,k), adjacent are: (r-1, k-1), (r-1,k), (r,k-1),
                                (r, k+1), (r+1,k), (r+1, k+1)
- No position may be repeated.
- Find a Pascal walk S <= 500 such that the sum of nums in every position
    is equal to N, guaranteed such exists,
"""

# Every level of the Pascal Triangle sums a total of 2^(index-1).
# I can calculate the Triangle up to a certain level whose sum is closest to the given N, and
# add downwards the elements I need.
# I need to make sure the walk is boustrophedonical; so it ends at an edge and i can sum 1s.
from pprint import pprint

class PascalWalk:
    def buildPascalTriangle(self, N):
        # N is the number of levels to generate
        pascal = dict()
        pascal[1] = [None, 1]    # fake 1-based index
        pascal[2] = [None, 1, 1]
        for r in range(3, N+1):
            pascal[r] = [None for _ in range(r+1)]
            pascal[r][1] = 1
            pascal[r][r] = 1        # edge numbers
            for k in range(2, r):
                pascal[r][k] = pascal[r-1][k-1] + pascal[r-1][k]
        return pascal
        # Power 2^P is found @ level P+1
        # Level L sums 2**(P-1)
        # 1. Given N, find 2^P smaller or equal to N. <<Generate P+1 levels of Pascal Triangle>>. (ex for 2^0 we generate 1 level)
            # If N is exactly equal to 2^P, just sum the path traversing level P+1
        # 2. Start summing level-wise from P+1 up to 1 (powers going from P to 0). If next-level-sum exceeds, a
            # until goal is reached. (what is the maximum amount of 1s we have to append? up to next power of two -1 if we do bottom up)
        # 3. When nextlevel + currentSum exceeds N, skip to next level (just adding the edge 1) and continue as normal.

    def closestPower(self, N):
        """Returns the power of 2 smaller or equal to N. e.g., if N=8 then p=3"""
        p = 0
        while (2**(p+1) <= N):  # return the smallest or equal power of 2
            p += 1
        return p

    def rowTraverse(self, right: bool, r: int):
        """Returns the order of positions visited along a level"""
        print("Adding row",r, "rowSum:", 2**(r-1))
        if right:   # we are on the right side, traverse from right to left
            return [(r, i) for i in range(r, 0, -1)]
        else:       # goes from left to right
            return [(r, i) for i in range(1, r + 1)]

    def pascalWalk(self, N):
        """_"""
        def rowSum(r):  # returns the sum value of a row
            return 2**(r-1)

        p = self.closestPower(N)    # power of two lower or equal to N
        if 2**p == N:
            return self.rowTraverse(False, p+1)      # the p+1 level sums exactly N

        currSum = 0
        r = p+1     # start at the level corresponding to power p
        path = list()   # we return a list of positions (row, index)
        right = False   # indicates if we are on the right side of Triangle
        # Traverse the rows (levels) descending from r to 1
        while currSum < N:
            print("currSum:",currSum)
            while (r > 0 and currSum + rowSum(r) <= N): # sum every next row r:0 while it does not exceed N
                currSum += rowSum(r)
                path.extend(self.rowTraverse(right, r))
                right = not right
                r -= 1
                print("currSum:",currSum)
            if currSum == N:
                print("Finished sum == N: ",currSum)
                return path
            elif r <= 0:
                return "Failed"
            # Else, we still have rows to sum.
            # Skip current row, only adding edge 1 to the path and Sum
            print("rowSum ",r,":", rowSum(r), "too large. Adding edge 1")
            if right:   # means we are in the right edge
                path.append((r, r))
            else:       # we are on the left edge
                path.append((r, 1))
            currSum += 1  # add edge one
            r -= 1      # move up again

        if currSum > N:
            return "Impossible"
        return path

    def main(self):
        for tc in range(int(input())):
            walk = self.pascalWalk(int(input()))
            print("Case #{}:".format(tc+1))
            for pos in walk:
                r, k = pos
                print(r, k)

PascalWalk().main()