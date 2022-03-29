#!/bin/python3

import math
import os
import random
import re
import sys


def staircase(n):
    """
    Its base and height are both equal to . It is drawn using # symbols and spaces.
    The last line is not preceded by any spaces.
    """

    char = "#"

    for count in range(1, n + 1):
        step = char * count
        line = f"{step: >{n}}"
        print(line)


if __name__ == "__main__":
    n = int(input().strip())

    staircase(n)
