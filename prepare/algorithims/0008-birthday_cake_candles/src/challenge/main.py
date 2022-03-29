#!/bin/python3

import math
import os
import random
import re
import sys
from typing import List


def birthdayCakeCandles(candles: List[int]) -> int:

    count: int = 0
    size: int = 0
    candle: int

    candles.sort()
    candles.reverse()

    for candle in candles:
        if size == 0:
            size = candle
        else:
            pass

        if size == candle:
            count += 1
        else:
            break

    return count


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
