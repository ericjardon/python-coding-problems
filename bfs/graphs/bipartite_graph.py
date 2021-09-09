'''
PROBLEM: Given an undirected graph, determine if it is Bipartite or not.

A Bipartite Graph is one that consists of exactly 2 disjoint sets, U and V, 
such that every node u in U connects to a node v in V. (also known as 2-colorable graphs).
No node in U is connected to any other node in U, and no node in V is connected to any node in V.

Bipartite graphs could represent a set of Cars and Persons, connected by ownership relationships.

---Hint---
We can use BFS to find whether a graph is bipartite. 
As we construct the bfs tree, every parent is given a color and every child of a node is given another color. 
If we find a child node with the same color as the parent, then it cannot be 2-colorable, 
and thus is NOT bipartite.

Any given node can only be connected to a differently-colored node.
Colors are used for visual explanation; they could be labels too.

A curious observation: in the bfs tree of a bipartite graph, 
even levels are one color and odd levels are another.
'''
from collections import deque
from graphs import UndirectedGraph


def isBipartite(ugraph: UndirectedGraph, start, N):
    """
    Receives an adjacency list undirected graph of N nodes labeled 0..N-1
    Returns a boolean indicating if the graph is 2-colorable or not
    """
    queue = deque()
    visited = [False for _ in range(N)]
    color = [0 for _ in range(N)]
    color[start] = 1
    queue.append(start)

    while queue:
        vertex = queue.popleft()

        for adj in ugraph.adjList[vertex]:
            if not visited[adj]:
                visited[adj] = True
                color[adj] = color[vertex] * -1
                queue.append(adj)

            elif color[adj] == color[vertex]:
                return False

    # No parent-child pair with same color found, thus the graph is 2-colorable
    return True


if __name__ == "__main__":
    edges = [
        (1, 2), (2, 3), (2, 8), (3, 4), (4, 6), (5, 7), (5, 9), (8, 9)
    ]       # edge (2,4) makes it non bipartite

    N = 10  # Max node label is 9
    graph = UndirectedGraph(edges, N)
    if isBipartite(graph, 1, N):
        print("\nGraph is bipartite.")
    else:
        print("\nGraph is NOT bipartite.")
