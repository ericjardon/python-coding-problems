from typing import List
class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        N = len(chargeTimes)
        # try sliding window
        # we have two pointers i and j
        # j moves forward as long as it is within budget.
        # keep track of max length: (i-j+1)
        # if j exceeds budget, now move i forward, stop when we're within budget again.
        # repeat 
        max_k = 0
        i = 0
        j = -1
        
        # Initial state variables
        max_time = chargeTimes[0] # arr length is at least 1
        run_cost = 0
        
        while j < N-1: # lookahead loop; and i < N
            # moving j forward
            j += 1
            k = j-i+1
            max_time = max(max_time, chargeTimes[j])
            run_cost += runningCosts[j]
            cost_total = max_time + k*run_cost
            exceedsBudget = cost_total > budget

            # move i forward, stop when we're within budget
            while exceedsBudget and i<j: #i < N-1:
                # print("push i", i,j)
                i += 1
                k = (j-i+1)
                if k<=0: break # skip and start at new j
                # recalculate max time if necessary
                if chargeTimes[i-1] == max_time:
                    max_time = max(chargeTimes[i:j+1])
                # Update running costs
                run_cost -= runningCosts[i-1]
                cost_total = max_time + k*run_cost
                exceedsBudget = cost_total > budget
                # print(i,"to",j,"cost", cost_total)

            # print(i,"to",j,"cost", cost_total)
            if not exceedsBudget:
                max_k = max(k, max_k)

        return max_k
        # TLE; probably because of the while loops or the max() call


# solution uses a priority queue for max times
# and a separate counter dictionary to know which times are out of our window.
# we add to pq every chargeTime[j] and to the dictionary also d[time[j]] += 1
# when we remove front element i, discount it from d
# when we check max element, check that d[pq[0]] > 0 else pop it until d[pq[0]] > 0

# Another option is binary search
# k is the length of window
# we search for k, and then at every test k, traverse the array in slices of k
# since we want max k, duplicate every time. When k exceeds, move into the middle of last k and current k.

# Solution().maximumRobots()
            
for i in range(6):
    i =5
    print(i)
print("end",i)
"""
[3,6,1,3,4]
[2,1,3,4,5]
25
[11,12,19]
[10,8,7]
19
[1]
[1]
5
[10,10,1]
[10,10,9]
9
[74,46,19,34,7,87,7,40,28,81,53,39,3,46,21,40,76,44,88,93,44,50,22,59,46,60,36,24,50,40,56,5,39,9,24,74,7,14,95,45,36,17,22,12,53,41,2,33,100,73,20,70,81,91,28,98,47,88,79,100,78,38,44,74,48,76,73,92,28,30,95,87]
[11,33,15,40,8,28,97,89,51,42,17,57,45,5,63,53,23,43,76,64,86,86,89,53,94,91,78,12,90,29,79,48,35,6,88,79,82,76,44,93,83,55,65,96,86,24,54,65,94,4,26,73,51,85,47,99,17,14,76,2,39,52,58,5,15,35,79,16,94,16,59,50]
447
"""