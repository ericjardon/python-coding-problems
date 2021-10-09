'''
Given a 2d array representing a board with coins '1' or nothing '0',
calculate the maximum value in coins you can get only by moving right or down.

Note that in any greedy scenario the coin collector would end up in the bottom-right corner.
Hence the bottom right corner is our tile to stop.
'''

# Brute Force approach
def collect_coins(board, M, N, i=0, j=0):
        
    if i == M-1 and j == N-1:
        return board[i][j]

    down = 0
    right = 0
    if i < M-1:
        # We can move down
        down = collect_coins(board, M, N, i+1, j) + board[i][j]
    if j < N-1:
        # We can move right
        right = collect_coins(board, M, N, i, j+1) + board[i][j]

    return max(down, right)


def collect_coins_tab(board, M, N):
    table = [[0 for _ in range(N+1)] for _ in range(M+1)]

    # Build the answer bottom up
    # Our table structure is 1-indexed
    for i in range(1, M+1):
        for j in range(1, N+1):
            # table[i][j] holds the max value obtained at i-1,j-1, 
            # compare coming from either up or left
            from_left = table[i][j-1]
            from_up = table[i-1][j]

            table[i][j] = max(from_left, from_up) + board[i-1][j-1]
    
    return table[M][N]


def collect_coins_inplace(board):
    M = len(board)
    N = len(board[0])

    dp = [[0 for _ in range(N)] for _ in range(M)]
    dp[0][0] = board[0][0]

    for col in range(1, N):
        # Top row can only come from the right
        dp[0][col] = dp[0][col-1] + board[0][col]
    
    for row in range(1, M):
        dp[row][0] = dp[row-1][0] + board[row][0]

        for col in range(1, N):
            left = dp[row][col-1]
            up = dp[row-1][col]

            dp[row][col] = max(left, up) + board[row][col]
    
    return dp[M-1][N-1]
    


board = [[0,0,0,0,1,0],
         [0,1,0,1,0,0],
         [0,0,0,1,0,1],
         [0,0,1,0,0,1]]
rows = len(board)
cols = len(board[0])
print("BF:", collect_coins(board, M=rows, N=cols))
print("Tabulation:", collect_coins_tab(board, M=rows, N=cols))
print("Another approach", collect_coins_inplace(board))