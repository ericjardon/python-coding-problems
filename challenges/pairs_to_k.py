
    

def pairsWithDifferenceK(k, arr):
    nums = set(arr)
    pairs = 0
    for n in arr:
        if n - k in nums:
            pairs += 1
    
    return pairs