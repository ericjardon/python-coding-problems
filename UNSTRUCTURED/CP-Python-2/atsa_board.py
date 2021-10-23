"""
 ATSA'S BOARD GAME
 A 'pairable' stones configuration is a placement of dark and white stones on a checkers board MxN such that
 for all 2x2 squares in the board, they contain 2 dark and 2 white.
 Are you be able to find how many distinct “pairable” stones configurations can be placed in a
 checkers board given its dimensions MxN?
"""

def pairableConfigurations(M: int, N: int) -> int:
    if M < 2 or N < 2:
        return 0

    count = 0
    board = [[None for _ in range(N)] for _ in range(M)]

    def countPairable(i: int, j: int, board: list[list[any]]) -> int:
        global count
        if i == M-2 and j == N-2:   # if we are in the last square we have finished filling
            count += 1
        else:           # check valid placements for current square, upperleft in i,j
            up_left = board[i][j]
            low_left = board[i][j+1]
            for up_right in [0,1]:
                for low_right in [0,1]:
                    if up_left + low_left + up_right + low_right == 2:
                        #
                        pass





    board = [[None for _ in range(N)] for _ in range(M)]
    # para cada par horizontal de celdas hay 4 opciones. 00, 01, 10 o 11.
    # para cada par horizontal su siguiente par forma un cuadrado.
    # para cada par horizontal debe cumplirse que tenga igual número de blancas y negras.
    # contamos 1 configuración cuando en nuestro arbol de exploración llegamos al par con i=M-2, j=N-2.
    # let 0 = light stone, 1 = dark stone
    pair_vals = [(0,0), (1,1), (1,0), (0,1)]      # a 2x2 square is valid when its sum is exactly 2 (2 blacks <-> 2 whites)
    # for every possible value of a pair
    return countPairable(0,0, board)


def main():
    for t in range(int(input())):
        M, N = [int(x) for x in input().split()]


if __name__ == '__main__':
    main()