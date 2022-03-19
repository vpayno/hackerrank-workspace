#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 03 - Intro to Conditional Statements

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""


class Challenge:
    """
    Day 03 - Intro to Conditional Statements
    """

    def __init__(self):

        self.number: int = 0
        self.result: str = ""

    def input_number(self):
        """
        Read a string without a prompt to keep things interesting.
        """
        self.number = int(input().strip())

    def solve(self):
        """
        Calculates if the number is weird or not.
        """

        if (self.number % 2) == 1:
            self.result = "Weird"
        else:
            if self.number in range(2, 5 + 1):
                self.result = "Not Weird"
            elif self.number in range(6, 20 + 1):
                self.result = "Weird"
            elif self.number > 20:
                self.result = "Not Weird"
            else:
                # coverage wants an else to close out an if statement
                pass  # pragma: no cover

        print(self.result)

    def main(self):
        """
        Read and save an integer, double, and String to your variables.
        """
        self.input_number()

        self.solve()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
