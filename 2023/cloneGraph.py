from collections import deque

class Node(object):
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        # Adjancency list: node.val, node.neighbors
        # For simplicity every node is indexed
        # Store cloned nodes in an array
        if node is None: return None

        clone = {} # int->Node
        ref = node.val

        # Breadth first search
        # a node is skipped when it has already been expanded

        expanded = set()

        q = deque()
        q.append(node)

        while q:
            n = q.popleft()
            if n in expanded:
                continue

            # Create clone if not exists
            if n.val not in clone:
                clone[n.val] =  Node(val=n.val, neighbors=[])

            # Traverse neighbors of n
            for neighbor in n.neighbors:
                # Create neighbor clone if not exists
                if neighbor.val not in clone:
                    clone[neighbor.val] = Node(val=neighbor.val, neighbors=[])
                
                # Add edge to clone graph
                clone[n.val].neighbors.append(clone[neighbor.val])

                # Add neighbor to queue
                q.append(neighbor)

            expanded.add(n)
    
        return clone[ref]

def checkGraphIsDeepClone(g1, g2):
    # Check if two graphs are deep clones
    # g1, g2 are Node objects
    # Return True if they are deep clones
    # Return False otherwise
    if g1 is None and g2 is None:
        return True

    if g1 is None or g2 is None:
        return False

    if g1.val != g2.val:
        return False

    if g1 is g2:    # should be different objects
        print("ERROR: same objects", g1.val, g2.val)
        return False

    if len(g1.neighbors) != len(g2.neighbors):
        return False

    for i in range(len(g1.neighbors)):
        if g1.neighbors[i].val != g2.neighbors[i].val:
            return False
        if g1.neighbors[i] is g2.neighbors[i]:
            print("ERROR: same objects", g1.neighbors[i].val, g2.neighbors[i].val)
            return False

    return True

def printAdjacencyList(nodes):
    for n in nodes:
        print("node", n.val, [x.val for x in n.neighbors])


if __name__ == "__main__":
    N = 4
    nodes = []
    for i in range(N):
        nodes.append(Node(val=i))

    # [[2], [1,3], [2]]
    nodes[0].neighbors = [nodes[1]]
    nodes[1].neighbors = [nodes[2]]

    copy = Solution().cloneGraph(nodes[0])
    print(checkGraphIsDeepClone(nodes[0], copy))
