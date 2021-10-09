
# Use accumulated sum (no need for prefix sum array)

def hasZeroSumArray(arr):
    # Either a prefix sum is repeated, (not too obvious!) 
    # or prefix sum is 0, means there is a subarray summing 0
    n = len(arr)
    sum_to_i = 0
    seen = set()
    for num in arr:
        sum_to_i += num
        if sum_to_i in seen or sum_to_i == 0:
            return True
        seen.add(sum_to_i)
    
    return False

