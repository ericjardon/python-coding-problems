'''
Given an array of heights "h", which contains n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.
'''

class Solution:
    def trap(self, h):
        N = len(h)
        # Two-pointer approach
        i = 0
        j = N - 1

        leftWall = h[0]
        rightWall = h[N-1]

        total = 0

        # Two pointers can tell us if water can be contained and from which side
        while (i < j-1):
            if (leftWall < rightWall):  # we know we can at least up to right wall
                # check if next wall is taller
                i += 1
                if (h[i] <= leftWall):  # h[i] is smaller than both left and right wall
                    total += (leftWall - h[i]) 
                else:                   # nothing can be contained
                    leftWall = h[i]  # update our left wall
            
            else:    # we know we can contain at least up to left wall
                # check if next wall is taller
                j -= 1
                if (h[j] <= rightWall): # h[j] is smaller than both right and left wall
                    total += (rightWall - h[j])
                
                else:
                    rightWall = h[j]  # update right wall
        
        return total