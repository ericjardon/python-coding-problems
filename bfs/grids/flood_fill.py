'''
Given a 2-d array with integers representing different colored pixels in a grid,
and a special integer for a new color, fill in from the starting pixel with the 
given color, recoloring the previous color, checking in four directions from a 
given pixel in the grid.
Return the resulting grid.
'''


from collections import deque


def floodFill(image: list[list[int]], start: tuple, newColor: int) -> list[list[int]]:
    """
    Performs the flood fill algorithm on a given grid with integers as colors.
    Returns the modified grid.
    """
    def isvalidCell(row, col):
        """Utility function to determine if a given row and col exist"""
        return row >= 0 and row < len(image) and col >= 0 and col < len(image[0])

    r0, c0 = start
    oldColor = image[r0][c0]

    visited = set()
    q = deque()
    q.append(start)
    visited.add(start)

    x = [1, 0, -1, 0]
    y = [0, 1, 0, -1]

    while len(q):
        # Pop current pixel from queue
        cell = q.popleft()
        row, col = cell
        # For every direction up,down,left,right
        for i in range(4):
            r = row + y[i]
            c = col + x[i]
            # If cell exists
            if isvalidCell(image, r, c):
                # If pixel has not been visited yet
                if image[r][c] == oldColor and (r, c) not in visited:
                    image[r][c] = newColor

                    # Add to queue for later traversal
                    q.append((r, c))
                    visited.add((r, c))
    return image
