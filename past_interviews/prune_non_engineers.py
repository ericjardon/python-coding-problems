'''Prune non-engineers from an org chart.

Test 1
E
  E
      N
    N  E

Test 2
E
  E
    E

Test 3
    E
N       N
        E
      E   N


Complexity?
N-ary tree:
 V <- total nodes
 b <- largest number of children.
 d <- max depth
'''

# O(V*b^2), we know number of nodes
from tkinter.tix import Tree
from typing import List, Optional, Union


class TreeNode:
    def __init__(self, val: str, children: Optional[List] = []):
        self.children = children
        self.type = val
  
    def __repr__(self, level=0):
        ret = "\t"*level+repr(self.type)+"\n"
        for child in self.children:
            ret += child.__repr__(level+1)
        return ret


def prune(node: TreeNode) -> Union[TreeNode, List[TreeNode]]:
    if node is None:   # sanity check
        return None

    if node.children:
        # for every child
        new_children = []
        # O(b^2)
        for child in node.children:  # O(b)
            result = prune(child)  # can return a forest (array), single node, or None

            if isinstance(result, list): # Pruned direct child and got a Forest
                # append to list of children O(b)
                new_children.extend(
                  [descendant for descendant in result if descendant])

            elif result is not None:
                # is a 'E' TreeNode
                new_children.append(result)
        # update this node's children
        node.children = new_children

    if node.type == 'N': # pop root and return its pruned children
        return node.children
    else:
        return node


def Solution(OrgTree: TreeNode) -> TreeNode:
    # Assume root is always engineer
    return prune(OrgTree)


# Example Trees
'''
Test 1
E
  E
      N
    N  E
'''
t1 = TreeNode('E', [TreeNode('E', [TreeNode('N', [TreeNode('N'), TreeNode('E')])])])
print(t1)
print("--- after pruning")
prune(t1)
print(t1)

print("======================\n======================")
'''
Test 2
E
  E
    E
'''
t2 = TreeNode('E', [TreeNode('E', [TreeNode('E')])])
print(t2)
print("--- after pruning")
prune(t2)
print(t2)
print("======================\n======================")

'''
Test 3
    E
N       N
        E
      E   N
'''
t3 = TreeNode('E', [TreeNode('N'), TreeNode('N', [TreeNode('E', [TreeNode('E'), TreeNode('N')])])])
print(t3)
print("--- after pruning")
prune(t3)
print(t3)