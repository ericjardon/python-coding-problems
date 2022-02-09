'''
Princess Peach is trapped in one of the four corners of a square grid. 
You are in the center of the grid and can move one step at a time in any of the four directions. 


The first line contains an odd integer N (3 <= N < 100) denoting the size of the grid. This is followed by an NxN grid. Each cell is denoted by '-' (ascii value: 45). The bot position is denoted by 'm' and the princess position is denoted by 'p'.
Grid is indexed using Matrix Convention

Expected Output:
Print out the moves you will take to rescue the princess in one go. 
The moves must be separated by '\n', a newline. 
The valid moves are LEFT or RIGHT or UP or DOWN.
'''

#!/usr/bin/python

class Bot:
    # DIRECTIONS = {
    #     'UP': (-1, 0),
    #     'DOWN': (1, 0),
    #     'LEFT': (0, -1),
    #     'RIGHT': (0, 1)
    # }

    def __init__(self, i, j):
        self.i = i
        self.j = j


def displayPathtoPrincess(n, grid):
    # Get position of Mario and Princess
    mario = None
    peach = None
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 'm':
                mario = Bot(i, j)
            if grid[i][j] == 'p':
                peach = Bot(i, j)
    
    if not mario or not peach: return

    dist_i = peach.i - mario.i
    if dist_i > 0: # peach is below
        move_i = 'DOWN'
    else:
        move_i = 'UP'
    
    dist_j = peach.j - mario.j
    if dist_j > 0: # peach is to the right
        move_j = 'RIGHT'
    else:
        move_j = 'LEFT'
    
    for i in range(abs(dist_i)):
        print(move_i)
    for j in range(abs(dist_j)):
        print(move_j)
    
    return

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)