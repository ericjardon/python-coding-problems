#  Just discard everything except every  number in the list,
# for some k>=1. Now, you just have to implement the idea, and your company will surely be very successful!


n, k = [int(x) for x in input().split()]
nums = input().split()

if n > 0:
    # print if index % k
    bound = len(nums) - 1
    for i in range(len(nums)):
        if (i+1) % k == 0:
            print(nums[i], end=' ' if i < bound else '')
