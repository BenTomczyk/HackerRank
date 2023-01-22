#!/bin/python3

import math
import os
import random
import re
import sys
import bisect

#
# Complete the 'activityNotifications' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY expenditure
#  2. INTEGER d
#


def activityNotifications(expenditure, d):
    history = sorted(expenditure[:d])
    # If d is odd: median of history == history[a] == history[b]
    # If d is even: median of history == (history[a] + history[b]) / 2
    a = math.ceil((d-1)/2)
    b = math.floor((d-1)/2)
    count = 0
    for i in range(len(expenditure)-d):
        count += (history[a] + history[b] <= expenditure[i+d])
        # Update history while keeping it sorted.
        history.pop(bisect.bisect_left(history, expenditure[i]))
        bisect.insort(history, expenditure[i+d])
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
