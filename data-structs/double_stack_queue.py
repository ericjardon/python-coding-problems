
class TwoStackQueue():
    """
    Idea of a 2-stack queue is for one queue to be used for enqueuing and another for dequeuing.
    Stack 2 will either be empty or contain elements in reverse order. (first half of the queue).
    Stack 1 is used for receiving elements as a normal stack (second half of the queue).
    For either enqueuing or dequeuing we 'pour' the elements of one stack into the other and the pop.
    This way we always get the front element (the bottom of original stack before pouring).
    We have to choose either enqueuing or dequeuing to be the costly O(n) operation.
    """

    # Let the top be the last index.
    enqStack = [] # stack 1 for enqueuing
    deqStack = [] # stack 2 for dequeuing 
    
    def __init__(self):
        super().__init__()

    def enqueue(self, x):
        self.enqStack.append(x)
    
    def dequeue(self):
        if not self.deqStack and not self.enqStack:
            # Queue is empty
            return

        # If stack 2 is empty, all elements in stack 1 are moved to stack 2.
        # We return the top element of stack 2.
        if not self.deqStack:
            while len(self.enqStack):
                self.deqStack.append(self.enqStack.pop())
            
        return self.deqStack.pop()

    def peek(self):
        if not self.deqStack and not self.enqStack:
            # Queue is empty
            print("Queue is empty")
            return
        
        if not self.deqStack:
            while len(self.enqStack):
                self.deqStack.append(self.enqStack.pop())
            
        print(self.deqStack[-1])
        


    

if __name__ == "__main__":

    q = TwoStackQueue()

    queries = int(input())
    
    for _ in range(queries):
        query = input().split()
        if query[0] == '1':
            # enqueue
            q.enqueue(int(query[1]))
        elif query[0] == '2':
            # enqueue
            q.dequeue()
        else:
            # peek
            q.peek()