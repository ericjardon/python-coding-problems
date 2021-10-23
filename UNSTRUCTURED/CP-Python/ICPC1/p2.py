"""Detailed Sorting Machine"""

# you can only sort by pushing elements to the tail of the list.
#vals = [1, 3, 5, 7, 9]
valso = [1, 3, 4, 5, 2]
def sortByTail(vals):
    # what is the minimum number of times buttons shall be pressed
    # to have a completely sorted array?
    # it will be the number of elements larger than the original tail
    times = 0
    for i in range(len(vals)):
        if vals[i] > vals[-1]:
            times += 1

    print(times)

def main():
    N = int(input())
    vals = input().split(" ")
    nums = []
    for val in vals:
        nums.append(int(val))
    sortByTail(nums)

main()

#sortByTail(vals)
#sortByTail(vals2)