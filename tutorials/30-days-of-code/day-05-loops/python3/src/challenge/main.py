#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 05 - Loops

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""


class Challenge:
    """
    Day 05 - Loops
    """

    def __init__(self, number: int = 0) -> None:

        self.number: int = number

    def input_number(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        self.number = int(input().strip())

    def solve(self) -> None:
        """
        Calculates multiples of n.
        """

        i: int
        result: int

        for i in range(1, 11):
            result = self.number * i
            print(f"{self.number} * {i} = {result}")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_number()

        self.solve()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
