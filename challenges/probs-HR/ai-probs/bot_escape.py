'''https://www.hackerrank.com/challenges/maze-escape?isFullScreen=true&hr_b=1


The input map (3x3) changes orientation according to the direction the bot is facing
The bot always faces whichever direction it moved last

Heuristic: The entire maze is enclosed; exit is not in a corner; 
        we can circle around walls giving preference to the right
        Circling around walls happen when there is a wall to the bot's
        behind-right or behind-left, the corresponding wall side is clear,
        and the behind side is clear.
'''

def visibleExit(board):
    # Return the coordinates of exit if found, None otherwise
    d = [-1, 0, 1]
    for di in d:
        for dj in d:
            if board[1 + di][1 + dj] == 'e':
                return (1 + di, 1 + dj)
    return None

def nextMove(board):
    # board is always 3x3, with bot at center
    
    # Look for e
    exit = visibleExit(board)
    if exit:  # exit is within 1 or 2 steps away
        ei, ej = exit
        
        if ei > 1: # exit is below
            if ej > 1:
                return 'RIGHT' if board[1][ej] != '#' else 'DOWN'
            if ej < 1:
                return 'LEFT' if board[1][ej] != '#' else 'DOWN'
            else:
                return 'DOWN'           
        else:       # exit is above
            if ej > 1:
                return 'RIGHT' if board[1][ej] != '#' else 'UP'
            if ej < 1:
                return 'LEFT' if board[1][ej] != '#' else 'UP'
            else:
                return 'UP'
    else:  # exit is not visible, probe around
        
        # Circle around walls
        if board[2][2] == '#' and board[1][2]!='#' and board[1][2] != '#':
            return 'RIGHT'
        if board[2][0] == '#' and board[1][2]!='#' and board[1][0] != '#':
            return 'LEFT'
        
        # Move forward whenever possible, else move right, else left, go back if no directions available
        if board[0][1] != '#':
            return 'UP'
        if board[1][2] != '#':
            return 'RIGHT'
        if board[1][0] != '#':
            return 'LEFT'
        return 'DOWN'
    
    

if __name__ == "__main__":
    id = int(input())
    board = [[ch for ch in input().strip()] for i in range(3)]
    print(nextMove(board))