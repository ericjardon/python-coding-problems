'''
NUMBER OF POSSIBLE PATHS 

Given a 2d matrix of M cols and N rows, find the num of
possible paths to reach a cell (x,j) from starting cell (0,0),
provided that moves can only be right or down.

Hint:
In a DP approach, the number of ways to reach a cell is equal to the
sum of the number of ways of reaching the upper and left neighbor cells. 

Recurrence relation:
paths[i][j] = paths[i-1][j] + paths[i][j-1]

BASE:
For all cells in top row and leftmost column, paths = 1.
'''


def count_possible_paths(M, N, grid, x, y):
    """
    Solves the number of possible paths problem in a bottom-up DP approach.
    Receives a 2d array, and destination cell's row and col coordinates x, y
    """

    paths = [[1 for _ in range(N)] for _ in range(M)]

    for i in range(1, M):
        for j in range(1, N):
            paths[i][j] = paths[i-1][j] + paths[1][j-1]


if __name__ == "__main__":
    N, M = [int(x) for x in input().split()]

    grid = []
    for _ in range(M):
        row = [int(x) for x in input().split()]
        grid.append(row)

        x, y = [int(x) for x in input().split()]

    print(count_possible_paths(N, M, grid, x, y))
