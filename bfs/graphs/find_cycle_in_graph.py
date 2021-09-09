'''
Given an undirected graph (having bidirectional edges), determine if it contains
a cycle or not.

--- Hint ---
A cross-edge is an edge pointing to an already visited node which is neither descendant nor ancestor of the current vertex
within the BFS Tree.
If we detect a cross-edge in an undirected graph, then there is a cycle in the graph.

Let v be the root of the BFS tree. A cross edge x->y is found if y was already visited and y is not the parent of x.
Why? we know there is a path such that v->y (and since the graph is undirected, there is also a path y->v). Because there
is also a path such that v->x, then we conclude v->x->y->v (a cyclic path) and the same is true in the opposite direction.
'''
from collections import deque


class UndirectedGraph:
    """Implements an undirected graph with nodes labeled with indices 0..N-1"""

    def __init__(self, edges: list[int], N: int) -> None:
        """
        Use an adjacency list for every node.
          edges -- a list of tuples (u,v); 
          N -- the number of nodes in graph
        """
        self.adjList = [[] for _ in range(N)]
        for (src, dest) in edges:
            self.adjList[src].append(dest)
            self.adjList[dest].append(src)  # bidirectional edges


def containsCycle(ugraph: UndirectedGraph, start: int, N: int) -> bool:
    queue = deque()
    queue.append((start, -1))  # enqueue tuples (node, parentNode)
    visited = [False for _ in range(N)]
    visited[start] = True

    while queue:
        vertex, parent = queue.popleft()

        for adj in ugraph.adjList[vertex]:
            # If adjacency has been visited and is not the parent node, it's a cross edge
            if visited[adj] and parent != adj:
                return True

            visited[adj] = True
            queue.append((adj, vertex))

    # No cross-edges found
    return False


if __name__ == "__main__":
    edges = [
        (1, 2), (1, 3), (1, 4), (2, 5), (2, 6), (5, 9),
        (5, 10), (4, 7), (4, 8), (7, 11), (7, 12), (6, 10)
        # our cycle is given by cross-edge 6-10: 10->5,5->2,2->6,6->10*
    ]
    N = 13  # max label is 12, so we need 13 node slots
    graph = UndirectedGraph(edges, N)
    if containsCycle(graph, 1, N):
        print("Graph has cycle.")
    else:
        print("Graph has no cycles.")
