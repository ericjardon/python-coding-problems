"""
    Latin Squares and Matrix Traces.
Latin Square: An nxn matrix which has n different values, and none is repeated
                in  a row or column.
Trace: the sum of values of the diagonal of a matrix \

Natural Latin Square: a latin square whose values go from 1 to N

Problem) Given an integer matrix containing possible values 1:N,
  Compute its trace and return it, along with # of rows, # of cols with repeated nums
"""


def vestigium(matrix, N):
    # Compute trace
    k = 0
    for i in range(N):
        k += matrix[i][i]
    # Count rows and cols with repeated elems
    repRows = set()
    repCols = set()
    rowVals = {}    # key is digit, val is boolean 'seen'
    colVals = {}
    for idx in range(N):
        rowVals[idx] = set()    # digits seen in the row at idx
        colVals[idx] = set()    # digits seen in the column at idx

    for i in range(N):      # for every row
        for j in range(N):      # for every col
            val = matrix[i][j]
            if val in rowVals[i]:   # if the value is already present add the row to repeated rows
                repRows.add(i)
            else:
                rowVals[i].add(val) # if not, add the value to the visited digits in ith row
            if val in colVals[j]:
                repCols.add(j)
            else:
                colVals[j].add(val)

    return k, len(repRows), len(repCols)


if __name__ == "__main__":
    T = int(input())    # number of testcases
    for i in range(1,T+1):

        N = int(input())    # size of matrix
        matrix = []
        for _ in range(N):
            line = input().rstrip().split(" ")
            row = [int(x) for x in line]
            matrix.append(row)

        k, r, c = vestigium(matrix, N)

        print(f"Case#{i}:", str(k), str(r), str(c))
### STATUS: ACCEPTED