from typing import List

def maxArea(height: List[int]) -> int:
    """Given a list of heights of bars in a
    bar chart, find two bars such that the area
    enclosed between the two is largest possible. """
    maxA = 0
    # Brute force with two pointers, check area with every pair.
    for i in range(len(height) - 1):        # O(n^2)
        for j in range(i+1, len(height)):
            container = min(height[i],height[j])*(j-i)
            maxA = max(maxA, container)
    return maxA

# goes too slow for inputs -> 3*10^4
def fastmaxArea(height: List[int]) -> int:
    """Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width
     but we are looking forward to a longer length container."""
    i = 0
    j = len(height) - 1
    maxA=0
    # Single pass, O(n)
    while i<j:
        # If h[i] < h[j], probe i onwards
        # else probe j backwards
        if height[i] < height[j]:
            A = (j - i) * height[i]
            i += 1
        else:
            A = (j - i) * height[j]
            j -=1
        maxA = max(A, maxA)

    return maxA


def TwoSum(nums: List[int], target: int) -> List[int]:
    """Given an array of integers and a target, return the indices of two numbers
        that add up to target. Assume there is always one single solution
        DO NOT USE SORTING"""
    seen = {}      # number: index of previously seen values

    for idx, num in enumerate(nums):
        complement = num - target       # number needed to make the sum
        if complement in seen:          # careful not to use the same num twice
            return [seen[complement], idx]
        seen[num] = idx

    return [0,0]

class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def printListNodes(head: ListNode):
    while (head is not None):
        if head.next == None:
            print(head.val)
        else:
            print(head.val,"->")
        head = head.next

def AddTwoNums(l1: ListNode, l2: ListNode) -> ListNode:
    i = 0
    a = 0
    while (l1 is not None):
        a += l1.val*(10**i)
        i += 1
        l1 = l1.next

    i = 0
    while (l2 is not None):
        a +=  l2.val*(10**i)
        i += 1
        l2 = l2.next
    print(a)

    num = str(a)
    n = None
    for digit in num:
        n = ListNode(int(digit), n)
    return n

def fasterAddTwoNums(l1: ListNode, l2: ListNode) -> ListNode:
    dummy = ListNode()  # dummy node points to head
    carry = 0   # 0 or 1 to add to next
    prev = dummy
    while l1 or l2:     # sums backwards??
        temp = ListNode(0)
        a = l1.val if l1 else 0
        b = l2.val if l2 else 0
        print("Adding:", a, b)
        carry, temp.val = divmod(
            a + b + carry, 10)      # to clamp value up to 9 and get carry 1 if res==10
        print("Carry: ",carry," Val:",temp.val)
        prev.next = temp
        prev = temp
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    if carry:
        print("Last carry")
        prev.next = ListNode(carry)
    return dummy.next

if __name__=="__main__":
    l14 = ListNode(2)
    l13 = ListNode(4, l14)
    l12 = ListNode(3,l13)
    l11 = ListNode(5, l12)  # 2435
    l23 = ListNode(5)
    l22 = ListNode(6,l23)
    l21 = ListNode(4,l22)   # 564
    # res: 2999
    # Lists are reversed: the number is read from least signif to most significant,
    # allowing that the digit of l1 at pos i is always to the same power as the other in l2
    # we just continue adding the excess digits of the larger summand with power of 10 corresponding to i
    # 111,8  for 8,111
    # 18    for    81
    printListNodes(fasterAddTwoNums(l11, l21))