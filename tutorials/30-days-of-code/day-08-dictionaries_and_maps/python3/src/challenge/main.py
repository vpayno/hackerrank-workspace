#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 07 - Arrays

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import Dict, List

from rich.traceback import install

install()


class Challenge:
    """
    Day 07 - Arrays
    """

    def __init__(self) -> None:

        self.quantity: int = 0
        self.data: Dict[str, str] = {}
        self.names: List[str] = []

        self.output: List[str] = []

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        self.quantity = max(int(input().strip()), 0)

    def input_data(self) -> None:
        """
        Read a list of names and numbers without a prompt to keep things
        interesting.
        """

        name: str
        value: str

        for _ in range(0, self.quantity):
            name, value = input().strip().split(" ")
            self.data[name] = value.strip()

    def input_names(self) -> None:
        """
        Read a list of names without a prompt to keep things
        interesting. Stop when we reach EOF.
        """

        name: str

        while True:
            try:
                name = input().strip()

                if name in ["", "EOF"]:
                    raise EOFError

                self.names.append(name)

            except EOFError:
                break

    def solve(self) -> None:
        """
        Reverse the numbers in the list.
        """

        name: str
        value: str

        for name in self.names:
            try:
                value = self.data[name]
                self.output.append(f"{name}={value}")
            except KeyError:
                self.output.append("Not found")

    def print_results(self) -> None:
        """Print the results of the challenge."""

        line: str

        for line in self.output:
            print(line)

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_quantity()

        self.input_data()

        self.input_names()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
