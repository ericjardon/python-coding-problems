## FIND K CLOSEST NUMBERS

def binsearch(arr, x):
    "Returns x or the closest number to x if not present"
    lo = 0
    hi = len(arr)-1
    while lo<=hi:
        mid= lo + (hi-lo)//2
        if arr[mid] == x:
            return mid, True
        elif arr[mid]>x:
            hi = mid-1
        else:
            lo = mid+1
    if hi == -1:
        return lo, False
    if lo == len(arr):
        return hi, False
    # else both indexes are within range
    if abs(x - arr[hi]) < abs(x - arr[lo]):
        return hi, False
    else:
        return lo, False


def find_k_closest(arr, k, target):
    """Returns the sorted list of k elements closest to target in the given arr"""
    # 1. Binary search for the target.
    if k==0:
        return []
    if k == len(arr):
        return arr
    if k > len(arr):
        raise Exception("Not enough elements in array")
    idx, found = binsearch(arr, target)
    closest = [arr[idx]]
    k -= 1
    i = idx+1  # larger elems
    j = idx-1   # smaller elems
    while(k>0 and i<len(arr) and j>-1):
        # add k remaining elements to closest. Scan left and right from idx
        if (arr[i] - target) < (target - arr[j]):
            closest.append(arr[i])
            i+=1
        else:
            closest = [arr[j]] + closest
            j-=1
        k-=1

    # we reached either end, keep appending until we have k elements
    while (k>0 and i<len(arr)):
        closest.append(arr[i])
        i+=1
        k-=1
    while (k>0 and j > -1):
        closest = [arr[j]] + closest
        j-=1
        k-=1

    return closest

#arr = [2,4,5,6,9,10,11,140,610]
# look for 7 should return index 3
#print(find_k_closest(arr, 10, 9))


## DELETE NODE WITH GIVEN KEY
class ListNode:
    def __init__(self, key, next=None):
        self.key = key
        self.next = next

def delete_node(head, key):
    """Given the head of a Linked List. Delete the node that contains the
        specified key."""
    if head is None: return None
    if head.key == key:
        return head.next
    dummy = ListNode(-1)
    dummy.next = head
    prev = head
    curr = head.next
    while (curr is not None):
        if curr.key == key:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next

    return dummy.next

def linked_list(arr):
    if len(arr)<1:
        return
    dummy = ListNode(-1)
    curr = ListNode(arr[0])
    dummy.next = curr
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_list(head):
    while head is not None:
        print(head.key, end=' ')
        head = head.next
    print()

def testDelNode():
    head = linked_list([4,5,1,9])
    k = 9
    print(f"Deleting {k}")
    print_list(delete_node(head, k))

## COPY LINKED LIST WITH ARBITRARY POINTER
class ArbitraryNode(ListNode):
    def __init__(self, key, next=None):
        super().__init__(key, next)
        self.pointer = None   # pointer to an arbitrary node in the list.

def CopyArbitraryList(head: ArbitraryNode):
    ## GOOD self-made solution: single-pass
    if head is None: return
    nodes = dict()  # maps a node to its arbitrary node pointer
    dummy = ArbitraryNode(-1)
    temp = ArbitraryNode(head.key)       # to iterate over our copy
    dummy.next = temp
    original = head.next            # to iterate over original
    # We are scanning the original list 1 position ahead from temp pointer (to avoid temp=None).
    # Hence, copy into temp.next
    while original is not None:
        # check if we already created the copy of original. if not, instantiate new copy
        if original.key not in nodes:
            temp.next = ArbitraryNode(original.key)
            nodes[original.key] = temp.next     # save the reference in our dict for future use
        else:
            temp.next = nodes[original.key]
        # check if we already created the copy of original's pointer.  if not, instantiate new copy
        if original.pointer:
            if original.pointer.key not in nodes:
                temp.next.pointer = ArbitraryNode(original.pointer.key)
                nodes[original.pointer.key] = temp.next.pointer
            else:
                temp.next.pointer = nodes[original.pointer.key]
        else:
            temp.next.pointer = None

        original = original.next
        temp = temp.next

    return dummy.next       # return head of deep copy
## UNTESTED ^^^^


## PROBLEM: Given an array of intervals,
# merge every overlapping interval and return the new list of intervals
from collections import deque
def mergeIntervals(intvals):
    # when do two intervals overlap?
    # Comparing start times we can decide which goes first.
    # Then, if first's end time is larger than second's start time, they overlap.
    def overlap(intval1, intval2):      # intval1 start time is less or equal than that of intval2
        #if intval2[0] < intval1[0]:
         #   intval1, intval2 = intval2, intval1
        if intval2[0] < intval1[1]:
            return True
        return False
    intvals.sort(key=lambda x: x[0])        # can skip if already sorted
    i = 0
    while i < len(intvals)-1:
        j = i+1
        if overlap(intvals[i], intvals[j]):
            new_intval = [intvals[i][0], max(intvals[i][1], intvals[j][1])]
            intvals[i] = new_intval     # replace first with new interval
            del intvals[j]              # delete the second
            continue                    # check mergeability with next in 'queue'
        i = j                           # if no overlap, check next pair of intervals
    return intvals
    ## COMPLEXITY IS NlogN + N when unsorted. If sorted, simple linear scan: O(N)

def testIntvals():
    it_ = [[100,220], [8,20], [1,2], [1,11]]
    it = [[1,2],[2,3],[3,4],[5,6], [3,6]]
    print(it)
    print(mergeIntervals(it))

testIntvals()