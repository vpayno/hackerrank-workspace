#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 28 - RegEx, Patterns, and Intro to Databases

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import re
from typing import Dict, List, Optional

from rich.traceback import install

install()


class Challenge:
    """
    Solution class.
    """

    def __init__(self,
                 quantity: int = 0,
                 database: Optional[Dict[str, str]] = None) -> None:

        self.quantity: int = quantity
        self.database: Dict[str, str]

        self.results: List[str] = []

        if database:
            self.database = database.copy()
        else:
            self.database = {}

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity == 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_data(self) -> None:
        """
        Read a list of names and email addresses without a prompt to keep things interesting.
        """

        first_name: str = ""
        email: str = ""

        if self.database == {}:
            for _ in range(0, self.quantity):
                first_name, email = input().strip().split()
                self.database[email] = first_name
        else:
            pass

    def solve(self) -> None:
        """
        Solves the challenge.
        """

        email: str = ""
        first_name: str = ""

        reo: re.Pattern = re.compile(r"^.*@gmail.com$")

        self.results = []

        for email, first_name in self.database.items():
            if reo.match(email):
                self.results.append(first_name)
            else:
                pass

        self.results.sort()

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        first_name: str = ""

        for first_name in self.results:
            print(f"{first_name}")

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
