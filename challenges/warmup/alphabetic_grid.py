'''
Given a square grid of characters in the range ascii[a-z], rearrange elements of each row alphabetically, 
ascending. Determine if the columns are also in ascending alphabetical order, top to bottom. 
Return YES if they are or NO if they are not.
'''

def gridChallenge(grid):


    for i, row in enumerate(grid):
        grid[i] = sorted(row)
    
    for j in range(len(grid[0])):
        col = [grid[i][j] for i in range(len(grid))]

        if col != sorted(col):
            print("NO")
    
    print("YES")


grid = [
"abcde",
"fghij",
"klmno",
"pqrst",
"uvwxy",
]
grid = ['ebacd', 'fghij', 'olmkn', 'trpqs', 'xywuv']
gridChallenge(grid)