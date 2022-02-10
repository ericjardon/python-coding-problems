# UNSOLVED

'''
There is an infinite number of 4 types of lego blocks of 
sizes d*h*w.

1,1,1
1,1,2
1,1,3
1,1,4

You want to build a wall that is n high(h) and m wide(w).
a. Should not have any holes
b. There CANNOT be a straight vertical line across _all_ rows of bricks
c. Bricks must be laid horizontally (?)

Return the number of ways that the wall can be built.
----
NOTES
Let d be the z axis, h be the y axis, w be the x axis.
Height is always upright.

Notice how both depth and height are CONSTANT. We can dismiss depth
as bricks can only be laid in facing a single direction.
In the test cases, we are not told whether we can rotate bricks 
along the vertical axis.

We can compute the number of possible ways to arrange bricks along a row,
and raise this number to the nth power, but we must account for
permutations that have a single straight line across all rows.
'''


# For every level of the n levels of bricks;
# comput the number of unique permutations of bricks (4,3,2,1)
# and the answer is the product of permutations of every level.
# CAVEAT: we're not accounting for single-vertical line bricks.

def print_ways(width, used):
    '''Returns the number of ways to
        fill a space of width using bricks 1,2,3,4'''
    if width<0:
        return
    if width ==0:
        print(used)
    
    for brick in range(1, min(5, width+1)):
        print_ways(width-brick, used + [brick])


def count_ways(width):
    '''Returns the number of ways to
        fill a space of width using bricks 1,2,3,4'''
    if width<0:
        return
    if width ==0:
        return 1
    
    ans = 0
    for brick in range(1, min(5, width+1)):
        ans += count_ways(width-brick)
    
    return ans

def count_ways_memo(width, memo):
    '''Memoized count_ways'''
    if memo is None:
        memo = {}
    
    if width not in memo:
        if width<0:
            return
        if width ==0:
            return 1
        
        ans = 0
        for brick in range(1, min(5, width+1)):
            ans += count_ways_memo(width-brick, memo)

        memo[width] = ans
    
    return memo[width]

def invalid_ways(n, m, memo):
    # Logic is not right. permutations may be repeated.
    invalid_ways = 0
    for split_i in range(1, m):
        invalid_ways += count_ways_memo(split_i, memo) * count_ways_memo(m-split_i, memo)
    
    return invalid_ways ** n  # is the correct ans really powered to n?

def legoBlocks(n, m):
    print(n, m)
    memo = {}
    row_ways = count_ways_memo(m, memo)
    print("\tways per row", row_ways)
    total_invalid_ways = invalid_ways(n, m, memo)
    print("\tinvalid ways", total_invalid_ways)

    total_row_ways = row_ways**n
    print("\ttotal row ways", total_row_ways)
    return total_row_ways - total_invalid_ways



if __name__=="__main__":
    # t = int(input().strip())

    # for t_itr in range(t):
    #     first_multiple_input = input().rstrip().split()

    #     n = int(first_multiple_input[0])

    #     m = int(first_multiple_input[1])

    #     result = legoBlocks(n, m)
    #     print(result)
    print(legoBlocks(2, 2))
    print(legoBlocks(3,2))
    print(legoBlocks(2,3))
    print(legoBlocks(4,4))