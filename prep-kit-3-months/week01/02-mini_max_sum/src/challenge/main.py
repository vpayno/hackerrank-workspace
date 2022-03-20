#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List, Tuple

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr: List[int]):
    # Write your code here

    numbers: List[int] = sorted(arr)
    slice_size: int = len(numbers) - 1

    slice_min: List[int] = numbers[0:slice_size]
    slice_max: List[int] = numbers[-slice_size:]

    min: int = sum(slice_min)
    max: int = sum(slice_max)

    number: int
    results: Tuple[int] = (min, max)

    print(" ".join([str(number) for number in results]))


if __name__ == "__main__":

    arr: List[int] = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
