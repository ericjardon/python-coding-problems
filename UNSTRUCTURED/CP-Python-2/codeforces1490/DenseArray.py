# An array of ints is dense if for any two consecutive elements,
# the bigger of the two is not more than twice bigger than the smaller.
# max(a,b)/min(a,b) <=2 for any a,b adjacent.

"""Given an arr A of N ints (dense or not). What is the minimum amount of
    numbers you need to add to make it a Dense Arrray?
    Note: numbers can be inserted anywhere in the array. """

# 1. find pairs consecutive nums which do not satisfy the dense constraint by traversing 2 by 2.
# 2. Once a pair is found, find the avg of the two and insert it. Check if satisfies with previous.
# if it doesnt, insert again, and so on. If it does, move to the next pair.

def validPair(a, b):
    return (max(a,b)/min(a,b)) <=2

def denseArray(A, n):
    ct = 0
    for i in range(n-1):
        a = A[i]
        b = A[i+1]
        while (not validPair(a,b)):
            ct += 1
            insert = 2*min(a,b)
            if a<b:   # compare insert with b
                a = insert
            else:               # compare insert with a
                b = insert
        # count insertions bewteen a and b, then move to next i element

    return ct


for t in range(int(input())):   # for every test case
    n = int(input())
    A = [int(x) for x in input().split()]
    count = denseArray(A, n)
    print(count)
