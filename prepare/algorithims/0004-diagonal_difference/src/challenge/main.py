#!/usr/bin/env python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr: List[List[int]]) -> int:

    total1: int = 0
    total2: int = 0
    diff: int

    for index1, index2 in zip(range(0, len(arr)), range(0, len(arr), 1)):
        total1 += arr[index1][index2]

    for index1, index2 in zip(range(0, len(arr)), range(len(arr) - 1, -1, -1)):
        total2 += arr[index1][index2]

    diff = abs(total1 - total2)

    return diff


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
