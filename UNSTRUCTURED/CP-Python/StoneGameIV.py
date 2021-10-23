# EXPLANATION
# Alice and Bob are playing a game, Alice starts first.
#    There are n stones, blocks or whatever in a pile, each player must remove
#    an exactly square number of items from the pile. If the player cannot make a move,
#    he/she loses.
#    If Bob and Alice were to play optimal strategies, the outcome becomes determined
#    from the start.
#    Thus, given the initial number n, there is a way to determine with certainty
#    who is the player that wins.
# HINT (LEETCODE): Use dynamic programming to keep track of winning and losing states. Given some number of stones,
#   Alice can win if she can *force* Bob onto a losing state.

from math import sqrt
def StoneGameIV(n : int):
    """Given n the initial number of stones in the pile,
        Return True if Alice wins."""
    # Solution: use Dynamic Programming to keep track of the determined outcome
    # of an initial number i of stones in the pile: either True for Alice wins
    # or False for Alice loses.

    dp = [None] * 100005  # Python list pre-allocation of size. max n is 10^5
    # Tabular DP: Base cases
    dp[1] = True    # because 1 is a perfect square, Alice leaves 0 to Bob and Alice wins
    dp[2] = False   # Alice can only take 1, Bob takes 1 and Alice loses
    dp[3] = True    # Alice takes 1, Bob takes 1, Alice takes 1 and Bob loses.

    squares = [1]
    for i in range(4, n+1):
        # Calculate the outcomes for cases 4 and up to n
        sq = int(sqrt(i))
        if (i == sq*sq): # if i is a perfect square add it
            squares.append(i)
            # PD if initial n is perfect square player automatically wins
            dp[i] = True
            continue
        win = False     # flag to know if alice wins with n=i
        for square in squares:
            # determine if any perfect square amount less than i allows for a win
            if dp[i - square] == False:
                # means taking sq stones leaves Bob's turn in False (lose)
                win = True
                break
        dp[i] = win     # Assign the outcome True or false to the game with n=i

    return dp[n]     # in the end return the outcome for the game with n=n