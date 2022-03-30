#!/bin/python3

import math
import os
import random
import re
import sys
from pprint import pprint
from typing import List


def solve(numbers: List[int]):

    sums: set = set()
    total: int = 0
    rows: List[int] = []
    row_start: int = 0
    row_index: int = 0
    col_start: int = 0
    col_index: int = 0
    line_num: int = 0
    skip_mid_col: bool = False
    col_shift: int = 0
    hourglass_index: int = 0

    for col_start in range(0, 4):
        total = 0
        skip_mid_col = False
        print(f"col_start={col_start}")
        for row_start in [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]:

            for col_index in range(col_start, col_start + 3):
                if row_start > 3 or row_index > 4:
                    break

                print(f"skip_mid_col={skip_mid_col}")
                skip_mid_col = not skip_mid_col

                print(f"col_index={col_index}")

                row_index = row_start + 0
                print(f"\trow_index={row_index}={row_index - 0} + 0")
                total += numbers[row_index][col_index]
                print(f"\ttotal={total}+={numbers[row_index][col_index]}")

                row_index = row_start + 1
                print(f"\trow_index={row_index}={row_index - 1} + 1")
                if not skip_mid_col:
                    total += numbers[row_index][col_index]
                    print(f"\ttotal={total}+={numbers[row_index][col_index]}")

                row_index = row_start + 2
                print(f"\trow_index={row_index}={row_index - 2} + 2")
                total += numbers[row_index][col_index]
                print(f"\ttotal={total}+={numbers[row_index][col_index]}")

                print()

                hourglass_index == 1

            if hourglass_index > 2:
                hourglass_index = 0
                sums.add(total)
                print(f"Completed first hourglass. sum={total}")
                total = 0
            else:
                print("next column in hourglass...")

        col_start += 1

    pprint(sums)


if __name__ == "__main__":

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    pprint(arr)

    solve(arr)
