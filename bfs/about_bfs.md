# Breadth First Search

BFS is a technique for traversing a graph. 

It is commonly used for "Shortest Path" problems.
In BFS, the cells with shortest path length L are visited first, then adjacent cells with path length L+1 and so on.
Every node reached by a BFS algorithm has a path length equal to the previous node's path length +1. The first appearance of any cell in our traversal will necessarily give the shortest path to that cell.

_Note: in matrix-grids, we don't need Priority Queue (min heap) to extract the closest node to our position in an iteration, because all adjacencies to a given cell have same distance from cell. It would make more sense to use Pqueue if we were in an unweighted graph, so we can pop the closest distance node._