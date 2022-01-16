from typing import Iterable, List, Optional

# Array representation of tree:
# A parent at index i has left child in 2*i+1 and right in 2*i+2

class Heap:     # Generic implementation of a max heap
    """With methods:
        - build_max_heap
        - extract_max (pop)
        - insert (push)
        - heap_sort
    """

    def __init__(self):
        self.h: List[float] = list()
        self.heapSize: int = 0

    def __repr__(self) -> str:
        return str(self.h)

    def parentIdx(self, child: int) -> Optional[int]:
        "Return the index of parent element of a elem given child index"
        if child > 0:    # if is not the root
            return (child - 1) // 2
        return None         # when idx==0 (root)

    def leftChild(self, parent) -> Optional[int]:
        "Return index of left child if exists, else None"
        left = 2 * parent + 1
        if left < self.heapSize:
            return left
        return None

    def rightChild(self, parent) -> Optional[int]:
        right = 2 * parent + 2
        if right < self.heapSize:
            return right
        return None

    def max_heapify(self, index: int) -> None:
        """Correct a single violation of max-heap property for a single subtree rooted at i,
            recursively heapify at swapped child"""
        if index < self.heapSize:       # sanity check
            # swap the largest of the three with the previous root
            temp: int = index
            left: int = self.leftChild(index)
            right: int = self.rightChild(index)
            if left is not None and self.h[left] > self.h[temp]:
                temp = left
            if right is not None and self.h[right] > self.h[temp]:
                temp = right
            # swap elems in array if there was a violation (root was not the largest)
            if temp != index:
                self.h[temp], self.h[index] = self.h[index], self.h[temp]
                self.max_heapify(temp)      # continue heapification in the new swapped child

    def build_max_heap(self, collection: Iterable[float]) -> None:
        """Given an unsorted list of items build a heap"""
        self.h = list(collection)      # copy of collection
        self.heapSize = len(self.h)
        if self.heapSize > 1:
            # Perform heapify from right to left. (bottom-up the tree, starting from last parent-level)
            # Heapify operation is useless for leaves, so we exclude the last level
            # Last level corresponds to second half of array.
            for i in range(self.heapSize//2 -1, -1, -1):  # for every parent node
                self.max_heapify(i)

    def max(self) -> float:
        """Peek the max element from heap"""
        if self.h:
            return self.h[0]
        else:
            raise Exception("Empty heap")

    def extract_max(self) -> float:
        """Get and remove the root of heap"""
        if self.heapSize>1:
            root: float = self.h[0]
            self.h[0] = self.h.pop(-1)  # replace with last element in heap
            self.heapSize = len(self.h) # update size of heap
            self.max_heapify(0)         # heapify from the top
            return root
        elif self.heapSize==1:
            self.heapSize -= 1
            return self.h.pop(0)
        else:
            raise Exception("Empty heap")

    def insert(self, val: float) -> None:
        """Push the specified value into the heap preserving heap order"""
        self.h.append(val)    # by default to the last position
        index: int = (self.heapSize - 1) // 2  # previously first leaf node in array (now has 1 child, i.e. last index)
        self.heapSize += 1
        while index is not None:
            self.max_heapify(index)     # heapify subtrees all the way up
            index = self.parentIdx(index)

    def heap_sort(self) -> None:
        """Sorts the internal array in ascending order"""
        size = self.heapSize
        # convention of j-index because it decreases
        for j in range(size-1, 0, -1):  # swap the root with jth element, heapify and again
            self.h[0], self.h[j] = self.h[j], self.h[0]
            self.heapSize -= 1
            self.max_heapify(0) # heapify for j-1 elements (so we exclude the item at j)
        self.heapSize = size

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    for unsorted in [
        [0],
        [2],
        [3, 5],
        [5, 3],
        [5, 5],
        [0, 0, 0, 0],
        [1, 1, 1, 1],
        [2, 2, 3, 5],
        [0, 2, 2, 3, 5],
        [2, 5, 3, 0, 2, 3, 0, 3],
        [6, 1, 2, 7, 9, 3, 4, 5, 10, 8],
        [103, 9, 1, 7, 11, 15, 25, 201, 209, 107, 5],
        [-45, -2, -5],
    ]:
        print(f"unsorted arr: {unsorted}")
        heap = Heap()
        heap.build_max_heap(unsorted)
        print(f"initial max-heap: {heap}")
        print(f"max value is {heap.extract_max()}")
        print(f"heap after popping max {heap}")
        heap.insert(100)
        print(f"heap after inserting 100: {heap}")
        heap.heap_sort()
        print(f"heap-sorted array: {heap}\n")
        print("========END TEST =========")
