#!/usr/bin/env python3

import collections
import math
import os
import random
import re
import sys
from typing import List, OrderedDict

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr: List[int]):
    counter: OrderedDict[str, int] = collections.OrderedDict({
        "positive": 0,
        "negative": 0,
        "zero": 0,
    })

    size: float = len(arr)
    num: int

    for num in arr:
        if num > 0:
            counter["positive"] += 1
        elif num < 0:
            counter["negative"] += 1
        else:
            counter["zero"] += 1

    result: List[float] = []
    value: float

    for _, value in counter.items():
        result.append(value / size)

    for value in result:
        print(f"{value:.6f}")


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
