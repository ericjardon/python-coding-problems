import math
# Add any extra import statements you may need here
from collections import deque
from collections import defaultdict

class Node: 
  def __init__(self, data): 
    self.val = data 
    self.children = []

# Add any helper functions you may need here

def countFromSubtree(subtree, c, S):
  # S is a 1-based string
  # c is the character to count for from subtree
  
  q = deque()
  q.append(subtree)
  count = 0
  
  while q:
    curr = q.popleft()
    if c == S[curr.val]:
      count += 1
      
    for nextNode in curr.children:
      q.append(nextNode)
      
  return count

def count_of_nodesForMemory(root, queries, s):
  # Every node is uniquely labeled, we don't know if it follows a particular structure
  # Expected result is an integer array
  # Will the queries be distinct?  
  # Brute-force it: traverse once to have an array of subtree nodes for every 1...N
  N = len(s)
  subtrees = [0] + [None]*(N)
  S = ' ' + s  # to have 1-based indexing
  
  q = deque()
  q.append(root)
  while q:
    curr = q.popleft()
    subtrees[curr.val] = curr
    
    for nextNode in curr.children:
      q.append(nextNode)
    
  ans = []
  for u,c in queries:
      subtree = subtrees[u]
      ans.append(countFromSubtree(subtree, c, S))
  # Performance is O(Q*N + N)->O(Q*N) for time, O(2N) for memory
  return ans

def initCounterForChars(s):
  
  return {
    c:0 for c in s
  }

def count_of_nodes(root, queries, s):
  # Memory-intensive but performant:
  # For every node we have a mapping of c-># occurrences
  
  # We traverse the tree only once
  # And then for every query, just fetch the node key, character key and add the value.
  
  N = len(s)
  c_at_n = [None] + [initCounterForChars(s) for _ in range(N)]
  S = ' ' + s
  
  q = deque()
  q.append(root)
  
  def traverse(node, previous_nodes, frequency_at_node, S):
    # Node is never null
    i = node.val
    c = S[node.val]
    frequency_at_node[i][c] += 1
    
    # Update the counter of c in every ancestor node
    for n in previous_nodes:
      frequency_at_node[n.val][c] += 1      
    
    for c in node.children:
      traverse(c, previous_nodes + [node], frequency_at_node, S)
  
  # Traverse only once; populate our DS c_at_n
  traverse(root, [], c_at_n, S)
  ans = []
  for u, c in queries:
    ans.append(c_at_n[u][c]) 
    
  return ans  
    
      
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
      if i != 0:
          print(', ', end='')
      print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
      result = False
  for i in range(min(expected_size, output_size)):
      result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1
    
if __name__ == "__main__":

  # Testcase 1
  n_1 ,q_1 = 3, 1 
  s_1 = "aba"
  root_1 = Node(1) 
  root_1.children.append(Node(2)) 
  root_1.children.append(Node(3)) 
  queries_1 = [(1, 'a')]

  output_1 = count_of_nodes(root_1, queries_1, s_1)
  expected_1 = [2]
  check(expected_1, output_1)

  # Testcase 2
  n_2 ,q_2 = 7, 3 
  s_2 = "abaacab"
  root_2 = Node(1)
  root_2.children.append(Node(2))
  root_2.children.append(Node(3))
  root_2.children.append(Node(7))
  root_2.children[0].children.append(Node(4))
  root_2.children[0].children.append(Node(5))
  root_2.children[1].children.append(Node(6))
  queries_2 = [(1, 'a'),(2, 'b'),(3, 'a')]
  output_2 = count_of_nodes(root_2, queries_2, s_2)
  expected_2 = [4, 1, 2]
  check(expected_2, output_2)

  # Add your own test cases here
  