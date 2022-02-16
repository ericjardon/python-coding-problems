'''# DEFINITIONS
Complete Binary Tree: a binary tree in which every level is filled except possibly the last.
                      as a consequence, all nodes are as far left as possible
Binary Heap: a CBT where items are stored according to value. A node's children are smaller (min-heap)
             or larger (max heap) than the node.

Max heap: root is always the largest element.
Min heap: root is always the smallest element

BT representation: can use an actual tree structure or even an Array.
Array representation is more space-efficient.
  A parent at index i has left child in 2*i+1 and right in 2*i+2

STEPS. --ASCENDING ORDER
1. Build max-heap with the data to sort.
2. Remove the root and replace with the last element in the heap.
2.1 then heapify again.
Repeat steps 2 while size of the heap is > 1'''

def heapify(treeArray, index, heapSize):

    minValIndex = index  # parent node
    left = 2*index+1
    right = 2*index+2

    # Find min value among the parent and its children, reassign index
    if left < heapSize and treeArray[left] < treeArray[minValIndex]:
        minValIndex = left
    
    if right < heapSize and treeArray[right] < treeArray[minValIndex]:
        minValIndex = right
    
    # If minimum value was not parent node.
    if minValIndex != index:
        # Swap the values
        treeArray[minValIndex] , treeArray[index] = treeArray[index], treeArray[minValIndex]
        # Heapify again from the winning child's index
        heapify(treeArray, minValIndex, heapSize)
    

def heapSort(unsorted):
    '''Returns the sorted array in decreasing order'''
    n = len(unsorted)
    # Initialize a heap.
    for i in range(n//2 -1, -1, -1):
        # Start to heapify from leftmost child
        heapify(unsorted, i, n)
    print("Initial heap:")
    print("\t", unsorted)

    for i in range(n-1, 0, -1):
        # From rightmost child and up
        unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
        # We then heapify the tree from root to the i-th node

        heapify(unsorted, 0, i)
        # Another option is to pop the root every time and heapify again
    
    return unsorted

if __name__ == "__main__":
    data = [4,1,21,5,7,0]
    print(heapSort(data))