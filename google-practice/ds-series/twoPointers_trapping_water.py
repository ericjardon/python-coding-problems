
# We should find valleys and determine their depth
# A valley exists when the current value in an array is less than any values on _either_ side

# Closing window approach
# Max amount of water that can be trapped is determined by the lower height to either side
# As we close in our pointers, accumulate water as long as 
# left pointer is smaller than right pointer and current left ptr is smaller than tallestLeft
# else if current right pointer is smaller than tallestRight

def trapRainWater(heights: list[int]) -> int:
    if not heights or len(heights) < 3: # no trappable water
        return 0
    
    left=0
    right=len(heights) - 1

    # tallest heights
    left_max = 0
    right_max = 0
    # answer
    water = 0

    # Sliding Window
    while left <= right:
        # print("left, right", left, right)
        # Choose pointer to work with: whichever is smaller height
        if heights[left] < heights[right]: # max width valley is restricted by left
            if heights[left] > left_max:
                # update tallest left and continue
                left_max = heights[left]
            else:
                # valley, bound by left_max and potentially heights[right]
                water += left_max - heights[left]
            left += 1 # close in left pointer
        else:                               # max width valley is restricted by right
            if heights[right] > right_max:
                # update tallest right and continue
                right_max = heights[right]
            else:
                # valley, bound potentially by heights[left] and right_max
                water += right_max - heights[right]
            right -= 1 # close in right pointer
    
    return water



# TEST CASES
print(trapRainWater([0,1,0,2,1,0,1,3,2,1,2,1])) # EXPECT 6
print(trapRainWater([4,2,0,3,2,5])) # EXPECT 9