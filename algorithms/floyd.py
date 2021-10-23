'''
FLOYD'S ALGORITHM
All-nodes shortest paths problems.

For an N-node graph, use a distance matrix nxn where the i,j entry 
indicates the path cost from i to j.


Floyd was deeply influenced by Warshall's algorithm to compute the
minimum Distance matrix.

Applicable to both directed and undirected graphs as long as 
there are no negative-length loops.
The algorithm can be tweaked to return the sequence of shortest paths too.

We compute a series of matrices D1..Dn.
The final Distance Matrix Dk is computed after a series of matrices D0, D1...
just like in warshall's.
Same rules apply: the identifier k of a matrix is the maximum vertex id allowed 
for the intermediate path. 
D0 hence is the ordinary weight matrix of the graph (adjacency matrix of a weighted graph).
Dn hence contains the lengths of shortest paths that can use all n nodes in the path.
'''

# A given path in Dk is [vertex i, ...intermediates not higher than k..., vertex j]
# Entry Dk[i,j] is the minimum cost

def floyd(weightMatrix):
    """
    Computes the min distance matrix for a given
    weight matrix of a graph
    """
    N = len(weightMatrix)
    Dcurr = weightMatrix
    for k in range(N):
        Dnext = Dcurr

        for i in range(N):
            for j in range(N):
                # Pick the min distance between previously stored distance
                # and distance of path i->k->j (non existing paths are infinitely weighted)
                Dnext[i][j] = min(Dcurr[i][j], Dcurr[i][k] + Dcurr[k][j])

    return Dcurr


if __name__=="__main__":
    adj = [
        [0, 1, 0, 0],
        [0, 0, 0, 1],
        [0, 0, 0, 0],
        [1, 0, 1, 0]
    ]

    inf = float('inf')

    W = [
        [0, inf, 3, inf],
        [2, 0, inf, inf],
        [inf, 7, 0, 1],
        [6, inf, inf, 0]
    ]

    print(floyd(W))
