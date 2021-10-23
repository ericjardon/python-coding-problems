""" the player uses N coins numbered from 1 to N, all the coins facing the same direction from the start.
Playing N rounds, where at each round k, the first k coins are flipped.
After N rounds how many coins are facing up or down?"""

# We will take tails to be TRUE, heads to be FALSE
import math


def coinflip(I, N, Q):
    # I: 1 for heads (FALSE), 2 for tails (TRUE)
    # Q: 1 to return #heads, 2 to return #tails
    # I is a trivial parameter. We start all coins as True.
    # If I==Q, we return True values, else we return False values.
    coins = [True for _ in range(N)]
    count = N
    for i in range(N):
        if (N-i) % 2 != 0:  # odd number
            coins[i] = False
            count -=1

    if I==Q:
        return count
        #return sum(coins)
    else:
        return N - count
        #return N - sum(coins)

# takes too long
# the resulting coin array is always intercalated. When true is always initial, odd arrays start with F and even ones start with True.
#print(coinflip(1, 10, 2))

def fasterCoinflip(I, N, Q):
    if I==Q:
        return int(math.floor(N/2))
    else:
        return int(math.ceil(N/2))

def main():
    try:
        T = int(input())
        for _ in range(T):
            G = int(input())
            for game in range(G):
                INQ = input().split(" ")
                I = int(INQ[0])
                N = int(INQ[1])
                Q = int(INQ[2])
                print(fasterCoinflip(I, N, Q))
    except Exception as e: print(e)

main()
