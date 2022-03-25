#!/bin/python3

import math
import os
import random
import re
import sys


def solve(decimal: int):

    binary: bin = bin(decimal)
    char: str
    count: int = 0
    counts: set = set()

    for char in str(binary)[2:]:
        if char == "1":
            count += 1
        else:
            counts.add(count)
            count = 0

    counts.add(count)

    # print(binary)
    # print(counts)
    print(sorted(list(counts))[-1])


if __name__ == "__main__":
    n: int = int(input().strip())

    solve(n)
