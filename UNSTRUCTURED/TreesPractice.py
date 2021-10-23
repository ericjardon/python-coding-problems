#================BINARY TREES ====================#
# TRAVERSALS: Preorder(NLR), Inorder(LNR), Postorder(LRN)
from collections import deque

class Node:
    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right
    def printTree(self, lvl=0):
        print(lvl*'  ', self.key)
        if self.right:
            self.right.printTree(lvl+1)
        if self.left:
            self.left.printTree(lvl+1)
    def preorder(self):  # NLR Traversal
        print(self.key)
        if self.left:
            self.left.preoder()
        if self.right:
            self.right.preorder()
    def isLeaf(self):
        return self.left is None and self.right is None


class BoundaryTraversal:
    """Given a binary tree perform the boundary traversal, printing
        the outermost nodes in a counterclockwise fashion, starting with root."""

    # We can print the left boundary, the leaf nodes, then the right boundary.
    # To avoid duplicate printing, print root first, then left, then leaves, then right.
    # leftmost and rightmost traversals should exclude their respective leaf nodes.

    def leftDFS(self, node):
        if node is None:    # No left node
            return
        if node.left is None and node.right is None:
            # dont print leftmost leaf node
            return
        print(node.key, end=' ')  # Top-down: first recursion prints first
        if node.left:               # Go as far left as possible.
            self.leftDFS(node.left)
        else:                       # If no left, go right
            self.leftDFS(node.right)

    def rightDFS(self, node):
        if node is None:    # no right node
            return
        if node.left is None and node.right is None:
            # dont print rightmost leaf node
            return
        if node.right:                  # Go as far right as possible.
            self.rightDFS(node.right)
        else:                           # If no right, go left
            self.rightDFS(node.left)
        print(node.key, end=' ')      # Bottom-up: first recursion prints last

    def inorderLeaves(self, root):
        if root is not None:
            self.inorderLeaves(root.left)
            # only print leaf nodes
            if root.left is None and root.right is None:
                print(root.key, end=' ')
            self.inorderLeaves(root.right)

    def boundaryTraversal(self, root):
        # 0. Edge case
        if root == None: return
        # 1. Print root
        print(root.key, end=' ')
        # 2. Top-down leftmost traversal from root.left
        self.leftDFS(root.left)
        # 3. Inorder leaf nodes traversal
        self.inorderLeaves(root)
        # 4. Bottom-up traversal from root.right
        self.rightDFS(root.right)

    def main(self):
        root = Node(1)
        root.left = Node(2)
        root.right = Node(3)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.left.left.left = Node(8)
        root.left.left.right = Node(9)
        root.left.right.right = Node(10)
        root.right.right.left = Node(11)
        root.left.left.right.left = Node(12)
        root.left.left.right.right = Node(13)
        root.right.right.left.left = Node(14)
        self.boundaryTraversal(root)
        # TIME COMPLEXITY O(n) for n nodes, SPACE COMPEXITY O(h) of call stack for h height of tree


## PROBLEM: Adjust a Binary Tree to have the Chlidren-Sum property.
class FixChildrenSum:

    def fixChildrenSum(self, root):        # inorder solution takes O(n^2) for n nodes
        def childrenSum(node):
            left = node.left.key if node.left else 0
            right = node.right.key if node.right else 0
            return left+right

        # 0. Base cases
        if root is None or root.left is None and root.right is None:
            return  # tree is empty or is a singleton
        # 1. Adjust left and right branches first
        self.fixChildrenSum(root.left)
        self.fixChildrenSum(root.right)
        # 2. Compute difference of node's value with children's sum
        diff = root.key - childrenSum(root)
        if diff < 0:            # root is less than children sum increment root's value to equal the sum
            root.key -= diff
        if diff > 0:            # root is greater, we need to increment children values
            subtree = root.left if root.left else root.right    # either update left or right, does not matter
            subtree.key += diff
            self.fixChildrenSum(subtree)     # readjust from subtree down

    def faster_fcs(self, root):     # Solution is O(n) for n nodes.
        def childrenSum(node):
            left = node.left.key if node.left else 0
            right = node.right.key if node.right else 0
            return left+right

        if root is None or root.isLeaf():
            return

        diff = root.key - childrenSum(root)
        if diff > 0:
            subtree = root.left if root.left else root.right
            if subtree:
                subtree.key += diff
        self.faster_fcs(root.left)
        self.faster_fcs(root.right)
        # Update current node
        root.key = childrenSum(root)
        # A possible downside vs the slower approach is that the resulting values of this tree may be much larger
        # while the other's increment is minimal

    def main(self):
        root = Node(25)
        root.left = Node(8)
        root.right = Node(10)
        root.left.left = Node(4)
        root.left.right = Node(5)
        root.right.left = Node(6)
        root.right.right = Node(7)
        root.printTree()
        #self.fixChildrenSum(root)
        self.faster_fcs(root)
        root.printTree()



