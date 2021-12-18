'''
Youre given an array `customers` that holds lists of [arrivalTime, timeToPrepare].
There is a single chef receiving the orders and the customers in the order they arrive.
He can only prepare for a single customer at a time.
He prepares food for customers in the order they're given in the input.

Return the average waiting time across al customers.

- customers is given in non-decreasing order (arrivalTime)

'''



from typing import List
from collections import deque

def mean(list):
    return 1.0*(sum(list)) / len(list)

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # Construct an array fo waiting times for each customer.
        # At the end simply take the mean.
        
        s = 0.0
        n = len(customers)

        q = deque(customers)
        time_ready = 0
        time_waited = 0


        while q:
            ta, tte = q.popleft() # time of arrival, time to execute
            #print(ta,tte, end=" || ")
            if ta>time_ready:
                time_ready = ta

            time_waited = time_ready - ta
            total_wait = time_waited + tte
            
            s += total_wait

            time_finished = time_ready + tte
            #print(f"tready:{time_ready}\ttwaited:{time_waited}\ttotal wait:{total_wait}\ttime finished:{time_finished}")
            time_ready = time_finished
        
        return s / n

c = [[1,2],[2,5],[4,3]]
x = Solution().averageWaitingTime(c)
print(x)