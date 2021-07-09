'''
Find the number of possible topological orderings of a Directed Acyclic Graph.
Topological Ordering of a Graph: a linear listing of nodes such that the first node has
no edge coming into it, and the last node has edge coming out. For every edge (vi -> vj) 
of the graph that appears on the list, the i-th node comes before the j-th node (i<j).
----
Kahn's Topological Sort:
- pick a vertex with no incoming edge (in-degree zero)
- remove its outcoming edges from the graph.
- vertices now having in-degree zero are valid candidates for next position.
- For every position in the topological ordering we may have c candidates.
- The number for total orderings is given by c0*c1*c2*...*cn-1

We use backtracking and recursion. The strategy of reusing one single array `order_so_far`
for all possibilities allows to save up a lot of space
'''


class Digraph:
    def __init__(self, N: int, edges: list[tuple] = []) -> None:
        """Node keys are labeled 0:N-1"""
        self.adjLists = [[] for _ in range(N)]
        self.indegrees = [0 for _ in range(N)]

        for u, v in edges:
            self.adjLists[u].append(v)
            self.indegrees[v] += 1
            # outdegrree is equal to the length of a node's adjacency list


class TopologicalOrderings:
    """
    Solves the problem of counting possible topological orderings
    of a Directed Acyclic Graph.
    """

    def __init__(self) -> None:
        self.count = 0

    def printAllOrderings(self, graph: Digraph):
        self.count = 0
        N = len(graph.adjLists)
        included = [False for _ in range(N)]
        order_so_far = []
        self.solve(graph, order_so_far, included, N)

    def solve(self, graph: Digraph, order_so_far: list[int], included: list[bool], N) -> None:
        """
        Recursive function for finding all topological orderings of a given DAG with numbered nodes.
        * graph: graph to traverse;  
        * path_so_far: partial ordering constructed up to now. It is modified in and out of recursion
        * included: memory structure to track which nodes are not in the ordering yet;
        * N: total number of nodes
        """

        # Loop over all vertices to find next candidate to append to ordering
        for vertex in range(N):
            # If indegree is 0 and it is not in our ordering
            if graph.indegrees[vertex] == 0 and not included[vertex]:

                # 'remove' the edges of vertex by decreasing its neighbors' indegrees
                for neighbor in graph.adjLists[vertex]:
                    graph.indegrees[neighbor] -= 1

                order_so_far.append(vertex)
                included[vertex] = True

                self.solve(graph, order_so_far, included, N)

                # BACKTRACK:
                # restore the edges of vertex by increasing neighbor's indegrees
                for neighbor in graph.adjLists[vertex]:
                    graph.indegrees[neighbor] += 1

                # remove current vertex from current position, mark it as not included
                order_so_far.pop()
                included[vertex] = False

                # in the next iteration this position will be occupied by a different vertex

        # After loop ends, no more candidate vertices left to add to ordering.
        # If all nodes are present in the ordering, count as valid ordering
        if len(order_so_far) == N:
            self.count += 1
            print(order_so_far)


if __name__ == "__main__":
    edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0),
             (3, 4), (5, 1), (7, 0), (7, 1)]
    N = 8       # max label is 7
    graph = Digraph(N, edges)
    to = TopologicalOrderings()
    to.printAllOrderings(graph)

    print(f"Total orderings = {to.count}")
