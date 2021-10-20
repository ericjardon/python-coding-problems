'''
Zigzag sequence is an array of distint integers such that
the first k elements in the sequence are in increasing order 
and the last k elements are in decreasing order, where 
k : (n+1)/2

Note: n is always odd

For every array in the input, print the elements of the 
_lexicogrgaphically smallest_ zigzag sequence.

'''
# You can only modify at most 3 lines
def buggy_zigzag(a, n):
    a.sort()  # sort distinct elements
    # Perform binary search
    print(a)
    mid = int((n + 1)/2) - 1  # middle index, careful to substract 1
    a[mid], a[n-1] = a[n-1], a[mid]  # insert largest element in the middle

    # reverse the half after mid, leave last element untouched as it is smallest from the group
    st = mid + 1
    ed = n - 2
    while(st <= ed):
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1 

    # Print elements of result
    for i in range (n):
        if i == n-1:
            print(a[i])
        else:
            print(a[i], end = ' ')
    return

test_cases = int(input())
for cs in range (test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    buggy_zigzag(a, n)