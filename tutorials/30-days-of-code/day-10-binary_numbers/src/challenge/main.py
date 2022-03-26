#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 10 - Binary Numbers

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import Optional

from rich.traceback import install

install()


class Challenge:
    """
    Main challenge class.
    """

    def __init__(self, number: Optional[int] = None):

        self.number: int = 0

        self.output: int = 0

        if number is not None:
            self.number = number
        else:
            self.numbers = 0

    def input_number(self):
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.number <= 0:
            self.number = max(int(input().strip()), 0)
        else:
            pass

    def solve(self):
        """Solves the challenge."""

        binary: str = bin(self.number)
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

        self.output = sorted(list(counts))[-1]

    def print_results(self):
        """Print the results of the challenge."""

        print(self.output)

    def main(self):
        """
        Challenge steps.
        """

        self.input_number()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
