'''
Given a binary matrix MxN of values 0 for water and 1 for land,
find the number of islands in it.
An island is formed by all connected cells of 1, horizontally,
vertically and diagonally.

Hint: though this is a Connected Components graph problem that could
be possibly solved with a Union-Find approach, it is also solvable with 
pure BFS.

1- start BFS from every unvisited land cell in the grid.
    if cell is visited, do not start a new BFS
2- each BFS will cover adjacent nodes so will detect a unique island
3- Total number of islands is equal to the number of unique searches made.
'''

from collections import deque


def CountIslands(matrix, M, N):
    visited = [[False for _ in range(N)] for _ in range(M)]
    islands = 0

    def isValidCell(row, col):
        return 0 <= row < M and 0 <= col < N and \
            matrix[row][col] == 1 and not visited[row][col]

    def BFS(row, col):
        queue = deque()
        queue.append((row, col))
        visited[row][col] = True

        directions = [
            (-1, 0),  # up
            (1, 0),  # down
            (0, 1),  # right
            (0, -1),  # left
            (-1, 1),  # up-right
            (1, 1),  # down-right
            (-1, -1),  # up-left
            (1, -1),  # down-left
        ]

        while queue:
            row, col = queue.popleft()
            for dr, dc in directions:
                r = row + dr
                c = col + dc
                if isValidCell(r, c):
                    visited[r][c] = True
                    queue.append((r, c))

    # Traverse every cell, start BFS if cell is unvisited Land
    for i in range(M):
        for j in range(N):
            if matrix[i][j] == 1 and not visited[i][j]:
                islands += 1
                BFS(i, j)  # BFS will cover all adjacent land cells

    return islands


if __name__ == "__main__":
    ex_grid = [
        [1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
        [0, 0, 1, 0, 1, 0, 1, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 1, 0, 0, 0],
        [1, 0, 0, 1, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
        [0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 0, 0, 1, 0, 0],
        [1, 1, 1, 1, 0, 0, 0, 1, 1, 1]]     # answer should be 5 islands

    # Time complexity of BFS solution is O(mxn)

    print(CountIslands(ex_grid, 10, 10))
