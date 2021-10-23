from collections import deque
from collections import defaultdict
import heapq



## PROBLEM: Directory Traversal using BFS
class File:
    def __init__(self, name, contents=None):
        self.name = name        # "/root/file"
        self.contents = contents   # List of other File objects
    def isDirectory(self):
        return self.contents is not None
    def listFiles(self):
        return self.contents
    def __repr__(self):
        return str(self.name)

class TraverseDirectory:
    """Given a directory of files, traverese and list out all the files
        present in it, as well as its subdirectories."""
    def traverseDir(self, rootDir: File):
        # 1. Create empty queue of Files. enqueue root directory.
        # 2. Loop through the queue until empty so all files & directories are processed.
        # 2.1 at each queue item:
        #   - pop item from queue
        #   - if item is directory, get list of all its contents, and enqueue it
        #   - if item is a file, print it to console
        q = deque()
        # no need for 'visited' structure since directory is inherently a tree
        q.append(rootDir)
        while q:
            curr = q.popleft()
            for file in curr.listFiles():
                if file.isDirectory():
                    q.append(file)
                else:
                    print(file)
    def main(self):
        f1 = File("/home/users/eric/index.js")
        f2 = File("/home/apps/PyCharm.exe")
        f3 = File("/home/users/eric/global.css")
        f4 = File("/home/apps/Chrome.exe")
        d1 = File("/home/users/eric", [f1,f3])
        d2 = File("/home/users/", [d1])
        d3 = File("/home/apps/", [f2, f4])
        d4 = File("/home/",[d2,d3])
        self.traverseDir(d4)
#TraverseDirectory().main()


## PROBLEM: Determine if a Binary Tree is Complete Binary Tree
# Complete Binary Tree: in every level except the last is completely filled.
                    #   all nodes are as far left as possible
class Node:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CheckCompleteness:
    """BFS level-order traversal: for every dequeued node check if it has both children.
      If a node without children or only 1 child, then every remaining node in queue SHOULD NOT
      have any children.
      NOTE: this version uses Node-based representation of Tree """
    def isComplete(self, root: Node):
        if root is None:        # empty trees by definition are not complete
            return False
        queue = deque()
        queue.append(root)
        flag = False    # marks end of full-node levels

        while queue:
            n = queue.popleft()
            if flag and n.right and n.left:
                # All nodes after first incomplete node should not have complete children
                return False    # tree is not a complete tree
            if n.left is None and n.right:
                return False   # nodes should be leftmost
            if n.left is None or n.right is None: # the node is incomplete:
                flag = True
            # node is incomplete: at least right node is missing
            if n.left:
                queue.append(n.left)
            if n.right:
                queue.append(n.right)

        return True     # no partially-complete nodes after flag was set

    def main(self):
        """ Construct below tree
                      1
                   /     \
                  2       3
                 / \     / \
                4   5   6   7
                                """
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        if self.isComplete(root):
            print("Binary Tree is Complete")
        else:
            print("Given Binary is not Complete")

# CheckCompleteness().main()

class CheckCompletenessArray:
    """Same as above but with Solution with Array-representation of Tree"""
    # A complete binary tree has certain convenient properties
    # when transformed into an array:
    # - Node at index i has its children at indexes 2*i+1 and 2*i+2
    # - If we try to construct an array from the tree then all the elements
    #   should hold consecutive positions (no gaps in array).
    # Hence, if a gap is found of the transformed array it can't be a complete tree.
    def size(self, root):   # returns size of array
        if root is None:
            return 0
        return 1 + self.size(root.left) + self.size(root.right)

    # Performs in-order traversal of tree (left, root, right),
    # marking an index as filled or not (by a node)
    def inorder(self, root, Array, i):
        if root is None or i >= len(Array):
            return
        self.inorder(root.left, Array, 2 * i + 1)
        Array[i] = True
        self.inorder(root.right, Array, 2 * i + 2)

    def isComplete(self, root, n):
        Array = [False for _ in range(n)]
        # Traverse the tree and populate as True where nodes exist
        self.inorder(root, Array, 0)
        for node in Array:
            if not node:
                return False
        return True
    # This solution approach is Linear

class WeightedGraph:
    def __init__(self, edges, N, undirected=False):
        self.adjList = [[] for _ in range(N)]
        for u, v, w in edges:
            self.adjList[u].append((v, w))
            if undirected:
                self.adjList[v].append((u,w))


class PrimLazy:
    """Implementation of Prim's lazy algorithm for finding Minimum Spanning Tree"""
    def main(self):
        edges = [
            (0,1,10),(0,2,1),(1,4,0),(1,2,3),(2,3,2),(2,5,8),(5,7,9),(5,6,6),
            (3,6,7),(4,5,1),(4,7,8),(6,7,12), (0,3,4), (3,5,2)
        ]
        N = 8
        g = WeightedGraph(edges, N, True)
        mst, cost = self.primMST(g, N, 0)
        print("MST cost:", cost)
        for w,u,v in mst:
            print(f"  {u}->{v} : {w}")

    def primMST(self, graph, N, start):
        visited = [False for _ in range(N)]
        pq = list()     # priority queue stores the edges by lowest cost
        # 1. Push all edges of starting node to priority queue
        visited[start] = True
        for vertex, cost in graph.adjList[start]:
            heapq.heappush(pq, (cost, start, vertex))       # cost goes first in tuple
        m = N-1     # a tree has N-1 edges by definition
        MST = list()        # return a list of edges
        mst_cost = 0
        # 2. # BFS to pick the next lowest-cost edge
        while pq and len(MST) != m:         # while queue is not empty and mst is unfinished
            # 2.1 pop the minimum edge
            w, u, v = heapq.heappop(pq)     # cost, from, to
            # 2.2 if the edge points to visited node, skip
            if visited[v]:
                continue
            # 2.3 Else, add the edge to the solution, mark as visited and enqueue all edges of new node
            MST.append((w,u,v))
            mst_cost += w
            visited[v] = True
            for vertex, cost in graph.adjList[v]:
                heapq.heappush(pq, (cost, v, vertex))

        if len(MST) != m:       # queue empty but mst unfinished
            print("No spanning tree found")
            return None, None
        return MST, mst_cost


if __name__ == '__main__':
    PrimLazy().main()