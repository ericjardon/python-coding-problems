from typing import List
from collections import deque

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # We can always push an item to stack.
        # We cannot always pop an item.
        # To pop an item, the head of our artificial stack must match.

        # If we finish all popped operations, we know it's True.

        stack = deque()
        M, N = len(pushed), len(popped)
        # While there are push and pop operations
        i, j = 0 , 0
        while i < M and j < N:
            # Push to stack every time
            stack.append(pushed[i])
            i += 1

            # Pop whenever we can as many as we can
            while j < N and len(stack) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        
       # Pop remaining elements if there are any
        while j < N and len(stack) and stack[-1] == popped:
            stack.pop()
            j += 1

        return j == N