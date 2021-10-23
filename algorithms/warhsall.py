'''
WARSHALL'S ALGORITHM
Is used to find the _transitive closure_ of a graph.

->The transitive closure of a directed graph is a binary matrix
that tells of the existence of a directed path of positive length
between the ith node and the jth node.

In constant time, the transitive closure allows us to determine if I can reach
a node j from a node i.
Ex )An application is spreadsheet software: if related cells of the sheet
are modeled after a digraph, we can know which cells are affected
when any cell is modified if there exists a path between them.
Ex 2 ) Another application is OO-software for testing inheritance relationships. 

The transitive closure can be found using either DFS or BFS. This is the naive method,
traversing the graph entirely starting from all of the i-th node's neighbors.

The better method is defined by Warhall's Algorithm.
'''

# Let n be the number of vertices n a directed graph.
# Label the nodes from 1 to n.
# We generate a series of nxn matrices, called R_k [1..n]
# where each R_i is a special adjacency matrix, where an entry
# [i,j] = 1 indicates there exists a path between i and j with every intermediate node
# NOT higher than k, subindex of matrix.
# Notice R_0 is the ordinary adjacency matrix.
# R_k, or R_n, consideras all other nodes in the graph as intermediate
# so is nothing more thant the transitive closure of the graph.

# The series of matrices from R_0 to R_n are computed in sequence, one after
# the other.
# A matrix R_k can be directly derived from R_(k-1) by using a simple rule:
#   R_k(i,j) = R_j(i,j) if R_j(i,j)==1,  which means the existing path i->j does not include k;
#   LOGICAL OR
#   R_k(i,j) = R_k-1(i,k) && Rk-1(k,j), meaning k is an intermediate; i.e. i->k->j


def warshall(adjacencyMatrix):
    """Computes the transitive closure of a given 
    adjacency matrix for a directed graph"""
    N = len(adjacencyMatrix)
    R_curr = adjacencyMatrix
    for k in range(N):
        R_next = R_curr

        for i in range(N):
            for j in range(N):
                # There is a path i->j if there previously was one, OR
                # if there is a path i->k and k->j
                R_next[i][j] = R_curr[i][j] or (R_curr[i][k] and R_curr[k][j])

        R_curr = R_next

    return R_curr

if __name__=="__main__":
    adj = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]

    print(warshall(adj))