## https://leetcode.com/problems/elimination-game/

def lastRemaining(n) -> int:
    # Keep track of both ends of the array; they are possible starts
    leftEnd = 1
    rightEnd = n
    ltr = True  # direction of elimination
    
    # In every pass, distance between consecutive elements 
    # increases by a factor of 2
    # e.g. [1,2,3,4,5,7,8] -> [2,4,6,8] -> [2,6] -> [6]
    step = 1

    while n > 1:
        if ltr:
            leftEnd += step
            if n%2:
                # if length is odd, last element is eliminated
                rightEnd -= step
        else:
            rightEnd -= step
            if n%2:
                # if length is odd, first element is eliminated
                leftEnd += step
        
        # Update our variables
        ltr = not ltr
        n = n // 2  # size decreases by at least half
        step *= 2
    
    return leftEnd  # notice we don't even need to process righEnd


## EXPLANATION
# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
