# Fibonacci Heap

# Order of a tree: the maximum degree among the nodes of the tree.
# Degree of a node: the number of children of that node.

# What is a fib heap useful for? For further imporving running time od Dijkstra

import math
class FibonacciTree:        # or rather, a FibonacciNode
    def __init__(self, value):
        self.value = value
        self.children = []
        self.order = 0      # the max number of children a node can have

    def add_to_end(self, t):    # to join a tree to the end of this tree
        self.children.append(t)
        self.order = self.order + 1     # order is the number of nodes of this tree (sic)

class FibonacciHeap:
    def __init__(self):
        self.trees = []     # a set of trees in a doubly linked circular list
        self.min = None     # points to the tree with minimum value
        self.count = 0

    #Insertion
    def insert_node(self, value):
        new_tree = FibonacciTree(value)
        self.trees.append(new_tree)
        if (self.min is None or value < self.min.value):
            self.min = new_tree     # reassign a pointer if there is a new smaller value
        self.count += 1

    def get_min(self):
        if self.min:
            return self.min.value
        return None

    def pop_min(self):
        smallest = self.min
        if smallest is not None:
            for child in smallest.children:
                self.trees.append(child)        # every child is set as a tree of the set
            self.trees.remove(smallest)     # remove it from the set of tress
            if self.trees == []:        # smallest had no children
                self.min = None
            else:
                self.min = self.trees[0]    # new min is the first in the set of trees
                self.consolidate()          # analogous to heapify in a binary heap
            self.count -= 1
            return smallest.value       # return the value removed from Heap

    # Consolidation:
    def consolidate(self):      # supposedly a logN operation
        # Reorganizes every tree in the list to be children of a smaller-value tree.
        def floor_log(x):
            return math.frexp(x)[1] - 1     # frexp returns the mantissa and exponent of a number (m,e), i.e. scientific notation

        aux = (floor_log(self.count) + 1 ) * [None]
        while self.trees != []:     # as long as there are trees in the old list
            x = self.trees[0]
            order = x.order
            self.trees.remove(x)        # removing every tree of the list
            while aux[order] is not None:   # if the slot we will put it in is occupied
                y = aux[order]      # y is the tree in the slot
                if x.value > y.value:      # the one who is smaller will prevail in the slot
                    x,y = y,x
                x.add_to_end(y)     # we want the smaller to be parent of the larger
                aux[order] = None   # we leave the slot empty
                order += 1          # move to the next slot to see if y can be child to x
            aux[order] = x      # put the removed tree in its slot corresponding to order (which will be the number of children we appended to x)

        # Finally convert the trees in aux to the heap's list
        # and update the self.min pointer
        self.min = None
        for k in aux:
            if k is not None:
                self.trees.append(k)
                if self.min is None or k.value < self.min.value:
                    self.min = k        # reassign if there's a new smallest val

def test():
    fib_heap = FibonacciHeap()
    fib_heap.insert_node(7)
    fib_heap.insert_node(3)
    fib_heap.insert_node(17)
    fib_heap.insert_node(24)
    print("Min value of the fibonacci heap is: {}".format(fib_heap.get_min()))
    print("Removing the min value: {}".format(fib_heap.pop_min()))
    print("New min: {}".format(fib_heap.get_min()))

test()