"""
You have n robots. You are given two 0-indexed integer arrays, chargeTimes and runningCosts, both of length n. The ith robot costs chargeTimes[i] units to charge and costs runningCosts[i] units to run. You are also given an integer budget.

The total cost of running k chosen robots is equal to max(chargeTimes) + k * sum(runningCosts), where max(chargeTimes) is the largest charge cost among the k robots and sum(runningCosts) is the sum of running costs among the k robots.

Return the maximum number of robots you can run such that the total cost does not exceed budget.
* the true version requires _consecutive_ robots
"""
# def getCost(indexes, all_times, all_costs):
#     times = [all_times[i] for i in indexes]
#     costs = [all_costs[i] for i in indexes]
#     print(len(times), len(costs))
#     t = max(times)
#     print("maxTime", t)
#     kc = len(times)*sum(costs)
#     print("k", len(times))
#     print("k * cost", kc)
#     print("total=", t + kc)
from typing import List

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        # Find highest k such that totalCost(k,...) <= budget.
        # k can be composed of different permutations of robots.
        # does order matter? -> no, it's a sum.
        
        def findK(times, costs, i, cost_time, cost_run, cost, k_so_far, memo, i_til_now):
            if cost > budget:
                return (-1, [])

            if i == len(times):
                return (k_so_far, i_til_now)
            
            if (i, cost) not in memo:
                skip, i_skip = findK(times, costs, i+1, cost_time, cost_run, cost, k_so_far, memo, i_til_now)
                
                new_k = k_so_far + 1
                new_cost_time = max(cost_time, times[i])
                new_cost_run = cost_run + costs[i]
                new_cost = new_cost_time + (new_k)*new_cost_run
                
                take, i_take = findK(times, costs, i+1, new_cost_time, new_cost_run, new_cost, new_k, memo, i_til_now + [i])
                if skip > take:
                    memo[(i, cost)] = (skip, i_skip)
                else:
                    memo[(i,cost)] = (take, i_take)

            return memo[(i, cost)]
        
        memo = {}
        ans = findK(chargeTimes, runningCosts, 0, 0, 0, 0, 0, memo, [])
        print(ans)
        return ans[0]