##PROBLEM Find Shortest Unique Prefix in an Array of Words
    # SOLUTION: Construct a Trie of the given Words. As we insert words into the trie,
    # keep track of how many times you visit a Trie Node. (use an extra field).
    # Then for every word in W, search for the word in the tree and stop when Node frequency is 1
    # Or faster yet, only traverse the Trie in dfs fashion. Every time we reach a node with freq=1,
    # add the constructed word to the answer, and return to continue with next path in Trie.
from collections import defaultdict
class ShortesUniquePrefix:
    """Given an array of words W where no word is a proper prefix of another,
        find the corresponding array of shortest unique prefixes that identify each word"""
    class TrieNode:
        def __init__(self):
            # we don't need a name for node, it is given by the relationship to its parent (dict pointer key)
            # however, note that name for a node could be the word_so_far value we are using in the traversal method
            self.children = dict()     # dictionary of child nodes with max 26 keys as letters
            self.freq = 0              # frequency is 0 upon creation

    def trieInsert(self, root:TrieNode, word:str):
        curr = root
        for char in word:
            curr.children.setdefault(char, self.TrieNode()) # create new child node if no path in trie exists
            # note: setdefault tells dict what to return if specified key is not found
            curr.children[char].freq += 1
            curr = curr.children[char]

    def shortestUniquePrefix(self, W):
        prefixes = list()

        def printPrefixes(node, word_so_far):
            if node is None: return
            if node.freq == 1:
                prefixes.append(word_so_far)
                print(word_so_far)
            else:
                for char, child in node.children.items():
                    printPrefixes(child, word_so_far + char)

        root = self.TrieNode()
        for w in W:
            self.trieInsert(root, w)
        # Once all words have been inserted to Trie, traverse and print out the prefixes
        printPrefixes(root, '')
        return prefixes

    def main(self):
        W = ['AND', 'BOOL', 'BONFIRE', 'CATCH', 'CASE', 'CHAR']
        self.shortestUniquePrefix(W)


## PROBLEM: Check whether the leaf traversal of two trees is the same or not.
class EqualLeafTraversal:
    def equalLeaves1(self, root1, root2):
        # Traverse both trees in same order, storing the leaves encountered in an array.
        # check if arrays are the same.    -- Approach 1: time O(m+n), space O(m+n) for two trees with m and n nodes
        def traverseLeaves(root):
            # Returns an array of the leaves of a rooted tree
            leaves = list()
            # Traverse LNR as we want to read the leaves left-to-right
            def inorder(root):
                if root:
                    inorder(root.left)
                    if root.isLeaf():
                        leaves.append(root.key)
                    inorder(root.right)
            inorder(root)
            return leaves
        leaves1 = traverseLeaves(root1)
        print(leaves1)
        leaves2 = traverseLeaves(root2)
        print(leaves2)
        i,j = 0,0
        while i<len(leaves1) and j<len(leaves2):
            if leaves1[i] != leaves2[j]:    # an element is not equal
                return False
            i+=1
            j+=1
        if i!=j: return False       # different length arrays
        return True                 # same length and all elements are equal

    def main(self):
        x = Node(1)
        x.left = Node(2)
        x.right= Node(3)
        x.left.left = Node(4)
        x.left.right = Node(5)
        x.right.left = Node(6)
        x.printTree()
        y = Node(1)
        y.left = Node(2)
        y.right=Node(3)
        y.left.right=Node(4)
        y.right.left = Node(5)
        y.right.right = Node(6)
        y.printTree()
        if self.equalLeaves1(x, y):
            print("Equal leaves")
        else:
            print("Non-equal leaves")


## PROBLEM: construct a Binary Expression Tree
# Build a tree that given a postfix notation it prints the infix notation.
# A BET is a BT whose leaves are operands: constants or variables.
# All other nodes contain binary operators.
# postfix notation: a b + c d e + x x
# infix notation:   (a+b) x (cx (d+e))
# An infix notation is produced by traversing inorder LNR a tree.
# Careful to add parentheses in opening and closing brackets of expressions.
# Note: Every subtree is its own expression.
# Note: You can find the operands to an operator by reading backwards the expression
# from that operator and picking the first two operands, pairing them as a single new operand.
# this effectively constructs the expression reading back-to-front, preppending to the expression each time.
# More interestingly, a postorder traversal of BET returns the postfix. The inorder traversal returns the infix.

