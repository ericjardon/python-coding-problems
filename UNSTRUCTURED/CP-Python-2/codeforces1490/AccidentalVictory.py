# N players, each with a positive number of tokens
# N-1 games are played, according to following rules:
# 1. each game, 2 players with tokens >=1 are selected at random.
# 2. whoever has more tokens is the winner. If tie, winner is chosen randomly.
# 3. The winner takes all of the loser's tokens.
# 4. the last player remaining with non-zero tokens is the winner.

# Any championship can have one or more outcomes.
# >>Given N and the number of tokens of each player,
# find all players that have non-zero probability of winning.
def findAllOutcomes(A, n):
    # for every possible initial pair?

    return A

def probableWinners(A, n):
    # print the index+1 of winning players in increasing order (as they came in A)
    # brute force all of the outcomes, use a set of seen winners.
    # print those seen winners
    winners = findAllOutcomes(A, n)
    winners.sort()
    for i in range(len(winners)-1):
        print(winners[i], end=' ')
    print(winners[-1])

for t in (range(int(input()))):
    n = int(input())
    A = [int(x) for x in input().split(" ")]
    # The sum of n over all test cases does not exceed 2*10**5
    probableWinners(A, n)
