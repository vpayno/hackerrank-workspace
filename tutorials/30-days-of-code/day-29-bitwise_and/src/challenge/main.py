#!/usr/bin/env python3

import os


def bitwiseAnd(N: int, K: int) -> int:

    maximum: int = 0

    i: int
    j: int
    h: int

    for i in range(1, N + 1):

        for j in range(1, i):

            h = i & j

            if maximum < h < K:
                maximum = h

            if maximum == K - 1:
                return maximum

    return maximum


if __name__ == "__main__":

    count: int
    lim: int

    with open(os.environ["OUTPUT_PATH"], "w") as fptr:

        q: int = int(input().strip())
        res: int

        for _ in range(q):
            count, lim = [int(num) for num in input().strip().split()]
            # first_multiple_input = input().strip().split()
            # count = int(first_multiple_input[0])
            # lim = int(first_multiple_input[1])

            res = bitwiseAnd(count, lim)

            fptr.write(f"{res}\n")
