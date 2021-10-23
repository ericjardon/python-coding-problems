from collections import deque


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class PathSum:
    """Given the root of a Binary tree and a number, return a list of the possible
    root-to-leaf paths (as lists) of which the sum is equal to this number"""

    def pathSum(self, root: TreeNode, s: int):
        # Results is a global variable for the list of paths
        # We define an inner helper function findPath
        # so this function 'knows' what results to append to.

        def findPath(node, path):
            if sum(path) == sum \
                    and node.left == None and node.right==None:
                results.append(path)
                # an improvement is to use a counter along the way so we dont use sum() function
            if node.left:
                findPath(node.left, path + [node.left.val])
            if node.right:
                findPath(node.right, path + [node.right.val])
                # Use of backtracking: we only explore if child node is not null

        results = []
        if not root:        # if the root is None
            return
        findPath(root, [root.val])

        return results

# LEETCODE PROBLEMS -- MEDIUM
# Notation (name: type) -> type is more typesafe and explicit.
# It tells the type of parameters needed and the return type.

class BinarySum:
    """Given a BST and a target k, determine if there are any
    two elements in the tree whose sum is equal to the target."""

    # FIRST APPROACH -- ONLY WORKS WITH POSITIVE NUMBERS :(
    def twoSum(self, root: TreeNode, k: int) -> bool:
        # we can split k in its possible two-sums, and do a search for each.
        # for each number i:(floor(k/2)), i=0, search for i and (k-i)
        # if both are found return true.
        def bSearch(node: TreeNode, val : int):
            if not node:
                return False
            if (node.val == val):
                return True
            if val < node.val:
                return bSearch(node.left, val)
            if val > root.val:
                return bSearch(node.right, val)
        for i in range(k//2 + 1):
            if (i != k-i):      # no duplicates allowed in BST
                if bSearch(root, i) and bSearch(root, k-i):
                    return True
        return False

    def twoSumNeg(self, root: TreeNode, k: int) -> bool:
        # Since negatives are allowed the search space is not just 0 to k/2
        # we have to look at every node and bsearch for its complement.
        def bSearch(node: TreeNode, val: int):
            if not node:
                return False
            if (node.val == val):
                return True
            if val < node.val:
                return bSearch(node.left, val)
            else:
                return bSearch(node.right, val)

        def traverse(node: TreeNode):
            if node == None:
                # node is null so nothing to look for here
                return False

            complement = k - node.val
            if node.val != complement and bSearch(root, complement):
                    # if the complement to this node's value exists in the tree
                    print("Val:", str(node.val), "Searching for", str(complement))
                    return True

            if traverse(node.left):
                return True
            if traverse(node.right):
                return True

            return False
        return traverse(root)

    def fasterTwoSum(self, root: TreeNode, k: int):
        # The idea is to traverse the BST and store the values in a sorted array.
        # inorder-traversal assures that the array is sorted.
        # Then we can use a two-pointer approach to find the first pair
        # of numbers whose sum equals k.
        def iot(root: TreeNode, array: list):
            if (root != None):
                array = iot(root.left, array)
                array.append(root.val)
                array = iot(root.right, array)
            return array

        array = iot(root, [])      # Traverse the tree inorder
        lo = 0
        hi = len(array) -1
        while (lo < hi):
            val = array[lo] + array[hi]   # probing a combination of lower and higher
            if val<k:
                lo += 1     # increment the lesser summand
            elif val>k:
                hi -= 1     # reduce the larger summand
            else:
                # the value is equal to k
                return True
        # If the cycle ends we didn't find any pair whose sum is k
        return False

def longestzigZag(root: TreeNode) -> int:
    def zigzag(node: TreeNode, goRight: bool, depth: int):
        # HELPER FUNCTION, COUNT RECURSIVELY FROM ANY NODE
        if node==None:
            return depth
        else:
            if goRight:
                right = zigzag(node.right, False, depth + 1)    # continue count
                left = zigzag(node.left, True, 0)   # restart zigzag count
            else:
                right = zigzag(node.right, False, 0)
                left = zigzag(node.left, True, depth + 1)

            return max(left, right)

    # STARTING FROM ROOT
    if root.left == None and root.right == None:
        return 0
    left = 0
    right = 0
    if root.left:
        left = zigzag(root.left, True, 0)
    if root.right:
        right = zigzag(root.right, False, 0)

    return max(left, right)

from typing import List

def rightSideView(self, root: TreeNode) -> List[int]:
    """Given a binary tree return the  values of the visible
        nodes to the right, traversed from top to bottom."""
    def rightmost2(node: TreeNode, traversal: List[int], levels: int = 0):
        # returns the list of rightmost visible nodes to the right starting from node
        # levels is the number of levels left to go further down. If negative, we are visible to the right
        if node == None:
            return traversal       # no more nodes, traversal stops
        levels -= 1     # descendeded one level.
        if levels <0:
            traversal.append(node.val)  # only start appending when we are lower than the levels of rightmost branch
        if node.right:
            R = rightmost2(node.right, [], levels)  # rightmost traversal of subtree, only appends visible nodes (levels) levels down
            L = rightmost2(node.left, [], len(R) + max(levels,0))
            # for visible nodes in left branch, we have to go deeper than the rightmost branch
            # + number of visible nodes in the middle right branch
            traversal += R + L      # add both the visible right and visible left nodes
        elif node.left:
            # if no right branch we just explore the left, going levels levels deep
            traversal += rightmost2(node.left, [], levels)
        return traversal

    return rightmost2(root, [])
# NOTE: you can also use a rightmost BFS, appending only leafs?

def averageOfLevels(self, root: TreeNode) -> List[float]:
    """Return a list of the average value per level"""
    # Every level has 2**n nodes.
    # From a given node we can get the sum of two children.
    # We can use an array of size levels.
    # At the ith place we accumulate the corresponding values for the ith level.
    # In the end we divide each entry of array by 2**i
    def getDepth(root: TreeNode):
        if root==None:
            return 0
        return max(getDepth(root.left) + 1, getDepth(root.right) + 1)

    def getSums(root: TreeNode, level=0):
        if root:
            counts[level] += 1
            sums[level] += root.val
            getSums(root.left, level + 1)
            getSums(root.right, level + 1)

    levels = getDepth(root)
    sums = [0]* levels
    avgs = [0]* levels
    counts = [0]* levels
    getSums(root)
    for i in range(levels):
        avgs[i] = sums[i]/counts[i]

    return avgs

def levelOrderBottom(root: TreeNode) -> List[List[int]]:
    """Return the traversal in bottom-up order: a list of the nodes left-right from bottom level to top level"""
    # Make a list per tree level.
    # Traverse the tree left, right,
    # append node values to the current level's list
    # Insert the level list in the (totLevels-currentLevel) index.
    def getDepth(root: TreeNode):
        # More precisely, get levels. Depth is num of levels-1
        if root == None:
            return 0
        return max(getDepth(root.left) + 1, getDepth(root.right) + 1)

    def traverse(node: TreeNode, currLvl):
        if node == None:
            return
        else:
            index = -1 - currLvl  # negative indices so we insert from back to front
            levels[index].append(node.val)
            print(levels)
            if node.left:
                traverse(node.left, currLvl + 1)
            if node.right:
                traverse(node.right, currLvl + 1)

    depth = getDepth(root)  # number of levels
    levels = [[] for i in range(depth)]      # a list per each level
    traverse(root, 0)
    return levels


def findBottomLeftValue(root: TreeNode)->int:
    """Return the value of the leftmost node at the bottom level"""
    # Find the depth of tree so we know which is last level
    def getDepth(root: TreeNode):
        if root==None:
            return 0
        return max(getDepth(root.left) + 1, getDepth(root.right) + 1)

    def pot(node: TreeNode, level: int):
        if node:
            if level < levels:
                left = pot(node.left, level+1)
                if left != None:
                    return left
                else:
                    return pot(node.right, level+1)
            else:
                if node.right == None and node.left == None:
                    return node.val
        else:
            return None

    levels = getDepth(root) - 1
    leftmostVal = pot(root, levels)
    return leftmostVal

## A better solution may be level-order traversal aka BFS
def findBottomLeftFaster(root: TreeNode)->int:
    # traverse the tree one time
    if root == None:
        return -1

    max_depth = -1  # to keep track of deepest level
    val = -1      # default leftmost value
    queue = deque()     # to store pairs (node, height)
    queue.append((root, 0))
    while len(queue):
        node, lvl = queue.popleft()  # dequeue
        if lvl > max_depth:
            max_depth = lvl     # update deepest level visited
            val = node.val      # the first value on a new level is leftmost
        # val is only updated once per level.
        # since we atre traversing left branch first it should be leftmost
        if node.left:
            queue.append((node.left, lvl+1))
        if node.right:
            queue.append((node.right, lvl+1))

    return val

def main():
    pass

main()