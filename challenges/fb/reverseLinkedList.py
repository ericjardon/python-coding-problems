import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here

def isEven(x):
  return x%2==0

def rev(prev, first, last):
  # Use a stack
  if first == last: return
  
  stack = []
  end = last.next
  curr = first
  
  while curr != last:
    stack.append(curr)
    curr = curr.next
  
  prev.next = last
  curr = last
  while stack:
    curr.next = stack.pop()
    curr = curr.next
  
  curr.next = end
  return
  

def reverse(head):
  # A subproblem is to find subparts
  
  dummy = Node(-1)
  dummy.next = head
  curr = head
  prev = dummy
  
  while curr:
    if isEven(curr.data):
      first = curr
      lookAhead = curr
      
      # LookAhead stops at last even node
      while lookAhead.next and isEven(lookAhead.next.data):
        lookAhead = lookAhead.next
      
      last = lookAhead  # last even node
      
      rev(prev, first, last)
      # first becomes the rightmost node in subarray
      prev = first
      curr = first.next
    
    else:
      prev = curr
      curr = curr.next
        
  return dummy.next







# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)

  # Add your own test cases here
  