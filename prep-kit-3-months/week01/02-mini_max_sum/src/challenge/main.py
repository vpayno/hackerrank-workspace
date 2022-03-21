#!/usr/bin/env python
"""
https://www.hackerrank.com/challenges/30-review-loop/problem

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import sys
from typing import List, Optional, Tuple


class Challenge:
    """
    Week 1 - Plus Minus
    """

    def __init__(self, numbers: Optional[List[int]] = None):

        self.numbers: List[int] = []
        self.slice_size: int = 0
        self.results: Tuple[int, int] = (0, 0)

        if numbers:
            self.numbers = sorted(numbers)
            self.slice_size = max(len(numbers) - 1, 0)

    def min_max_sum(self):
        """Get the minimum and maximum sum from the list of numbers."""

        slice_min: List[int] = self.numbers[0:self.slice_size]
        slice_max: List[int] = self.numbers[-self.slice_size:]

        sum_min: int = sum(slice_min)
        sum_max: int = sum(slice_max)

        self.results = (sum_min, sum_max)

    def print_result(self):
        """Prints the Tuple with the min and max sum numbers."""
        print(" ".join([str(number) for number in self.results]))

    def input_numbers(self):
        """Ask for a list of numbers without a prompt because that's how HR rolls."""

        if len(self.numbers) <= 0:
            arr: List[int] = list(map(int, input().strip().split()))

            self.numbers = sorted(arr)
            self.slice_size = max(len(self.numbers) - 1, 0)
        else:
            # we need an else to make coverage happy
            pass

    def main(self):
        """Main method for the challenge."""

        self.input_numbers()

        self.min_max_sum()

        self.print_result()


def get_cmdline_arguments() -> List[int]:
    """Get the list of numbers from the command line."""

    input_numbers: List[int] = [int(number) for number in sys.argv[1:]]

    return input_numbers


if __name__ == "__main__":  # pragma: nocover

    data: List[int] = get_cmdline_arguments()

    program = Challenge(data)

    program.main()
