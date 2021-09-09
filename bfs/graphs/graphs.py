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
