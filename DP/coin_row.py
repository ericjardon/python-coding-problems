'''
There is a row of n coins whose values are some positive integers C0, C2, . . . , Cn-1, 
not necessarily distinct. The goal is to pick up the maximum amount of money 
subject to the constraint that no two consecutive coins
can be picked up.
'''
from random import choice
# This is also a basic take/not-take type of problem that can be 
# solved with Brute Force but also with Memoization.

def coin_row(coins, i):
    # Traverse array recursively, from back to front
    # Complexity O(2^n)

    if i < 0:  # coin row is finished
        return 0
    if i == 0:
        return coins[0]

    take = coin_row(coins, i-2) + coins[i]
    not_take = coin_row(coins, i-1)

    return max(take, not_take)
    
# Coin Row is a candidate for DP as it has overlapping subproblems
# and optimal substructure (combination of all optimal solutions is the optimal global solution).

def coin_row_dp(coins, i, dp):
    if dp[i] == -1:
        # If value is not cached, calculate it
        if i < 0:  # coin row is finished
            return 0
        if i == 0:
            return coins[0]

        take = coin_row_dp(coins, i-2, dp) + coins[i]
        not_take = coin_row_dp(coins, i-1, dp) 
        dp[i] = max(take, not_take)
    
    return dp[i]

# DP using iterative tabulation approach
def coin_row_tab(coins, n):
    dp = [-1 for _ in range(n+1)]  # size n + 1

    dp[0] = 0
    dp[-1] = 0  # good thing we have an extra space at the end 

    # The solution is built bottom up.
    # dp[i] holds the maximum result after i decisions
    # So dp[i] holds the best answer after n decisions
    for i in range(1, n):
        take = coins[i] + dp[i-2]  
        not_take = coins[i-1]

        dp[i] = max(take, not_take)

    return dp[n]


def testCoinRow(arr, mode):
    N = len(arr)
    if mode=="memo":
        memo = [-1 for _ in range(N)]
        print(coin_row_dp(arr, i=N-1, dp=memo))

    elif mode=="table":
        print(coin_row_tab(arr, N))

    else:
        print(coin_row(arr, i=N-1))



n = 10
denoms = [5, 2, 1, .5, .2, .1]
coins = [choice(denoms) for _ in range(n)]

print("Coins", coins)
testCoinRow(coins, n)
testCoinRow(coins, mode="memo")
testCoinRow(coins, mode="tab")