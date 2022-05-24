#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 09 - Recursion 3

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import os
import sys
from typing import Optional, TextIO

from rich.traceback import install

install()


class Challenge:
    """
    Day 07 - Arrays
    """

    def __init__(self, number: Optional[int] = None) -> None:

        self.number: int = 0

        self.output: int = 0

        if number is not None:
            self.number = number
        else:
            self.numbers = 0

    def input_number(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.number <= 0:
            self.number = max(int(input().strip()), 0)
        else:
            pass

    def factorial(self, number: int) -> int:
        """Recursive factorial function."""

        retval: int

        if number > 1:
            retval = number * self.factorial(number - 1)
        else:
            retval = number

        return retval

    def solve(self) -> None:
        """Solves the challenge."""

        self.output = self.factorial(self.number)

    def print_results(self) -> None:
        """Print the results of the challenge."""

        if "pytest" in sys.modules:

            print(self.output)

        else:

            fptr: TextIO

            try:
                fptr = open(os.environ["OUTPUT_PATH"], "w", encoding="utf8")
            except KeyError:
                fptr = sys.stdout

            with fptr:
                fptr.write(str(self.output) + "\n")

                fptr.close()

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_number()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
