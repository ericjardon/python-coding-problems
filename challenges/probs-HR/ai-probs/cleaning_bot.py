#!/usr/bin/python

# Head ends here

DIRECTIONS = [(0,1), (1,0), (-1, 0), (0, -1)]

def validPos(i, j):
    return (0 <= i < 5) and (0 <= j < 5)

def bfs(board, boti, botj):
    from collections import deque
    
    q = deque()
    visited = set()
    q.append((boti, botj))
    visited.add((boti, botj))
    
    while q:
        i, j = q.popleft()
        if board[i][j] == 'd': return i, j
        
        for di, dj in DIRECTIONS:
            next_i = i + di
            next_j = j + dj
            
            if validPos(next_i, next_j) and (next_i, next_j) not in visited:
                q.append((next_i, next_j))
                visited.add((next_i, next_j))
    # No cells to clean
    return None
    
def next_move(posr, posc, board):
    if board[posr][posc] == 'd':
        return 'CLEAN'
    
    target_i, target_j = bfs(board, posr, posc)
    
    if target_i > posr:
        return 'DOWN'
    if target_i < posr:
        return 'UP'
    if target_j > posc:
        return 'RIGHT'
    if target_j < posc:
        return 'LEFT'
    return ' CLEAN'

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    print(next_move(pos[0], pos[1], board))