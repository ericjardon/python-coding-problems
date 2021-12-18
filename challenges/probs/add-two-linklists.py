class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
        -> Optional[ListNode]:
        # Use stacks to reverse
        s1 = []
        s2 = []

        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        
        digit = 0
        temp = ListNode(0)
        # New lists are created back to front
        while s1 or s2:
            if s1:
                digit += s1.pop()
            if s2:
                digit += s2.pop()

            # Get rid of carries
            carry, num = divmod(digit, 10)
            # Building back to front of list, preppending
            temp.val = num
            preppend =  ListNode(carry)
            preppend.next = temp
            digit = carry  # accumulate for next

        if preppend.val > 0:
            return preppend
        
        return preppend.next

    def _addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) \
        -> Optional[ListNode]:
        '''Without reversing input lists'''

        # 0. Obtain lengths of both
        len1 = 0
        len2 = 0
        temp1 = l1
        temp2 = l2
        while temp1 is not None or temp2 is not None:
            if temp1 is not None:
                len1 += 1
                temp1 = temp1.next
                
            if temp2 is not None:
                len2 += 1
                temp2 = temp2.next

        # 1. Traverse both lists, pairwise.
        temp1 = l1
        temp2 = l2
        dummy = ListNode(0)
        temp3 = dummy
        for pos in range(max(len1, len2), 0, -1):
            digit = 0
            if pos <= len1:
                digit +=  temp1.val
                temp1 = temp1.next
            if pos <= len2:
                digit += temp2.val
                temp2 = temp2.next
            
            if digit < 10:
                temp3.next = ListNode(digit)
                temp3 = temp3.next
            else:
                temp3.val += 1
                temp3.next = ListNode(digit%10)
                temp3 = temp3.next
        
        # Check for overloaded digits
        temp4 = dummy.next
        prev = dummy
        while temp4:
            if temp4.val == 10:
                prev.val

        # Check overload in dummy
        if dummy.val > 0:
            print("Return dummy")
            return dummy
        elif dummy.next.val == 10:
            head = ListNode(1)
            head.next = dummy.next
            head.next.val = 0
            return head
        
        return dummy.next
        ## FAILS ON 899, 699, ETC + 1 (receding carries) 
        


def LinkedList(list):
    if not list: return None

    dummy = ListNode()
    temp = dummy
    for val in list:
        temp.next = ListNode(val)
        temp = temp.next

    return dummy.next
    
def printLL(list):
    temp = list
    print("[", end='')
    while temp:
        print(temp.val, end=' ')
        temp = temp.next

    print("]")


l1 = LinkedList([8,9,9,9])
l2 = LinkedList([2])

printLL(l1)
printLL(l2)
l3 = Solution().addTwoNumbers(l1, l2)

#printLinkedList(l1)
#printLinkedList(l2)
printLL(l3)