'''
Given a Maze represented by a rectangular grid of MxN cells, filled with
    'O' -- open cell
    'X' -- blocked cell
    'M' -- landmine (boom!)
Find the distance from every open cell to the nearest mine
**Note: Diagonal moves are not allowed. Cells containing a mine have 0 distance.
blocked cells & cells unreachable by a mine have -1 distance
-----
We solve this problem using Breadth first search starting from every possible
landmine, so that we find the shortest path to every other cell.
We enqueue a cell with the previous path cost (distance) +1 so we keep
track of the path's distance from a mine to any other cell.
The first time we reach an open cell, the assigned distance is 
necessarily from the closest (least cost) mine.
'''
from collections import deque


class LandmineDistance:
    def solve(self, map, M, N):
        # Use a 2d array to keep track of distances to each cell
        distance = [[-1 for _ in range(N)] for _ in range(M)]

        # Use two queues: one for the vertical index and another for horizontal
        qi = deque()
        qj = deque()        # this approach avoids packing-unpacking

        # Find and enqueue all cells with a landmine
        for i in range(M):
            for j in range(N):
                # If cell has a mine
                if map[i][j] == 'M':
                    qi.append(i)
                    qj.append(j)
                    # Base case: mines have distance zero to closest mine
                    distance[i][j] = 0

        # For exploring in four directions
        x = [1, 0, -1, 0]
        y = [0, 1, 0, -1]

        # Breadth First Search for every landmine.
        # The first landmine to update a cell is also the closest to it.
        while qi:   # qi and qj always have same length
            row = qi.popleft()
            col = qj.popleft()

            curr_dist = distance[row][col]

            for i in range(4):
                next_r = row + y[i]
                next_c = col + x[i]

                # If cell exists in map
                if (0 <= next_r < M) and (0 <= next_c < N):

                    # If cell is open and first time encountered, update distance to it
                    if map[next_r][next_c] == 'O' \
                            and distance[next_r][next_c] == -1:
                        distance[next_r][next_c] = curr_dist + 1

                        qi.append(next_r)
                        qj.append(next_c)

        # Return the map of all distances
        return distance


if __name__ == "__main__":
    example_maze = ["O M O O X",
                    "O X X O M",
                    "O O O O O",
                    "O X X X O",
                    "O O M O O",
                    "O X X M O"]
    M = len(example_maze)
    for r in range(M):      # turn rows into arrays
        example_maze[r] = example_maze[r].split(' ')
    N = len(example_maze[0])
    for row in LandmineDistance().solve(example_maze, M, N):
        print(row)
