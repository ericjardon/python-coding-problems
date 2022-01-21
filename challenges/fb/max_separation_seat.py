'''
You're given an array of seats where  1 is occupied, 0 is available

There is at least 1 person sitting and 1 available seat.
Return the maximum distance to the closest person if you must sit.

HINT: this formulation has a lot of edge cases.
The logic is to find the maximum gap and return the maximum distance within that gap.
How to handle gaps in the extremes of the row?
'''
from typing import List

class Solution:
    # In a 1d array, 1 is busy and 0 is available.
    # return max distance to closest occupied seat
    def maxDistToClosest(self, seats: List[int]) -> int:

        max_dist = 1 # min answer possible
        start, end = 0,0
        # max_gap = 0,0
        firstAvail = True

        for i in range(len(seats)):
            if seats[i] == 1:
                print("End of gap", start, end)
                # update max distance based on gap extremes, 
                length = end - start + 1  # length of gap

                if start == 0:
                    max_dist = length
                    print("Beginning gap", max_dist)
                    max_gap = start, end
                
                else:
                    dist = length // 2 + length%2
                    if dist > max_dist:
                        print("Intermediate gap", dist)
                        max_dist = dist
                        max_gap = start, end

                # next available seat is first in gap
                firstAvail = True

            else:
                if firstAvail:
                    print("Start gap", i, end='...')
                    start = i
                    firstAvail = False
                end = i
        
        if end == len(seats) - 1:
            print("Ending gap", end - start + 1)
            max_dist = max(end - start + 1, max_dist)
        
        return max_dist
                        
  

class Solution(object):
    def maxDistToClosest(self, seats):

        N = len(seats)
        # let left[i] hold the max distance to the left of i
        # let right[i] hold the max distance to the right of i
        # if i is occupied, either is 0
        left, right = [N] * N, [N] * N

        for i in range(N):
            if seats[i] == 1: left[i] = 0
            elif i > 0: left[i] = left[i-1] + 1

        for i in range(N-1, -1, -1):
            if seats[i] == 1: right[i] = 0
            elif i < N-1: right[i] = right[i+1] + 1

        return max(min(left[i], right[i])
                   for i, seat in enumerate(seats) if not seat)