from typing import List

class Solution:
    " 148 / 151 testcases passed, but Time Limite Exceeded"
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # We can either push, or pop (2 options)
        # First operation must be push.
        # After that, we can do backtracking to find a possible combination.
        from collections import deque

        # essentially we want to find the combination of pushed and popped
        # operations, namely the sequence push, pop that empties out the arrays.
        if len(popped) > len(pushed):
            return False

        if len(pushed) == 0:
            return len(popped) == 0

        # All possible combinations of push, pop
        def findSequence(i, j, pushed, popped, st):
            if i==len(pushed) and j == len(popped):
                # all operations have been made
                return True
            
            # Push: try to advance i
            if i == len(pushed):
                # cannot push if there are no push operations
                push = False
            else:
                st_push = st.copy()
                st_push.append(pushed[i])
                push = findSequence(i+1, j, pushed, popped, st_push)

            # Pop: try to advance j
            if len(st) == 0 or j == len(popped) or popped[j] != st[-1]:
                # cannot pop if st is empty, there are no pop operations,
                # or if top does not match
                pop = False
            else:
                st_pop = st.copy()
                st_pop.pop()
                pop = findSequence(i, j+1, pushed, popped, st_pop)

            return pop or push

        return findSequence(0,0, pushed, popped, deque())
                



