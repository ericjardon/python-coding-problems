'''
Given an NxN board numbered boustrophedonically. Start from bottom left.
Normal squares are valued -1. Squares representing snakes or ladders have 
the number of the square number they lead to.
At any square you have 6 possible choices forward (like a dice).
Return the LEAST number of moves required to reach the last square (numbered N*N)
'''

from collections import defaultdict  # for missing keys
from collections import deque   # regular doubly-linked queue
import heapq    # priority queues


class SnakesAndLadders:

    # STANDARD BFS APPROACH
    def solveWithBFS(board: list[list[int]]) -> int:
        N = len(board)

        def getCoords(squareNum):
            """
            Helper function to calculate row and column of a given square number
            in a boustrophedonically numbered board, represented by a NxN grid
            """
            row_bottomUp, col = divmod(
                squareNum - 1, N)  # returns (quotient,residual)
            # If row is odd, column order is counted in reverse.
            if row_bottomUp % 2:
                col = (N - col) - 1  # additive complement from N, zero based

            # additive complement from N, zero based
            row = (N - row_bottomUp) - 1
            return row, col

        start = (1, 0)   # (square number, moves)
        queue = deque([start])
        visited = set()
        visited.add(1)

        while queue:
            size = len(queue)
            # Loop over all enqueued nodes in the current search tree level
            for i in range(size):
                square_num, moves = queue.popleft()
                if square_num == N*N:
                    # end of board, return number of moves
                    return moves

                # For every possible dice value
                for i in range(1, 7):
                    s = square_num + 1
                    s_row, s_col = getCoords(s)

                    # If square exists on the board
                    if (0 <= s_row < N) and (0 <= s_col < N):

                        # If square is a snake or ladder store the destination
                        if board[s_row][s_col] != -1:
                            # destination of snake/ladder
                            s = board[s_row][s_col]

                        if s not in visited:
                            queue.append((s, moves+1))
                            visited.add(s)

        # If while loop ends, end of board was never reached
        return -1

    # DIJKSTRA-BASED APPROACH
    def solveWithDijkstra(board: list[list[int]]) -> int:
        N = len(board)
        if N == 2:
            return 1     # special case, a 2x2 board can be won with a roll of 4

        lboard = [0, ]    # linear board, 1-based index
        count = 0

        # Convert the 2d board into a 1d array
        for r in range(N-1, -1, -1):  # loop through all rows, from last to first
            count += 1

            if count % 2 == 0:  # even rows are read backwards
                row = board[r][::-1]
            else:
                row = board[r]

            # Append the row to our linear board
            lboard.extend(row)

        costs = defaultdict(int)        # 0 for missing keys
        q = list()
        heapq.heappush(q, (0, 1))        # tuples: (cost, squareNum)

        # We obtain all shortest paths to all squares,
        # then return the cost of reaching the last square.
        while q:
            # pops from min heap (closest or least-cost square)
            moves, squareNum = heapq.heappop(q)

            # calculate the available squares available for a die roll at this square
            dice = min(N*N-squareNum, 6)

            # For every possible dice roll
            for i in range(1, dice+1):
                s = squareNum + i          # landing square

                # If landing square is a snake we update `s` to the destination square
                if lboard[s] != -1:
                    s = lboard[s]

                # Relaxation: If we already explored s and have a better cost, update it
                if s in costs:
                    if (moves + 1) < costs[s]:
                        costs[s] = moves + 1

                        # Reinsert this square and path cost to the min heap
                        q.remove(s)
                        heapq.heapify(q)
                        heapq.heappush(q, (costs[s], s))

                # If its the first time visiting this square, set the current path cost
                else:
                    costs[s] = moves + 1
                    heapq.heappush(q, (costs[s], s))

        if not costs[N*N]:      # if value is 0 (default), no path exists
            return -1
        return costs[N*N]
