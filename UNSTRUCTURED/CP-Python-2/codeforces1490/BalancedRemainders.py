# An array of balanced remainders of 3 is one array such that
# the sets of elements c_i corresponding to remainer i of 0, 1 and 2
# have the same number of elems.
# For example, [0,1,2,3,4,5] is balanced, as there are 2 for each set c_i

"""Given a length N divisible by 3 and an array of ints, find the minimumb
    number of increments you must do to any element in order to get a
    balanced remainders array. """

    # preprocess the array to count the number of elements of each set ci.
    # incrementing an element will remove an element from its set and add it to another set
    # c0 -> c1, c1->c2, c2->c0

    #The problem is reduced to having three numbers c1, c2, c3 and finding the number of moves
    # (where a move is increase one, decrease another) for them to be equal.

def balancedRemainders(n, A):
    c = [0,0,0]
    for x in A:
        c[x%3] += 1
    #print("initial:", c)
    return findMoves(c)

def findMoves(c):
    moves = 0
    while(c[0] != c[1] or c[1] != c[2]):
        i = biggest(c)      # index of biggest set
        c[i] -= 1
        c[(i+1)%3] += 1
        #print(c)
        moves += 1
    #print("Result: ", end='')
    return moves

def biggest(c):
    if c[0] >= c[1]:
        if c[0] >= c[2]:
            # reduce c0, augment c1
            return 0
        else:
            # reduce c2, augment c0
            return 2
    elif c[1] >= c[2]:
        # reduce c1 and augment c2
        return 1
    else:
        # reduce c2 and augment c0
        return 2

if __name__ == '__main__':
    for t in range(int(input())):
        #print("Testcase", t+1)
        n = int(input())
        A = [int(x) for x in input().split()]
        print(balancedRemainders(n, A))