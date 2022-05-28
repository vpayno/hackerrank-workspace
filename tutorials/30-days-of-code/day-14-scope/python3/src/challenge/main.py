#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 14 - Scope

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional

from rich.traceback import install

install()


class Difference:
    """
    Day 14 - Scope
    """

    def __init__(self, numbers: List[int]):
        self.numbers: List[int] = numbers
        self.maximum_difference: int = 0

    def __str__(self) -> str:
        """String representation of the class."""

        return f"Largest difference in {self.numbers} is {self.maximum_difference}\n"

    def compute_difference(self):
        """Finds the maximum absolute difference between any  numbers in a list of numbers."""

        diff: int

        self.numbers.sort()

        diff = abs(self.numbers[0] - self.numbers[-1])

        self.maximum_difference = diff


class Challenge:
    """
    Day 14 - Scope
    """

    def __init__(self,
                 quantity: Optional[int] = None,
                 numbers: Optional[List[int]] = None):

        self.quantity: int = 0
        self.numbers: List[int] = []

        self.output: int = 0

        if quantity is not None:
            self.quantity = quantity
        else:
            self.quantity = 0

        if numbers is not None:
            self.numbers += numbers
        else:
            self.numbers = []

    def input_quantity(self):
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = max(int(input().strip()), 0)
        else:
            pass

    def input_numbers(self):
        """
        Read a list of ints without a prompt to keep things interesting.
        """

        if len(self.numbers) <= 0:
            self.numbers = [
                int(number) for number in input().strip().split(" ")
            ]
        else:
            pass

    def solve(self):
        """Solves the challenge."""

        code = Difference(self.numbers)
        code.compute_difference()

        self.output = code.maximum_difference

    def print_results(self):
        """Print the results of the challenge."""

        print(self.output)

    def main(self):
        """
        Challenge steps.
        """

        self.input_quantity()

        self.input_numbers()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
