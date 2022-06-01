#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 15 - Linked List

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import Dict, List, Optional

from rich.traceback import install

install()


class CalculatorError(Exception):
    """
    Calculator exception class.
    """

    def __init__(self, key: str = "generic") -> None:
        self.messages: Dict[str, str] = {}
        self.message: str

        self.messages["generic"] = "generic calculator error"
        self.messages["power"] = "n and p should be non-negative"

        self.message = self.messages.get(key, "generic calculator error")

        super().__init__(self.message)


class Calculator:  # pylint: disable=too-few-public-methods
    """
    Calculator that only knows how to calculate powers.
    """

    @staticmethod
    def power(number: int, power: int) -> int:
        """
        Calculates power p of n.
        """

        if number >= 0 and power >= 0:
            result: int = 1
            for _ in range(0, power):
                result = result * number
        else:
            raise CalculatorError("power")

        return result


class Challenge:
    """
    Solution class.
    """

    def __init__(self,
                 quantity: int = 0,
                 numbers: Optional[List[List[int]]] = None) -> None:

        self.quantity: int = quantity

        self.numbers: Optional[List[List[int]]]

        self.calculator = Calculator()

        if numbers:
            self.numbers = numbers.copy()
        else:
            self.numbers = []

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a pair of ints without a prompt to keep things interesting.
        """

        if self.numbers is None or len(self.numbers) == 0:
            self.numbers = []

            number: int
            power: int

            for _ in range(0, self.quantity):
                number, power = map(int, input().strip().split())
                self.numbers.append([number, power])
        else:
            pass

    def solve(self) -> None:
        """Solves the challenge."""

        number: int
        power: int
        result: int

        for number, power in self.numbers or []:
            # for the output to match the challenge, we have to print the results
            # or the exception text at the same time.
            try:
                result = self.calculator.power(number, power)
                print(result)
            except CalculatorError as error:
                print(error)

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_quantity()

        self.input_numbers()

        self.solve()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
