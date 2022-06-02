#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 19 - Interfaces

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List

from rich.traceback import install

install()


class AdvancedArithmetic:  # pylint: disable=too-few-public-methods
    """
    Informal Abstract Class
    """

    def divisor_sum(self, number: int) -> int:
        """
        Returns the sum of the multiples of a number.
        """

        raise NotImplementedError


class Calculator(AdvancedArithmetic):  # pylint: disable=too-few-public-methods
    """
    Calculator class.
    """

    def divisor_sum(self, number: int) -> int:
        """
        Returns the sum of the multiples of a number.
        """

        multiples: List[int] = []

        for divisor in range(1, number + 1):
            if number % divisor == 0:
                multiples.append(divisor)

        return sum(multiples)


class Challenge:
    """
    Solution class.
    """

    def __init__(self, number: int = 0) -> None:

        self.number: int = number
        self.output: int = 0

        self.calculator: Calculator = Calculator()

    def input_number(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.number == 0:
            self.number = int(input().strip())
        else:
            pass

    def solve(self) -> None:
        """
        Solves the challenge.
        """

        self.output = self.calculator.divisor_sum(self.number)

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        print("I implemented: " + type(self.calculator).__bases__[0].__name__)
        print(self.output)

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
