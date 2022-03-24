#!/bin/python3
"""
HackerRank - Day 09 - Recursion
"""

import os
import sys


def factorial(number: int) -> int:
    """Recursive factorial function."""
    retval: int

    if number > 1:
        retval = number * factorial(number - 1)
    else:
        retval = number

    return retval


if __name__ == "__main__":
    try:
        fptr = open(os.environ["OUTPUT_PATH"], "w", encoding="utf8")
    except KeyError:
        fptr = sys.stdout

    with fptr:
        num: int = int(input().strip())

        result = factorial(num)

        fptr.write(str(result) + "\n")

        fptr.close()
