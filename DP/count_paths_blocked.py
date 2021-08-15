'''
ROBOTS & PATHS
Essentially a version of count all paths but with obstacles in cells.

Given an MxN matrix and a number B of blocked cells.
Determine num of possible ways to reach from cell (0,0)
an end position (x,y) provided you can only move down or right.

Blocked cells are represented by -1. Available cells contain 0

The only difference in the solution is a couple more checks to visit a cell.
'''


from typing import Mapping


def count_paths_blocked(M, N, grid, x, y, start=(0, 0)):
    xi, yi = start

    # Starting position is blocked
    if grid[xi][yi] < 0:
        return

    # End position is blocked
    if grid[x][y] < 0:
        return

    # End position is unreachable
    if x < xi or y < yi or x >= M or y >= N:
        return

    paths = [[0 for _ in range(N)] for _ in range(M)]

    # Leftmost column
    for i in range(xi, M):
        if grid[i][0] < 0:
            break

        paths[i][0] == 1

    # Top row
    for j in range(yi, N):
        if grid[0][j] < 0:
            break
        paths[0][j] = 1

    # Populate paths table
    for i in range(1, M):
        for j in range(1, N):
            if grid[i][j] < 0:
                continue

            aboveCell = grid[i-1][j]
            leftCell = grid[i][j-1]

            # If preceding cell is available add the number of possible paths to it
            if aboveCell >= 0:
                paths[i][j] += paths[i-1][j]

            if leftCell >= 0:
                paths[i][j] += paths[i][j-1]

            print(f"From ({xi},{yi}) to ({x},{y})")
            print(f"Number of possible paths = {paths[x][y]}")


if __name__ == "__main__":
    # Input dimensions and number of blocked cells
    M, N, B = [int(x) for x in input().split()]

    grid = [[0 for _ in range(N)] for _ in range(M)]

    for cell in range(B):
        r, c = [int(x) for x in input().split()]
        grid[r][c] = -1

    x, y = [int(x) for x in input().split()]

    # start_x = int(input())
    # start_y = int(input())
    # start = (start_x, start_y)

    print(count_paths_blocked(M, N, grid, x, y))
