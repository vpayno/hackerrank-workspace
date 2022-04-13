#!/usr/bin/env python3

import os
from typing import Set


def bitwiseAnd(N: int, K: int) -> int:

    results: Set = set()
    result: int

    i: int
    j: int

    for i in range(1, N):
        for j in range(i + 1, N + 1):
            # print(f"{i} & {j} = {i & j}")
            results.add(i & j)

    for i in reversed(list(results)):
        if i < K:
            result = i
            break

    # print(f"result={result}")
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        count = int(first_multiple_input[0])

        lim = int(first_multiple_input[1])

        res = bitwiseAnd(count, lim)

        fptr.write(str(res) + "\n")

    fptr.close()
