#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 25 - Running Time and Complexity

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

        self.output: List[str] = []

        if numbers is not None:
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
            for _ in range(0, self.quantity):
                self.numbers.append(int(input().strip()))
        else:
            pass

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Checks to see if the passed number is a prime number.

        Using case 8:
        - 1st iteration: 8m 58s
        - 2nd iteration: 4m 27s
        """

        i: int
        result: bool = True

        if number == 1:
            result = False

        elif number == 2:
            result = True

        elif number % 2 == 0:
            result = False

        else:
            for i in range(3, number, 2):
                if number % i == 0:
                    result = False
                else:
                    pass

        return result

    def solve(self) -> None:
        """
        Solves the challenge.
        """

        number: int

        for number in self.numbers:
            if self.is_prime(number):
                self.output.append("Prime")
            else:
                self.output.append("Not prime")

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        line: str

        for line in self.output:
            print(f"{line}")

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
