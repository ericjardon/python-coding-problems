'''
In a tennis tournament of N players, every player plays against every other player.

The rules are as follows:

If p1 won over p2, and p2 won over p3, then
p1 has won over p3.

Find winner of the tournament in O(N) time and O(1) space;
Find the ranking of players in O(NlogN) time


VERSION 1:
- Given: list of (p, [win1, win2, win3,...])

VERSION 2:
- Given list of tuples (winner, loser)

'''

from typing import List, Tuple


class Tournament():

    def __init__(self, games: List[Tuple[int, List[int]]]):
        self.games = {
            p: set(defeated) for p, defeated in games
        }


    def get_tournament_winner_v1(self):
        # return the difference between total players and tota defeated players
        return (
            set([player for player, _ in self.games])) - \
                set([player for defeated, _ in self.games for player in defeated]) # for every player defeated in every list of defeats

    def get_ranking(self):
        # Sort the players by merge sort where player's 
        # pairwise matches determine which elemtn is larger

        ranking = list(self.games.keys())

        return self.mergeSortPlayers(ranking, len(ranking))


    def merge(self, B, p, C, q, A, n):
        """ Out of place sorting"""
        # receive the lengths of both halves which are always p+q == n
        i,j,k = 0,0,0   # counter for B, C and A respectively

        def winsOver(pA, pB):
            if pB in self.games[pA]:
                return True
            else:
                return False

        while i<p and j<q:      # choose whichever is smaller from next elem of B or C: Bi vs Cj
            if winsOver(B[i], C[j]):
                A[k] = B[i]
                i+=1
            else:
                A[k] = C[j]
                j+=1
            k += 1

        if i == p:      # means we finished the B subarray, Copy the remaining C elems
            while j < q:
                A[k] = C[j]
                j+=1
                k+=1
        else:
            while i < p: # Copy the remaining B elems
                A[k] = B[i]
                i += 1
                k += 1


    def mergeSortPlayers(self, A, n):    # in-place sorting
        # A is the array to be split into two halves
        # B is the first half and C is the second half.
        # we can only apply mergeSortPlayers when len > 1
        if n > 1:
            B = A[0: n//2]      # slicing takes the references to the inner elements of the list not a new copy
            C = A[n//2:]        # by slicing we can divide and conquer and have subarrays within the array
            self.mergeSortPlayers(B, len(B))    # in place works because even though indexes are changing, the references point to the same objects of original A
            self.mergeSortPlayers(C, len(C))
            merge(B, len(B), C, len(C), A, n)
        # if array len == 1 leave as is
