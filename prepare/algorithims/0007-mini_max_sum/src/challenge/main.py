#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    arr.sort()

    slice_size = max(len(arr) - 1, 0)

    slice_min: List[int] = arr[0:slice_size]
    slice_max: List[int] = arr[-slice_size:]

    sum_min: int = sum(slice_min)
    sum_max: int = sum(slice_max)

    results = (sum_min, sum_max)

    print(" ".join([str(number) for number in results]))


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
