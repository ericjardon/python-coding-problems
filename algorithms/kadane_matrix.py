def maxSubmatrix(matrix):
    # Generate all possible submatrices of fixed matrix
    # pick the one with largest sum
    ans = 0

    rows = len(matrix)
    cols = len(matrix[0])

    # For every possible starting row
    for start_row in range(rows):
        # For every possible starting col
        for start_col in range(cols):
            # For every possible ending row
            for end_row in range(start_row, rows):
                for end_col in range(start_col, cols):

                    # make the sum
                    submatrix = 0
                    for i in range(start_row, end_row+1):
                        col = []
                        for j in range(start_col, end_col+1):
                            col.append(matrix[i][j])
                            submatrix += matrix[i][j]
                    ans = max(ans, submatrix)


    print(ans)


matrix = [[0, -2, -7, 0],
          [9, 2, -6, 2],
          [-4, 1, -4, 1],
          [-1, 8, 0, -2]]

maxSubmatrix(matrix)

# O(N^6) Time;  O(1) Space
def kadane(arr):
    '''Returns the largest sum of contiguous 1D subarray,
    in an efficient way. Works for arrays with negative ints'''

    # Traverse once. 
    # Accumulate in a contiguous sum but restart if it becomes negative.
    # Keep track of the globally maximum sum an update when necessary
    n = len(arr)
    global_max = float('-inf')
    current_contiguous = 0

    for i in range(n):
        current_contiguous += arr[i]
        if global_max < current_contiguous:
            global_max = current_contiguous
        if current_contiguous < 0:
            # We cannot do worse than 0. Slice subarray here.
            current_contiguous = 0
    
    return global_max

    
# O(N^3) Time, O(N^2)
def kadaneMatrix(matrix):
    # For every possible starting and ending column
    # Sum every row and add the sum into an array.
    # Apply Kadane to this array of row sums.
    # Keep track of global max, update when necessary
    ### NOTE: the row sum from start_col:end_col can be calculated in constant time 
    ### if we create an auxiliary matrix with the prefix sum  of each row.
    n = len(matrix)
    m = len(matrix[0])
    curr = 0
    maxSum = float('-inf')
    prefixSumRows = [[0 for _ in range(m)] for _ in range(n)] # will store row-wise prefix sum arrays 

    for r in range(n):
        for c in range(m):
            if c==0:
                prefixSumRows[r][c] = matrix[r][c]
            else:
                prefixSumRows[r][c] = prefixSumRows[r][c-1] + matrix[r][c]

    # For every possible vertical slice start_col:end_col
    for start_col in range(m):
        for end_col in range(start_col, m):
            aux = [] # stores sums of every row within start:end
            for r in range(n):
                if start_col==0:
                    row_sum = prefixSumRows[r][end_col]
                else:
                    row_sum = prefixSumRows[r][end_col] - prefixSumRows[r][start_col-1]
                
                aux.append(row_sum)

            submatrix = kadane(aux) # get max sum of possible row sums
            maxSum = max(maxSum, submatrix)

    print(maxSum)

print("\n Kadane Submatrix Sum")
kadaneMatrix(matrix)


def seansGame(squareMatrix):
    N2 = len(squareMatrix)
    n = N2//2

    pass
