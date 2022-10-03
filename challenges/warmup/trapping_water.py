from typing import List
'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it can trap after raining.
'''


class Solution:
    def trap(self, heights: List[int]) -> int:
        # Stack solution, not the fastest 
        
        N = len(heights)
        stack = []
        water = 0
        # Go left to right, only stack bars (indexes) that
        # are leq than previous one. Bars are stacked in decreasing order.
        for i in range(N):
            # Check if this wall bounds previous ones
            while (stack and heights[i] > heights[stack[-1]]):
                # save this bar
                popped = stack.pop()
                # If stack empty, there is no bounding bar to the left
                if (not stack):
                    break
                
                # Else, top of stack is larger than popped bar
                # Calculate water above this bar: height difference times distance
                d = i - stack[-1] - 1 # from current to other bounding wall
                h = min(heights[i], heights[stack[-1]]) - heights[popped]
                # add to result
                water += d * h
                
            # The loop ends when top of stack is larger or when stack is empty
            # so i is the new latest 'smaller' bar 
            stack.append(i)
        
        return water
            