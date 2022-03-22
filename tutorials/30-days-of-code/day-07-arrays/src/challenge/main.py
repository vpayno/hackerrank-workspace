#!/bin/python3

from typing import List


def solve(numbers: List[int]):
    print(" ".join([str(number) for number in reversed(numbers)]))


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    solve(arr)
