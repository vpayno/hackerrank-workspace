#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 06 - Review

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional


class Challenge:
    """
    Day 06 - Review
    """

    def __init__(self, lines: Optional[List[str]] = None) -> None:

        self.input_lines: int
        self.lines: List[str] = []
        self.output: List[str] = []

        self.line: str

        if lines is not None:
            # mypy: Argument 1 to "append" of "list" has incompatible type
            # "List[str]"; expected "str"
            # self.lines.append(lines)
            for line in lines:
                self.lines.append(line)
            self.input_lines = len(self.lines)
        else:
            self.lines = []
            self.input_lines = 0

    def input_number(self) -> None:
        """
        Read a number without a prompt to keep things interesting.
        """

        if self.input_lines <= 0:
            self.input_lines = max(int(input().strip()), 0)
        else:
            pass

    def input_string(self) -> None:
        """
        Read a string without a prompt to keep things interesting.
        """

        if len(self.lines) <= 0:
            data: str

            for _ in range(0, self.input_lines):
                data = input().strip()
                self.lines.append(data)
        else:
            pass

    def solve(self) -> None:
        """
        Break up the string into an even and odd index strings.
        """

        index: int
        letter: str
        text_even: str = ""
        text_odd: str = ""
        new_line: str
        line: str

        self.output = []

        for line in self.lines:
            text_even = ""
            text_odd = ""

            for index, letter in enumerate(line):
                if index % 2 == 0:
                    text_even += letter
                else:
                    text_odd += letter

            # The instructions said two spaces but their tests look for one.
            new_line = f"{text_even} {text_odd}"
            self.output.append(new_line)

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print("\n".join(self.output))

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_number()

        self.input_string()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
