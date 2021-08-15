'''
Find the path of Minimum Cost in a Grid with cost values per cell.

Given an MxN matrix Cost[M][N] where Cost[i][j] represents the
cost of visiting the cell (i,j).
Find the path from (0,0) to a given destination cell (x,y)
that has minimum total cost, provided you can only move in two
directions, either down or right.
All costs are positive.

Hint:
The minimum cost at any given cell is equal to  current cell's cost.
plus the minimum accumulated cost from either the upper or left neighbor cells

Recurrence Relation:
minCost(i,j) = min(minCost(i-1, j), minCost(i, j-1)) + cost[i][j]

'''


class MinCostGrid:
    def solve(self, N, M, cost, x, y):
        """
        Solves the min cost path problem with a Dynamic Programming,
        bottom up approach. 
        Using bottom up guarantees that all subproblems of an instance
        have already been solved.
        """

        # Sanity check. Is (x,y) reachable?
        if x >= M or y >= N:
            return

        minCost = [[0 for _ in range(M)] for _ in range(N)]

        # Base case
        minCost[0][0] = cost[0][0]

        # Top row and leftmost column are single-move paths
        for j in range(1, M):
            minCost[0][j] = minCost[0][j-1] + cost[0][j]
        for i in range(1, N):
            minCost[i][0] = minCost[i-1][0] + cost[i][0]

        # Populate min cost table
        for i in range(1, N):
            for j in range(1, M):
                fromUp = minCost[i-1][j]
                fromLeft = minCost[i][j-1]

                # Recurrence relation
                minCost[i][j] = min(fromUp, fromLeft) + cost[i][j]

        print(f"Min cost to ({x},{y}) is {minCost[x][y]}")

    def main(self):

        for testcase in range(int(input())):
            # Input N, M values
            N, M = [int(x) for x in input().split()]
            cost = []

            # Input cost grid
            for _ in range(M):
                row = [int(x) for x in input().split()]
                cost.append(row)

            x, y = [int(x) for x in input().split()]
            self.solve(N, M, cost, x, y)


'''
1
5 5
1 3 4 2 6
4 2 6 3 6
9 10 12 15 1
3 4 5 2 10
12 12 12 12 12
3 3

'''
# Example answer is 27

MinCostGrid().main()
