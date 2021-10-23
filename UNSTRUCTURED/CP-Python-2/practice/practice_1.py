# https://codeforces.com/gym/103150


# 1) Addition Range Queries
# Given an array of N integers, we have to perform K operations.
# Each operation consists on replacing the i-th element by the sum
# of all other elements in the array.
# After k operations, find the maximum absolute difference between two elements.
class AdditionRangeQueries:
    """Solves the Addition Range Queries problem"""

    def solve(self, n, k, array):
        """
        Outputs the max difference after k operations.
        """

        # Last pass to find max difference
        min_val = array[0]
        max_val = array[0]
        for i in range(len(array)):
            min_val = min(min_val, array[i])
            max_val = max(max_val, array[i])
        print(max_val - min_val)


    def main(self):
        """Driver program"""

        T = int(input())        # testcases: 1,10^4
        for t in range(T):
            n, k = [int(x) for x in input().split()]
            array = [int(x) for x in input().split()]
            self.solve(n, k, array)
    # the sum of n over test cases is not larger than 2*10^5

AdditionRangeQueries().main()
# Conclusion: it so happens that the max difference does not change after k operations.
# Every number is incremented equally at every operation. DO NOT be fooled by problem statement



# 2) Arrowing Process
# We have a grid nxm containing arrows in every cell.
# A move consists of swapping two adjacent arrows pointing at each other.
# What is the maximum number of moves that can be performed?
from collections import deque
   # deque is a doubly linked queue, provides append and popleft ops
class ArrowingProcess:
    def __init__(self):
        a = dict()
        a['>'] = 1
        a['<'] = -1
        a['^'] = 2
        a['v'] = -2

        self.a = a

    def check(self, c1, c2):
        return self.a[c1] + self.a[c2] == 0

    def solve(self, n, m, grid):
        pass

    def main(self):
        """Driver program"""
        T = int(input())

        for t in range(T):
            n, m = [int(x) for x in input().split()] # both less than 1000
            grid = []
            for _ in range(n):
                row = input()
                grid.append(row)

            self.solve(n, m, grid)


