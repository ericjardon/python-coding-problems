'''
Given a SORTED array of integers find the first and the last occurrences of
a given target number. 
----
Linear scanning is impractical when array size is in the order of millions.
Since the array is sorted, we can do binary search instead: one time for the first
occurrence and another for the last.
'''


def firstAndLast(array: list[int], target: int):
    lo = 0
    hi = len(array) - 1

    # Find first occurrence of target.
    while lo <= hi:  # repeat as long as lower pointer is leq to higher pointer
        mid = lo + (hi-lo)//2  # rounded down

        if array[mid] >= target:
            hi = mid - 1  # continue decreasing hi until it is one position before first
        else:
            lo = mid + 1

    first = lo
    print("first", first)
    hi = len(array) - 1
    while lo <= hi:
        mid = lo + (hi-lo)//2  # rounded down
        if array[mid] <= target:
            lo = mid + 1  # continue increasing lo until it is one position after last
        else:
            hi = mid - 1

    last = hi
    print("last", last)
    if first > last:
        return (-1, -1)
    return (first, last)

# EXPLANATION: Target element can be repeated. We can consider the target as
# a subarray with all consecutive occurrences of target. Binary search could land on
# any of these elements. Once mid hits the target, we continue decreasing
# hi pointer to the left so mid is moving left too. Because hi is moved left as long as mid
# lands in target subarray, hi will at most move to one position less than first occurrence.
# Once mid lands to the left of target subarray (and mid is always less or equal to hi),
# lo starts to be pushed up until it surpasses hi. Lo will then hold the first occurrence.
# Even if the first occurrence is at index 0 (lo), hi eventually becomes -1 and
# lo is by default more than hi, so we stop without index position errors.
# When the loop finishes, the first occurrence is always found in lo.

# The same logic applies to the last occurrence, only we continue increasing lo instead of decreasing hi.


if __name__ == "__main__":

    arrays = {
        # target 6: 15 and 22
        0: [1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 4, 4, 4, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 7, 7, 8, 9, 9, 9],
        1: [1, 2, 2, 3],  # target 1: 0 and 0
        2: [1, 2, 3, 4, 5, 6, 7, 8, 78],  # target 78: 8 and 8
        3: [1, 1, 6, 10],  # target 1: 0 and 1
        4: [1, 1, 1],
        5: [1, 1, 2, 2, 4, 4]
    }
    targets = [6, 1, 78, 1, -2, 5]
    answers = [(15, 22), (0, 0), (8, 8), (0, 1), (-1, -1), (-1, -1)]

    testcases = len(targets)

    # Testcases
    for i in range(testcases):
        a = arrays[i]
        k = targets[i]
        ans = firstAndLast(a, k)
        print(ans)
        if ans == answers[i]:
            print(f"Test {i+1} passed")
        else:
            print(f"Test {i+1} failed. expected {answers[i]}")
