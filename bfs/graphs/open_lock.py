'''
Consider a lock with four wheels with numbers 0 to 9 (after 9 comes 0 again).
Moves can be done one wheel at a time.
The lock can reacha  dead end state when a combination disables the lock and can no longer move.
The initial state is 000.
Given a list of dead-end combinations and a target representing the combination
to unlock, return the number of minimum moves required to open the lock,
return -1 if it is impossible.
----
Once again a shortest path problem (where nodes in the path are lock states),
so we can solve it with BFS.
'''

import heapq  # for a heap data structure
from collections import defaultdict

# First consider the case where we can jump from any digit to another in a single wheel.


def openLockFull(deadends: list[str], target: str) -> int:
    """
    Dijkstra's algorithm to find all shortest paths to all combinations.
    Deadends act as a limit to search space.
    Returns the minimum path cost to target string.
    """
    # Map of combination->cost (# of moves)
    path_costs = defaultdict(int)  # returns 0 on missing keys

    q = []
    start = (0, '0000')
    # Use a priority queue (min heap) to always pop the least-cost combination first
    heapq.heappush(q, start)
    deadends = set(deadends)  # for quicker checking

    # EDGE CASES
    if '0000' in deadends:
        return -1
    if target == '0000':
        return 0

    # Find all shortest paths to every combination and return the path cost to target
    while q:
        curr_cost, curr_comb = heapq.heappop(q)
        print(f"Current combination {curr_comb}: {curr_cost} moves")

        # For every wheel of the lock
        for pos in range(4):
            # For every possible digit
            for digit in '0123456789':
                next_comb = curr_comb[:pos] + digit + curr_comb[pos+1:]

                # Skip if potential combination is a deadend or is the same as current
                if next_comb in deadends or next_comb == curr_comb:
                    continue

                # If this combination has already been seen, update cost
                if next_comb in path_costs:
                    # Dijkstra relaxation
                    if (curr_cost + 1) < path_costs[next_comb]:
                        path_costs[next_comb] = curr_cost+1
                        # Since cost was updated, reinsert to heap
                        q.remove(next_comb)
                        heapq.heapify(q)
                        heapq.heappush(q, (path_costs[next_comb], next_comb))

                # If this combination is new, set current cost
                else:
                    path_costs[next_comb] = curr_cost+1
                    heapq.heappush(q, (path_costs[next_comb], next_comb))

    # If no path to target was found
    if not path_costs[target]:
        return -1

    return path_costs[target]


# Consider the case where moves can be done only from consecutive digits.
# Implementation is almost the same, all that changes is how we search in BFS

def openLock(deadends: list[str], target: str) -> int:
    path_costs = defaultdict(int)

    q = []
    start = (0, '0000')
    heapq.heappush(q, start)

    deadends = set(deadends)

    # EDGE CASES
    if '0000' in deadends:
        return -1
    if target == '0000':
        return 0

    # Dijkstra to find all shortest paths to every combination
    while q:
        curr_cost, curr_comb = heapq.heappop(q)
        # For every wheel of the lock
        for pos in range(4):
            # For moves left and right of the wheel
            for move in [-1, 1]:
                # 9+1 gives 0 and 0-1 gives 9
                digit = int(curr_comb[pos] + move) % 10

                next_comb = curr_comb[:pos] + str(digit) + curr_comb[pos+1:]

                # Skip if next combination is a deadend or exactly the same as current
                if next_comb in deadends or next_comb == curr_comb:
                    continue

                if next_comb in path_costs:
                    if (curr_cost + 1) < path_costs[next_comb]:
                        path_costs[next_comb] = curr_cost + 1
                        # Since cost was updated, reinsert to queue
                        q.remove(next_comb)
                        heapq.heapify(q)
                        heapq.heappush(q, (path_costs[next_comb], next_comb))

                else:
                    path_costs[next_comb] = curr_cost + 1
                    heapq.heappush(q, (path_costs[next_comb], next_comb))

    # Return -1 if path to target was not found
    if not path_costs[target]:
        return -1

    # Return minimum path cost to target
    return path_costs[target]


if __name__ == "__main__":
    pass
