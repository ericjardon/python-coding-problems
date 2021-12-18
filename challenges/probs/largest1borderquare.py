'''
Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, 
or 0 if such a subgrid doesn't exist in the grid.
'''
from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        # Preprocess to have two grids that tell us the consecutive ones to the right and down.
        # For every corner cell i,j that could increase our answer: check width and height. l=min(w,h), 
        # where w and h are consecutive 1s.  Then, check valid square: bottom and right sides should have at least l consecutive ones

        def maxconsecutive1s(si, sj, direction, grid):
            # direction is any of r(0,1) d(1,0),  and maybe u(-1,0), l(0,-1)
            ones = 1
            di, dj = direction
            i = si + di
            j = sj + dj
            while i<len(grid) and j<len(grid[0]) and grid[i][j] == 1:
                ones += 1
                i += di
                j += dj
            
            return ones
        
        def getAuxGrids(grid):
            # Create aux grids: aux[i][j] is num of consecutive 1s from i,j
            hor = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]
            ver = [[-1 for _ in range(len(grid[0]))] for _ in range(len(grid))]

            for row in range(len(grid)):
                j=0
                while j < len(grid[0]):  # traverse row horizontally
                    if grid[row][j]==0:  # skip zeroes
                        j += 1
                        continue
                    ones = maxconsecutive1s(row, j, (0,1), grid)  # compute max num of ones from current cell
                    hor[row][j] = ones
                    ones -= 1
                    j += 1

                    while j < len(grid[0]) and ones>0:
                        hor[row][j] = ones
                        ones -=1
                        j += 1

            print("Horizontal grid")
            for row in hor:
                print(row)
            print("-----")

            for col in range(len(grid[0])):
                i = 0
                while i < len(grid):
                    if grid[i][col]==0:
                        i += 1
                        continue
                    ones = maxconsecutive1s(i, col, (1,0), grid)
                    ver[i][col] = ones
                    ones -= 1
                    i += 1

                    while i < len(grid) and ones>0:
                        ver[i][col] = ones
                        ones -= 1
                        i += 1

            print("\nVertical grid")
            for row in ver:
                print(row)
            print("-----")

            return hor, ver

        def checkBorderSquare(si,sj,l,hor,ver):
            '''We know left and top sides are l. check if bottom and right have at least l consecutive squares'''
            return hor[si+l-1][sj] >= l and ver[si][sj+l-1] >= l


        hor, ver = getAuxGrids(grid)

        maxLen = 0 # global max square length
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # check if i,j forms a border square
                w = hor[i][j]
                h = ver[i][j]
                l_max = min(w,h) # max possible square length
                # check lengths from l to 1
                for l in range(l_max, 0, -1):
                    if l > maxLen:
                        print("New possible length", l, "at", i,j)
                        if checkBorderSquare(i,j,l,hor,ver):
                            print("bigger square", l*l)
                            maxLen = l
                        else:
                            print("candidate failed")
                    else:
                        break
        print("area of max square", maxLen*maxLen)          
        return maxLen*maxLen


# grid = [
#     [1,1,1,1,1],
#     [0,1,0,1,1],
#     [0,1,0,0,0],
#     [1,1,0,1,1],
#     [0,0,0,0,0]
# ]

# grid = [
#     [1,1,1],
#     [1,1,0],
#     [0,0,0],
# ]

# grid = [[0,0,0,1]]

grid = [
    [0,1,1,1,1,1,1,0],
    [1,1,1,1,1,1,1,1],
    [1,0,1,1,1,0,1,1],
    [1,1,1,1,0,1,1,1],
    [1,0,1,0,0,1,1,1],
    [0,1,1,1,1,0,1,1]
    ]

Solution().largest1BorderedSquare(grid)

