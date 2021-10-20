def prefixSum(arr):
    ps = arr.copy()
    
    for i in range(1, len(arr)):
        ps[i] += ps[i-1]
    
    return ps