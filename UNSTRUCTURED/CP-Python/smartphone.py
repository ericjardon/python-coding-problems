"""Find the optimal price with which you can get the most revenue.
Given N budgets, determine the price that in the most occasions is lower
than or equal to that budget.
In other words we need to find the price P for which N*P (purhcases*price)
is maximized."""
def main():
    N = int(input())
    budgets = []
    for _ in range(N):
        budgets.append(int(input()))
    b = sorted(budgets)
    print(maxrevenue(b))

def maxrevenue(budgets):
    # t. complexity O(n). Brute force because it traverses all scenarios
    n = len(budgets)
    maxRev = 0
    for i in range(n):
        if budgets[i]*(n-i) > maxRev:
            maxRev = budgets[i]*(n-i)
    return maxRev
try:
    main()
except:
    pass

# improvement is to do backtracking: if the next revenue is smaller
# than current max revenue, stop and return.
# this effectively means that marginal benefit is negative

# Challenge: do maxrevenue better than linear time