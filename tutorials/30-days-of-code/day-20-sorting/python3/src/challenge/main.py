#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 20 - Bubble Sort

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional

from rich.traceback import install

install()


class Challenge:
    """
    Solution class.
    """

    def __init__(self,
                 quantity: int = 0,
                 numbers: Optional[List[int]] = None) -> None:

        self.quantity: int = quantity
        self.numbers: List[int]

        self.num_swaps: int = 0
        self.first_element: int
        self.last_element: int

        if numbers:
            self.numbers = numbers.copy()
        else:
            self.numbers = []

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity == 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a list of numbers without a prompt to keep things interesting.
        """

        if len(self.numbers) == 0:
            self.numbers = list(map(int, input().rstrip().split(" ")))
        else:
            pass

    def solve(self) -> None:
        """
        Solves the challenge.
        """

        i: int
        j: int

        for i in range(0, len(self.numbers)):

            for j in range(0, len(self.numbers) - i - 1):

                if self.numbers[j] > self.numbers[j + 1]:
                    self.numbers[j], self.numbers[j + 1] = (
                        self.numbers[j + 1],
                        self.numbers[j],
                    )
                    self.num_swaps += 1

            if self.num_swaps == 0:
                break

        self.first_element = self.numbers[0]
        self.last_element = self.numbers[-1]

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        print(f"Array is sorted in {self.num_swaps} swaps.")
        print(f"First Element: {self.first_element}")
        print(f"Last Element: {self.last_element}")

    def main(self) -> None:
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
