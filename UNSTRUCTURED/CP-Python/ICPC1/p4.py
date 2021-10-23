"""Halloween:
    Baker goes through the neighbourhood's houses in a linear fashion.
    Neighbours will not give him candy if Baker has asked for candy in
    an adjacent house.
    This is a version of the coin row problem where the values are the
    number of candies at each house."""
houses = [9, 21, 33, 31, 21, 84, 86, 53]
# BRUTE FORCE APPROACH
def maxCandy(houses, n):
    # n starts at the last index
    if n<0:     # no houses left
        return 0

    ask = maxCandy(houses, n-2) + houses[n]
    not_ask = maxCandy(houses, n-1)

    return max(ask, not_ask)

# print(maxCandy(houses, len(houses)-1))

# DP APPROACH
def memoMaxCandy(houses, n, memo):
    if n not in memo:
        # if not on the table, calculate it
        if n<0:     # base case: no houses left
            return 0
        else:
            take = memoMaxCandy(houses, n-2, memo) + houses[n]
            not_take = memoMaxCandy(houses, n-1, memo)
            memo[n] = max(take, not_take)

    return memo[n]

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        line = input().split(" ")
        houses = [int(h) for h in line]
        print(memoMaxCandy(houses, n-1, {}))
main()