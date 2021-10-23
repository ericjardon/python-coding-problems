# Given n
from typing import List


def numberOfMatches(n: int) -> int:

    teams = n
    matches = 0
    while (teams>1):
        if teams%2==0:
            matches += teams/2
            teams = teams/2
        else:
            matches += (teams-1)/2
            teams = (teams-1)/2 + 1

    return int(matches)

def minPartitions(self, n: str) -> int:
    # Decibinary number 1001 any comb of 1 and 0 starting in 1
    # Given n how many decibinaries do we need?
    max = 0
    for digit in n:
        if int(digit) == 9:
            return 9
        if int(digit) > max:
            max = int(digit)

    return max


def stoneGameVII(stones: List[int]) -> int:
    # Alice and Bob play greedily
    # Alice picks first
    scoreA = 0
    scoreB = 0
    aliceTurn = True
    while len(stones)>1:
        if aliceTurn:
            # Alice picks the lower value
            if sum(stones[1:]) > sum(stones[:-1]):
                del stones[0]
                scoreA += sum(stones)
            else:
                del stones[-1]
                scoreA += sum(stones)
        else:
            # pick the stone for which the gain of Alice is minimum no matter her decision
            if len(stones)>2:
                if (sum(stones[2:])) < (sum(stones[:-2])):
                    # lo que le toca a alice en el futuro debe ser el mínimo
                    del stones[0]
                    scoreB += sum(stones)
                else:
                    del stones[-1]
                    scoreB += sum(stones)
            else:
                if stones[0] > stones[2]:
                    del stones[2]
                    scoreB += stones[0]
                else:
                    del stones[0]
                    scoreB += stones[0]

        aliceTurn = not aliceTurn
    return scoreA - scoreB
    # ABSOLUTE FAILURE, LEARN DP AND GAME-THEORY-RELATED PROBLEMS
