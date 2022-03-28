#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#


def compareTriplets(a, b):
    score_alice: int = 0
    score_bob: int = 0

    for num1, num2 in zip(a, b):
        if num1 > num2:
            score_alice += 1
        elif num1 < num2:
            score_bob += 1
        else:
            pass

    return [score_alice, score_bob]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
