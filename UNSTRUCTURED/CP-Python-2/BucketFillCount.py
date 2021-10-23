# A Bucket tool recolors adjacent (horizontal, vertical only) cells.
# Given a picture as a 2d array, find the min number of fills to
# completely repaint the picture.

# we can use a counter of cells to know when that count is equivalent to the
# area of the image. When the counter equals the area we have finished.
## NOTE: This problem was solved for the FB2021 hack qualification challenge

# we can use BFS to simulate the recoloring
from collections import deque
def strokesRequired(picture):
    def validCell(i, j):
        return 0 <= i < m and 0<=j<n

    def bfs(r, c, color, visited):
        q = deque()
        q.append((r,c))
        visited[r][c] = True
        x = [1,0,-1,0]
        y = [0,1,0,-1]
        while q:
            r, c = q.popleft()
            for i in range(4):
                    next_r = r + x[i]
                    next_c = c + y[i]
                    if validCell(next_r, next_c):    # if cell is within picture is not repainted
                        if visited[next_r][next_c]:
                            continue
                        if picture[next_r][next_c] == color:
                            q.append((next_r, next_c))
                            visited[next_r][next_c] = True

    strokes = 0
    m = len(picture)
    n = len(picture[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if not visited[i][j]:
                bfs(i,j, picture[i][j],visited)
                strokes += 1
    return strokes

if __name__ == '__main__':
    picture = ["aabba",
               "aabba",
               "aaacb"]
    picture2 = ["aaaba",
                "ababa",
                "aaaca"]
    picture3 = ["bbbbb"]
    print(strokesRequired(picture))
    print(strokesRequired(picture2))
    print(strokesRequired(picture3))
