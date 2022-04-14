#!/usr/bin/env python3

import os
import sys
import time
from typing import Set

import big_o


def bitwiseAnd(N: int, K: int) -> int:

    results: Set = set()
    result: int

    i: int
    j: int

    for i in range(1, K):
        for j in range(i + 1, N + 1):
            result = i & j
            if result < K:
                results.add(result)

    return max(results)


def bitwise_and_bench(lines):
    for line in lines:
        count, lim = [int(num) for num in line.strip().split()]
        bitwiseAnd(count, lim)


if __name__ == "__main__":
    with open("./test-long-inputs.txt", "r") as data:
        lines = data.readlines()[1:]

    def samples(line):
        return [line for line in lines]

    best, others = big_o.big_o(bitwise_and_bench, samples, n_measures=20)

    print(f"Best {best}")
    print()
    for class_, residuals in others.items():
        print(class_)

    sys.exit(0)

    time_start = time.time()

    with open(os.environ["OUTPUT_PATH"], "w") as fptr:

        t = int(input().strip())

        for _ in range(t):

            # count, lim = [int(num) for num in input().strip().split()]

            first_multiple_input = input().rstrip().split()

            count = int(first_multiple_input[0])

            lim = int(first_multiple_input[1])

            res = bitwiseAnd(count, lim)

            fptr.write(f"{res}\n")

    time_end = time.time()

    print(f"total time: {time_end - time_start:.2f}s")
