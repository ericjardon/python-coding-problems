# Get a function that finds all maximum intervals that are good sequences
# and call the sum subarray function for all of them 

# Answer complexity: traversal O(N), interval sum O(N) worst case -> O(N^2)

def appearances(i, N):
    return (N-i)*(i+1)

def sumOfSubarrays(A, i, j):
    # every element at position i appears a known number of times among the possible subarrays of a sequence len N
    # appearances(i) = seqsDoStartWithi(i) + seqsDontStartWithi(i)
    # appearances(i) = (number of positions including i to end) + (number of positions before i * number of positions including i to end)
    # appearances(i) = (N-i) + i*(N-i) = (N-i)(i+1)
    N = j - i + 1
    print("\tGood sequence length", N)
    if N == 1:
        print("result", A[i])
        return A[i]
    s = 0
    idx = 0
    for k in range(i, j+1):
        print(f"\t add {A[k]}*appearances({idx})")
        s += A[k] * appearances(idx, N)
        idx += 1
    print("result", s)
    return s

def sumOfAllGoodSequences(A):
    if not A or len(A) == 0:
        return 0
    if len(A) == 1:
        return A[0]
    result = 0
    st = 0
    while st < len(A):
        # Find maximum ending index which is good sequence
        ed = st
        while ed < len(A)-1 and A[ed+1] - A[ed] == 1:
            ed += 1
        
        print("Good sequence from", st, "to", ed)
        result += sumOfSubarrays(A, st, ed)
        # Move to next
        st += (ed - st + 1)
    
    return result


A = [1,2,3,2,2,5,6,7] 
# two increasing seqs: 123 and 567
# 1 + (1+2) + 2 + (2+3) + 3 + (1+2+3) = 6+6+3+5 = 20
# 5 + 6 + 7 + (5+6) + (6+7) + (5+6+7) = 18+18+11+13 = 36+24 = 60
# ans = 80 + singletons in the middle: 2, 2, = 84
print(sumOfAllGoodSequences(A))