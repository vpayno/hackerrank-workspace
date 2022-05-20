#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 07 - Arrays

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional

from rich.traceback import install

install()


class InputDoesNotMatchQuantityException(Exception):
    """Raised when the quantity input doesn't match the number of numbers in
    the 2nd input.

    Attributes:
        quantity -- expected number of numbers in 2nd input
        numbers -- list of numbers from 2nd input
    """

    def __init__(
        self,
        quantity: int,
        numbers: List[int],
        message:
        str = "Quantity of numbers in 2nd input doesn't match the quantity " +
        "described in the 1st input.",
    ) -> None:

        self.quantity: int = quantity
        self.numbers: List[int] = numbers
        self.message: str = message

        super().__init__(self.message)

    def __str__(self) -> str:
        return (
            f"quantity={self.quantity} != len(numbers)={len(self.numbers)}\n" +
            f"{self.message}")


class Challenge:
    """
    Day 07 - Arrays
    """

    def __init__(self, numbers: Optional[List[int]] = None) -> None:

        self.numbers: List[int] = []
        self.quantity: int = 0

        self.output: List[int] = []

        if numbers is not None:
            # mypy: Argument 1 to "append" of "list" has incompatible type
            # "List[str]"; expected "str"
            # self.numbers.append(numbers)
            for line in numbers:
                self.numbers.append(line)
            self.quantity = len(numbers)
        else:
            self.numbers = []

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = max(int(input().strip()), 0)
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a space separated list of numbers without a prompt to keep things
        interesting.
        """

        if len(self.numbers) <= 0:
            self.numbers = [
                int(number) for number in input().strip().split(" ")
            ]
        else:
            pass

        # We're not using the first integer but maybe we should through an
        # exception if the quantity number doesn't match the number of numbers
        # in the second inputs.
        if self.quantity == len(self.numbers):
            # We need if/else for coverage but pylint doesn't like an else after a raise.
            pass
        else:
            raise InputDoesNotMatchQuantityException(self.quantity,
                                                     self.numbers)

    def solve(self) -> None:
        """
        Reverse the numbers in the list.
        """

        self.output = list(reversed(self.numbers))

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print(" ".join([str(number) for number in self.output]))

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_quantity()

        # Intentionally not catching the raised exception.
        self.input_numbers()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
