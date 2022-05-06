#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 02 - Data Types

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""


class Challenge:
    """
    Day 02 - Data Types
    """

    def __init__(self) -> None:
        self.int1: int = 4
        self.double1: float = 4.0
        self.str1: str = "HackerRank "

        # Declare second integer, double, and String variables.
        self.int2: int = 0
        self.double2: float = 0.0
        self.str2: str = ""

    def __str__(self) -> str:
        """
        String representation of the class.
        """

        return " ".join([
            str(self.int1 + self.int2),
            str(self.double1 + self.double2),
            str(self.str1 + self.str2),
        ])

    def input_int(self) -> None:
        """
        Read an integer without a prompt to keep things interesting.
        """
        self.int2 = int(input())

    def input_float(self) -> None:
        """
        Read a float without a prompt to keep things interesting.
        """
        self.double2 = float(input())

    def input_str(self) -> None:
        """
        Read a string without a prompt to keep things interesting.
        """
        self.str2 = input()

    def print_results(self) -> None:
        """
        Print the results.
        """
        # Print the sum of both integer variables on a new line.
        print(self.int1 + self.int2)

        # Print the sum of the double variables on a new line.
        print(self.double1 + self.double2)

        # Concatenate and print the String variables on a new line
        # The 's' variable above should be printed first
        print(self.str1 + self.str2)

    def main(self) -> None:
        """
        Read and save an integer, double, and String to your variables.
        """
        self.input_int()
        self.input_float()
        self.input_str()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
