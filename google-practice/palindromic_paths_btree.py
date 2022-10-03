'''
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be 
pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.
'''
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # We can get a palindromic permutation if and only if:
        # the length is even and there is an even number of all the digits present in path
        # the length is uneven and there is exactly one digit with an uneven number of occurrences in the path
        
        
        def checkPseudoPalindrome(path):
            vals = [node.val for node in path]
            digit_odd = [False for _ in range(10)]
            for x in vals:
                digit_odd[x] = not digit_odd[x]
            
            if len(vals)%2 == 0 and sum(digit_odd) == 0:
                return 1
            if len(vals)%2 == 1 and sum(digit_odd) == 1:
                return 1
            return 0
                
        def dfs(node, path):
            if node is None:
                return 0
            if not (node.left or node.right):
                return checkPseudoPalindrome(path + [node])
            
            if node.left:
                l = dfs(node.left, path + [node])
            else:
                l = 0
            if node.right:
                r = dfs(node.right, path + [node])
            else:
                r = 0
            
            return l + r
        
        return dfs(root, [])
        # TLE on LeetCode
        