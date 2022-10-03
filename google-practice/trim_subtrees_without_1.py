# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def hasOne(subtree):
    # check val, and check both subtrees.
    if subtree is None:
        return False

    left = hasOne(subtree.left) 
    if not left:
        subtree.left = None

    right = hasOne(subtree.right)
    if not right:
        subtree.right = None

    return subtree.val == 1 or left or right
    
from typing import Optional

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Do dfs that returns True if subtree has 1.
        
        if hasOne(root):
            return root

        return None
        
        