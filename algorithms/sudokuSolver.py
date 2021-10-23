'''
Backtracking solution to a
Sudoku Board.

Given a grid of characters representing a 9x9 sudoku board
Return the same board filled out completely, such that there
are no repeating digits in row, column or subsquare (3x3).

------- DESCRIPTION
We explore possible solutions for the board while backtracking.

1. Explore the board and register the occupied and empty squares.
1.1. Use 3 data structures for storing the unavailable digits for 
    every column, every row and every subsquare.
1.2. Use a fourth array to store the empty cells to fill.

2. For every empty cell, identify the possible values for that cell 
    according to the unavailable values you registered.
3. Next, perform DFS, traversing empty cells one by one, sorted from 
   least to most number of available values.
3.1 On every recursion loop through the possible values. 
3.2 For every valid value placement, update the availability data structures and recurse
    again with the next empty cell.
3.3 When we stop at a valid solution i.e. the loop runs out, return False (no answer).
3.4 If DFS traversed all empty cells array succesfully, return True

The backtracking condition is given if by the return value of 
 solvable(board, emptycells, nextCell)
after having placed a value in the current cell.
If True, we found an answer with our current decision.
If false, we must revert our placement and pick the next possible value for the cell.

'''

# We can keep track of a cell's possible values and subsquare number.
# We can optimize two constraints:
# - We only consider the values available for a cell due to its position
# - We start filling out the most restricted cells; those with the least
#   number of values available to them
from typing import List, Type

class SudokuSolver:
    
    # Value availability: [[isAvailable boolean for values 0..9]...]
    rowVals = None
    colVals = None
    squareVals = None


    def solveSudoku(self, board):
        """
        Modifies the board in-place
        Assumes provided board is valid
        """
        class Cell:
            '''
            Utility class to keep track of the subsquare a sudoku cell belongs to,
            and to track the possible values for that cell.
            This list of possible values depends on the position of the cell in board.
            '''
            def __init__(self, row, col):
                self.row = row
                self.col = col
                self.square = (row//3)*3 + (col//3) # indexed 0..8
                self.possibleValues = []


        rowVals = [[True for _ in range(10)] for _ in range(9)]
        colVals = [[True for _ in range(10)] for _ in range(9)]
        squareVals = [[True for _ in range(10)] for _ in range(9)]

        def getEmptyCells(board):
            emptyCells = []

            for i in range(9):
                for j in range(9):
                    subSquare = (i//3)*3 + (j//3)
                    if board[i][j] == '.':  # if cell is not empty
                        emptyCells.append(Cell(i,j))
                    else:
                        val = int(board[i][j])  # cast str to int
                        rowVals[i][val] = False
                        colVals[j][val] = False
                        squareVals[subSquare][val] = False
            
            return emptyCells

        def updateAvailableValues(cell: Cell):
            """
            Called at the start of procedure to initialize candidate
            values for an empty cell
            """
            for val in [1,2,3,4,5,6,7,8,9]:
                # If value is available, append it to possible values
                if rowVals[cell.row][val] and colVals[cell.col][val] \
                    and squareVals[cell.square][val]:
                    cell.possibleValues.append(val)
        
        def solved(cells, board, i):
            """
            Recursive function that uses backtracking to find a solution to
            a given sudoku board. It explore combinations in place and reverts
            the placement made if no solution is possible in that path.
            cells -> an array of Cells to fill, sorted by num of available values
            board -> character grid with digit or '.' if empty
            i -> index of current Cell to fill
            """
            if i == len(cells):
                # We succesfully filled out every Cell
                return True
            cell = cells[i]

            for val in cell.possibleValues:
                if rowVals[cell.row][val] and colVals[cell.col][val] \
                    and squareVals[cell.square][val]:
                    board[cell.row][cell.col] = str(val)  # cast int to str
                    rowVals[cell.row][val] = False
                    colVals[cell.col][val] = False
                    squareVals[cell.square][val] = False

                    if solved(cells, board, i+1):
                        return True
                    
                    # If not solved with this placement, revert decision and try another one
                    board[cell.row][cell.col] = '.'
                    rowVals[cell.row][val] = True
                    colVals[cell.col][val] = True
                    squareVals[cell.square][val] = True

            return False # no possible placement can be made so current board is an invalid answer

        emptyCells = getEmptyCells(board)
        if len(emptyCells) == 0: return

        print("Number of empty cells", len(emptyCells))

        for cell in emptyCells:
            updateAvailableValues(cell)
        
        emptyCells.sort(key=lambda c: len(c.possibleValues))

        # Solves in-place. Input board is guaranteed to have unique solution
        solved(emptyCells, board, 0)


def printBoard(board):
    for row in board:
        print(row)
        print()

if __name__=="__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    printBoard(board)
    SudokuSolver().solveSudoku(board)

    printBoard(board)
