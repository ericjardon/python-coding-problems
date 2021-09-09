'''
Given an MxN matrix, representing a sensor-filled room that activates
death lasers, find the shortest path from any cell in the
leftmost column all the way to the righmost column.

Cell values are:
0 - represents a sensor. 8-way adjacent cells activate the sensor.
1 - represents an open, walkable cell

From starting position, you can only move in 4 ways.
You must return the length of shortest path from left to right 
that does not activate any sensors.

---Hint---
Since it is a Shortes Path problem it can be solved using BFS.
The added constraint is to avoid adjacent cells that may activate
a sensor. How do we identify these 'unsafe' cells?
We can preprocess the grid, marking with 0 any 8-way adjacent cell
to a sensor. Then we can perform a normal, obstacle-aware BFS.

Our search should stop when current column equals N-1.
'''
from collections import deque


def shortestSafePath(matrix, M, N):
    directions = [
        (1, 0),
        (0, 1),
        (-1, 0),
        (0, -1),
        (1, 1),
        (-1, 1),
        (1, -1),
        (-1, -1)
    ]

    # Pre-processing stage: tagging unsafe cells
    for i in range(M):
        for j in range(N):
            # If sensor found, tag adjacent cells
            if matrix[i][j] == 0:
                for r, c in directions:
                    rr = r+i
                    cc = c+j
                    if 0 <= rr < M and 0 <= cc < N and matrix[rr][cc] == 1:
                        matrix[rr][cc] = -1

    # BFS Stage: find shortest path
    queue = deque()
    visited = [[False for _ in range(N)] for _ in range(M)]

    for i in range(M):
        # If cell is safe, enqueue as possible starting cell
        if matrix[i][0] == 1:
            queue.append((i, 0, 0))  # tuple (row, col, cost)

    while queue:
        row, col, cost = queue.popleft()
        if col == N-1:
            return cost

        for k in range(4):
            dr, dc = directions[k]
            rr = row + dr
            cc = col + dc

            if 0 <= rr < M and 0 <= cc < N and\
                    not visited[rr][cc] and matrix[rr][cc] == 1:

                visited[rr][cc] = True
                queue.append((rr, cc, cost+1))

    # Destination is unreachable
    return float('inf')


if __name__ == "__main__":
    map = [
        [0, 1, 1, 1, 0, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    ]
    M = len(map)
    N = len(map[0])
    shortestLen = shortestSafePath(map, M, N)
    # 11 is correct
    print(f"Shortest distance of safe route is {shortestLen}")