class BinaryExpressionTree:
    """Constructs a BET from a given postfix notation. reads front to back appending to expression.
        METHOD: Read the postfix one symbol at a time. If symbol is operand, create a Node
        and push it to the stack. It symbol is operator, pop two operands from stack and assign as children
        to a new Node with the operator as key, & push this new subtree (subexpression) to the stack.
        At the end, every pointer has been popped except the root node pointer. (which is the largest expression)"""
    def isOperator(self,char):
        return char == '+' or char == '-' or char == 'x'

    def constructBET(self, postfix):
        stack =deque()
        for char in postfix:
            if self.isOperator(char):
                # point to root of last sub-expressions
                x = stack.pop()
                y = stack.pop()
                # popped expressions will be children of operator
                node = Node(char, y, x)     # y is the leftmost operand
                stack.append(node)
            else:                           # if char is an operand, e.g. a,b,c,...
                stack.append(Node(char))    # push to stack as a leaf
        # Postfix expression must be correct for this to work
        return stack[-1]    # return top of stack which contains root operator of entire expression

    def postfix(self, root):    # returns the postfix expression of a BET
        # traverse postorder from the root; LRN
        def postorder(root):
            if root:
                postorder(root.left)
                postorder(root.right)
                print(root.key, end=' ')
        postorder(root)

    def infix(self, root):
        # traverse inorder from the root; LNR
        def inorder(root):
            if root:
                if self.isOperator(root.key):
                    print('(', end='')
                inorder(root.left)
                print(root.key, end='')
                inorder(root.right)
                if self.isOperator(root.key):
                    print(')', end='')
        inorder(root)

    def main(self):
        postfix = "ab+cde+xx"
        bet = self.constructBET(postfix)
        print("Postfix:\t", end='')
        self.postfix(bet)
        print("\nInfix:\t", end='')
        self.infix(bet)

## PROBLEM: Mirror an N-ary tree
# An N.ary tree is a tree where each node has no more than N children
# Hence, a good representation is a Node using an array of pointers of its children.

# Naive approach: Recursively traverse the tree, at each node reverse its array of pointers.
# It does not matter top down or bottom up
class NaryNode:
    def __init__(self, key):
        self.key = key
        self.children = list()

class MirrorTree:
    def printTree(self, node):  # preorder printing
        if node is None:
            return
        print(node.key, end=' ')
        for child in node.children:
            self.printTree(child)

    def mirrorTree(self, root):
        def mirror(node):
            if node:
                copy = Node(node.key)   # take the value of original node
                copy.children = list(node.children[::-1])       # make its children a reversed list of original's children
                for i in range(len(copy.children)):     # for every slot in the array of children reassign the pointer to a mirror copy
                    copy.children[i] = mirror(copy.children[i])
                return copy
            return None
        return mirror(root)     # creates a mirror copy

    def reverseOrder(self, array):
        def swap(i, j):
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
        n = len(array)
        for i in range(n//2):   # rounds down
            swap(i, n-i-1)      # a middle position swaps with itself

    def main(self):
        root = NaryNode(1)
        (root.children).append(NaryNode(2))
        (root.children).append(NaryNode(3))
        (root.children).append(NaryNode(4))
        (root.children).append(NaryNode(5))
        (root.children).append(NaryNode(6))

        (root.children[0].children).append(NaryNode(7))
        (root.children[0].children).append(NaryNode(8))
        (root.children[0].children).append(NaryNode(9))

        (root.children[2].children).append(NaryNode(10))
        (root.children[2].children).append(NaryNode(11))
        (root.children[2].children).append(NaryNode(12))

        (root.children[4].children).append(NaryNode(13))
        (root.children[4].children).append(NaryNode(14))

        (root.children[0].children[1].children).append(NaryNode(15))
        (root.children[0].children[1].children).append(NaryNode(16))

        (root.children[4].children[0].children).append(NaryNode(17))
        (root.children[4].children[0].children).append(NaryNode(18))
        (root.children[4].children[0].children).append(NaryNode(19))
        (root.children[4].children[0].children).append(NaryNode(20))
        self.printTree(root)
        mirrored = self.mirrorTree(root)
        print()
        print("Mirror:\t", end='')
        self.printTree(mirrored)
        print()
        print("Original:\t", end='')
        self.printTree(root)        # SOLUTION IS CORRECT


class TreePathSum:
    """Given a binary tree return True if there exists a complete root-to-leaf path
     such that the sum of node values equals a target."""
    def completePathSum(self, root, target):
        def findSum(node, sum):
            """recursive DFS returns True if there is a root-leaf path
             that adds up to sum"""
            if node is None or sum + node.key > target:
                return False
            sum += node.key
            if node.right is None and node.left is None:
                return sum==target
            return findSum(node.left, sum) or findSum(node.right, sum)
        # Call to utility function
        return findSum(root, 0)

    def pathSum(self, root, target):
        """Returns any partial paths that adds up to target"""
        def sumPath(node, remaining):
            if remaining == 0:
                return True
            if node is None or remaining<0:
                return False

            return sumPath(node.right, remaining - node.key) or \
                   sumPath(node.left, remaining - node.key)
        return sumPath(root, target)

    def main(self):
        pass




if __name__ == '__main__':
    #BoundaryTraversal().main()
    #FixChildrenSum().main()
    #ShortesUniquePrefix().main()
    #EqualLeafTraversal().main()
    #BinaryExpressionTree().main()
    #MirrorTree().main()
    pass