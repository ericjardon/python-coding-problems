#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):

    n = len(arr)
    plus = 0
    minus = 0
    zero = 0

    for num in arr:
        if num > 0:
            plus += 1
        elif num < 0:
            minus += 1
        else:
            zero += 1
    
    positives = plus*1.0 / n
    negatives = minus*1.0 / n
    zeroes = zero*1.0 / n

    print("{:.6f}".format(positives))
    print("{:.6f}".format(negatives))
    print("{:.6f}".format(zeroes))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
