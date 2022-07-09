#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 29 - Bitwise AND

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import os
import sys
from typing import List, Optional, TextIO

from rich.traceback import install

install()


class Challenge:
    """
    Challenge Solution
    """

    def __init__(
        self,
        quantity: int = 0,
        data: Optional[List[tuple[int, int]]] = None,
    ) -> None:

        self.quantity: int = quantity

        self.data: List[tuple[int, int]]

        self.output: List[int] = []

        if data is not None:
            self.data = data
        else:
            self.data = []

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_data(self) -> None:
        """
        Read a list of ints without a prompt to keep things interesting.
        """

        number: int = 0
        limit: int = 0

        if len(self.data) <= 0:
            for _ in range(self.quantity):
                number, limit = [int(num) for num in input().strip().split()]
                self.data.append((number, limit))
        else:
            pass

    @staticmethod
    def bitwise_and(number: int, limit: int) -> int:
        """Finds the maximum bit."""

        maximum: int = 0

        i: int
        j: int
        result: int

        for i in range(1, number + 1):

            for j in range(1, i):

                result = i & j

                if maximum < result < limit:
                    maximum = result
                else:
                    pass

                if maximum == limit - 1:
                    return maximum

        return maximum

    def solve(self) -> None:
        """Solves the challenge."""

        number: int
        limit: int

        self.output = []

        for number, limit in self.data:
            self.output.append(self.bitwise_and(number, limit))

    def print_results(self) -> None:
        """Print the results of the challenge."""

        number: int

        if "pytest" in sys.modules:

            for number in self.output:
                print(f"{number}")

        else:

            fptr: TextIO

            try:
                fptr = open(os.environ["OUTPUT_PATH"], "w", encoding="utf8")
            except KeyError:
                fptr = sys.stdout

            with fptr:
                for number in self.output:
                    fptr.write(f"{number}\n")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_quantity()

        self.input_data()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
