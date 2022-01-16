'''
    Given k sorted arrays with N elements in each.
    Implement an iterator for iterating over the elements in ascending order.
    Do not modify the provided data.
    You can only use O(K) extra data.

    Your implementation should have next() and hasNext() methods.

'''

import heapq
from typing import List
# heapq.heappush(heap, item)
# heapq. heappop(heap)
# heapq.heapify(list)

class MyIterator():
    
    def __init__(self, data) -> None:
        self.data = data
        # We can only use K extra space
        # Priority Queue
        self.pq = []
        # the index of next element in the i-th list (K lists)
        self.k = [0 for _ in range(len(data))] 
        self.preProcess(data)

    def next(self):
        # Remove item from our queue, increase index val for appropriate array. 
        tmp = heapq.heappop(self.pq)
        self.postProcess(tmp) 
        return tmp

    def hasNext(self):
        # Simply return if priority queue is empty or not
        return len(self.pq) > 0
    
    def preProcess(self, data: List[List[int]]):
        for i in range(len(self.k)):
            # push the indexes of smallest k elements?
            heapq.heappush(self.pq, data[i][self.k[i]])
        
        
    def postProcess(self, removed: int):
        # For every list in data
        for i in range(len(self.k)):
            # Update index of list who popped
            if self.k[i] < len(self.data[i]) and self.data[i][self.k[i]] == removed:
                self.k[i] += 1 # move to the next index in the ith list
            
                # Push the next element in the i-th list to priority queue
                if self.k[i] < len(self.data[i]):
                    heapq.heappush(self.pq, self.data[i][self.k[i]])
                    # The next element in the i-th llist is added to pq
            

data = [[1,5,7],[2,3,10],[4,6,9]]

it = MyIterator(data)

while it.hasNext():
    print(it.next(), end=' ')