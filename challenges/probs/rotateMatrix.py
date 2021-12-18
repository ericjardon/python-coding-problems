'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

'''
from typing import List
from math import ceil
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # start from the top. for every index in the top, we place it on the same position 
        # in next perpendicular side e..g right side.
        # we take the old value, place the new one, and the old value should be placed next
        # once we do all for sides, reaching back to the top, we move to the next position i in the side. 
        def getAnalogousCorners(i,j,n):
                    '''Returns coordinates corresponding to j in every side of matrix'''
                    opposite = (n-i-1, n-j-1)
                    right = (j, n-i-1)
                    left = (n-j-1, i)
                    return [right, opposite, left, (i,j)]

        n = len(matrix) # n x n

        # For every layer in the matrix, outside in
        for layer in range(ceil(n/2)):  # square anchored at layer,layer
            for pos in range(layer, n-layer-1):
                val = matrix[layer][pos]
                print("Start:", layer, pos, f"({val})")
                for cell in getAnalogousCorners(layer, pos, n):
                    row, col = cell
                    print(f"Move {val} to {(row,col)}")
                    temp = matrix[row][col]
                    matrix[row][col] = val
                    val = temp
                print("----")
                for r in matrix:
                    print(r)
                print("----")
            
            

        print("Final matrix:")
        for r in matrix:
            print(r)
        print("----")

matrix = [
    [1,2,3],
    [8,0,4],
    [7,6,5]
]


matrix = [[1]]

matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
matrix = [[1,2],[3,4]]

Solution().rotate(matrix)                

print("....")
for r in matrix:
    print(r)

## answer is correct