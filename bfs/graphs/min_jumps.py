"""Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index."""

from typing import List
from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        # implement bfs
        END = len(nums) - 1
        jumps = 0
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        print("Start queue", q)
        print("Need to reach", END)
        while q:
            size = len(q)

            # For every possible position enqueued in previous jump
            for _ in range(size):
                currPos = q.popleft()
                print("current:", currPos)
                if currPos == END:
                    return jumps
                elif currPos > END:
                    continue
                for jump in range(1, nums[currPos]+1):
                    # enqueue a possible position
                    next = currPos + jump
                    if next not in visited:
                        visited.add(next)
                        q.append(next)
            print("queue", q)
            # Number of jumps
            jumps += 1

nums = [2,3,1,1,4]
Solution().jump(nums)