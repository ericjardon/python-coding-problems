


from heapq import *

class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        
        if not self.small or num < -self.small[0]:
            heappush(self.small, -num)
        else:
            heappush(self.large, num)
            
        if len(self.small) == len(self.large) + 2:
            heappush(self.large, -heappop(self.small))
            
        if len(self.large) == len(self.small) + 1:
            heappush(self.small, -heappop(self.large))

    def findMedian(self) -> float:
        
        if len(self.small) == len(self.large):
            return (-self.small[0] + self.large[0]) / 2
        else:
            return -self.small[0]


def solve(arr):
    # For every index i, return the median of the sorted array from 0..i inclusive
    out = [v for v in arr]

    mf = MedianFinder()
    for i in range(len(arr)):
        mf.addNum(arr[i])
        out[i] = mf.findMedian()
    return out

if __name__=="__main__":
    # TODO
    ex = []