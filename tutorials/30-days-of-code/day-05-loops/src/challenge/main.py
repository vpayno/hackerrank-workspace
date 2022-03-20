#!/bin/python3


def solve(n: int):
    r: int

    for i in range(1, 11):
        r = n * i
        print(f"{n} x {i} = {r}")


if __name__ == "__main__":
    n = int(input().strip())

    solve(n)
