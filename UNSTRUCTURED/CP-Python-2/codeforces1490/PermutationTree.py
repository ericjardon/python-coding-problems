# Permutation: a sequence of n numbers (1-n) occurring exactly once.

# Given a permutation, transform it into a binary tree and for each vertex v
# return the depth of that vertex (# of edges from root to v)

# Note: the max (root node) is always n. Look for n, then look for n-1, and so on.
# Preprocess the array to know which value is in which index.
# Then construct the binary tree and do dfs to find the depth of each.
# return an array with the ith vertex depht in the ith position

class TreeNode:
    def __init__(self, key=None, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self, level=0):
        tree = "\t"*level + str(self.key) + "\n"
        if self.right:
            tree += self.right.__str__(level+1)
        if self.left:
            tree += self.left.__str__(level+1)
        return tree

def buildTree(pos, A, n):
    inserted=set()
    root = TreeNode(n)
    depths = [0 for _ in range(n)]

    def build(parent, min_i, max_i, d):
        if len(inserted) == n or min_i==max_i:
            return
        parent_i = pos[parent.key]
        #print("Start recursion for parent", A[parent_i])
        #print("Left:", A[min_i:parent_i])
        # Do left if there are elems to the left
        if A[min_i:parent_i]:      # if there are elements to the left of i
            l = parent.key - 1      # find next max key to the left of i
            while l in inserted or pos[l]<min_i or pos[l]>=parent_i:   # l within boundaries and uninserted
                l -= 1
            #print("max key:", l)
            if l>0:
                parent.left = TreeNode(l)
                depths[pos[l]] = d+1
                inserted.add(l)
                #print("inserted", l)
                build(parent.left, min_i, parent_i, d+1)        # recur on left subarray A[0,i]

        #print("Right:", A[parent_i+1:max_i])
        # Do right if there are elems to the right
        if A[parent_i+1:max_i]:
            r = parent.key - 1      # candidate key for right subtree (within boundaries and uninserted)
            while pos[r]<parent_i+1 or pos[r]>=max_i or r in inserted:   # find next max key to the right of i
                r -= 1
            #print("max key:", r)
            if r>0:
                parent.right = TreeNode(r)
                depths[pos[r]] = d + 1
                inserted.add(r)
                #print("inserted", r)
                build(parent.right, parent_i+1, max_i, d+1)     # recur on right subarray A[i+1, n]
        #print("End recursion for parent", A[parent_i])

    build(root, min_i=0, max_i=n, d=0)
    #print("depths:",depths)
    return root, depths

def permutationTree(A, n):
    positions = dict()        # key: key, value: index
    for i in range(len(A)):
        positions[A[i]] = i
    tree, depths = buildTree(positions, A, n)
    depths = [str(d) for d in depths]
    print(" ".join(depths))


for _ in range(int(input())):
    n = int(input())
    A = [int(x) for x in input().split()]
    permutationTree(A, n)

