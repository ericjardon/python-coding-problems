'''
Given an adjacency list graph representing a Snakes & Ladders board, find the 
minimum moves necessary to win.

Strategy: view the board as a graph to explore with BFS-
From any vertex v we can move to v+1, v+2, v+3...
If any of the destination vertices has a snake or ladder pointing to 
a position X, then our final position is X.

The problem is reduced to finding Shortest Path between two nodes in 
a Directed GRaph.

Let the Board be a board with a start tile and N more tiles, where Snakes and Ladders are stored in
dict structure of source,dest key:value pairs


'''

from collections import defaultdict, deque


class Board:
    '''A simple directed graph representation using adjacency lists'''

    def __init__(self, edges: list[tuple[int, int]], N: int):
        self.adjList = [[] for _ in range(N)]

        for (src, dest) in edges:
            self.adjList[src].append(dest)


def solveSnakesAndLadders(snakes: defaultdict[int, int], ladders: defaultdict[int, int], N: int):

    # Stage 1: Construct the Board
    edges = []

    for tile in range(N):
        for dieroll in range(1, 7):

            dest = tile + dieroll
            if dest <= N:
                snake = snakes[dest]
                ladder = ladders[dest]

                if snake or ladder:
                    dest = snake or ladder

                edges.append((tile, dest))

    board = Board(edges, N)

    #  Stage 2. BFS on the resulting board
    return BFS(graph=board, N=N, start=0)


def BFS(graph: Board, N: int, start=0):
    """
    Performs BFS and returns the shortest path 
    Receives an S&L board as a graph, number of tiles and starting tile
    Tiles are numbered 1 through N inclusive
    """
    queue = deque()
    visited = [False for _ in range(N+1)]
    visited[start] = True
    queue.append((start, 0))  # enqueue tuples (vertex, min_moves)

    while queue:
        print("queue")
        vertex, min_cost = queue.popleft()
        if vertex == N:
            return min_cost

        for adj in graph.adjList[vertex]:
            if not visited[adj]:
                visited[adj] = True
                queue.append((adj, min_cost+1))


if __name__ == "__main__":
    snakes = defaultdict(int)   # default value returns 0
    ladders = defaultdict(int)
    # Record snakes in board
    snakes[17] = 7
    snakes[54] = 34
    snakes[62] = 19
    snakes[64] = 60
    snakes[87] = 36
    snakes[93] = 73
    snakes[95] = 75
    snakes[98] = 79
    # Record ladders in board
    ladders[4] = 14
    ladders[9] = 31
    ladders[21] = 42
    ladders[28] = 84
    ladders[51] = 67
    ladders[72] = 91
    ladders[80] = 99
    # assume board is 10x10 including start
    print("Min num of moves is {}".format(
        solveSnakesAndLadders(snakes, ladders, N=100)))
