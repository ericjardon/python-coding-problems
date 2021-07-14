'''
Given a Square Matrix (grid), find the shortest path from (0,0) 
to the cell (N-1,N-1), where at any given cell with value K, 
you can ONLY MOVE K steps in either of the four directions.
Return the shortest path possible from start to end cells.
----
We can do a BFS search to find all possible paths and stop once we reach
the destination. To reconstruct the path traversed we can implement
a utility class that has a pointer to its parent or previous cell.

We always instantiate a new Cell when we reach it in the grid. At the end
we return the destination cell, and iteratively print out the path.

'''
from collections import deque  # as is common for BFS algorithms


class Cell:
    """
    Utility class for reconstructing the shortest path found
    by our BFS algorithm
    """

    def __init__(self, row, col, parent):
        self.r = row
        self.c = col
        self.parent = parent

    def __repr__(self):
        return str((self.r, self.c))

    def getKey(self):
        return (self.r, self.c)


def getBestPathKSteps(grid: list[list[int]], N: int) -> Cell:

    # Initialize an empty queue, enqueue starting cell with 0 distance from start
    q = deque()
    start = Cell(row=0, col=0, parent=None)
    q.append(start)

    visited = set()

    # Available moves
    y = [1, 0, -1, 0]
    x = [0, 1, 0, -1]

    while q:
        current_cell = q.popleft()
        row, col = current_cell.getKey()

        # Number of possible steps we can take
        k = int(grid[row][col])

        # If we reached destination cell return it
        if row == N-1 and col == N-1:
            return current_cell

        # Else, for every possible direction
        for i in range(4):
            # Compute next cell to visit
            next_row = row + y[i]*k
            next_col = col + x[i]*k

            # if cell exists in map
            if (0 <= next_row < N) and (0 <= next_col < N):

                # Instantiate next Cell with current cell as parent
                next_cell = Cell(row=next_row, col=next_col,
                                 parent=current_cell)

                # If the next cell has not already been visited, enqueue it
                if next_cell.getKey() not in visited:
                    visited.add(next_cell.getKey())
                    q.append(next_cell)

    # Destination cell is unreachable, return no cell
    return None


def getPath(lastCell: Cell) -> list[Cell]:
    """
    Iteratively prints out the path from root cell, given the destination cell.
    """
    path = []

    while (lastCell is not None):
        path = [lastCell] + path
        print(path)
        lastCell = lastCell.parent

    return path


def shortestKSteps(grid: list[list[str]], N: int):
    lastCell = getBestPathKSteps(grid, N)
    print("last cell", lastCell)

    path = getPath(lastCell)

    if len(path) == 0:
        print("Destination is unreachable")
    else:
        for cell in path:
            print(cell, end=" ")
        print(f"Minimum number of moves is {len(path)-1}")


if __name__ == "__main__":
    example_grid = [
        "4 4 6 5 5 1 1 1 7 4",
        "3 6 2 4 6 5 7 2 6 6",
        "1 3 6 1 1 1 7 1 4 5",
        "7 5 6 3 1 3 3 1 1 7",
        "3 4 6 4 7 2 6 5 4 4",
        "3 2 5 1 2 5 1 2 3 4",
        "4 2 2 2 5 2 3 7 7 3",
        "7 2 4 3 5 2 2 3 6 3",
        "5 1 4 2 6 4 6 7 3 7",
        "1 4 1 7 5 3 6 5 3 4"
    ]

    for row in range(len(example_grid)):
        example_grid[row] = example_grid[row].split(' ')

    shortestKSteps(example_grid, len(example_grid))
