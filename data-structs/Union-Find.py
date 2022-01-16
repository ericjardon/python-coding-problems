from typing import List
## UNION-FIND

# Count Components problem given a graph's adjacency matrix
def countComponents(n : int, edges: List[List[int]]):
    """
        n: number of nodes in graph, or dimension of edges
        edges: list of edges [u, v]
    """
    membership = [x for x in range(n)]      # every element starts by its own

    # Loop through all edges and union the connected nodes
    for u, v in edges:
        union(u, v, membership)
        # at the end of loop the membership array holds only distinct set representatives

    # To count components is to count distinct parents
    parents = set()
    for p in parents:
        if p not in parents:
            parents.add(p)

    return len(parents)

def union(u:int, v:int, parents:List[int]) -> None:
    """Put in the same set by assigning the parent of v as parent of parent of u"""
    parentU = find(u, parents)
    parentV = find(v, parents)
    parents[parentU] = parentV

def find(v:int, parents:List[int]):
    """Find and return the representative node (set membership) of v"""
    if parents[v] == v:    # if v is a representative of set
        return v
    else:
        # recursively find the representative and reassign in parents array (path compression)
        parents[v] =  find(parents[v], parents)
        return parents[v]