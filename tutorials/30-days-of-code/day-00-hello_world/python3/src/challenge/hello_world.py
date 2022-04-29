"""
HackerRank - 30 Days of Code - Day 00 - Hello World

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import sys
from typing import List, Optional


class Challenge:
    """
    Day 00 - Hello World
    """

    def __init__(self, greeting: str = "Hello, World.") -> None:
        """
        The things we do to make pylink happy.
        """

        self.greeting: str = greeting
        self.input_string: Optional[str] = None

    def __str__(self) -> str:
        """
        String representation of the class.
        """

        output: Optional[str] = None

        if self.input_string:
            output = f"{self.greeting} {self.input_string}"
        else:
            output = self.greeting

        return output

    def hello_world(self, input_string: Optional[str] = None) -> List[str]:
        """
        Read a full line of input from stdin and save it to our dynamically
        typed variable, input_string.

        Print a string literal saying "Hello, World." to stdout.

        Print the user supplied string.
        """

        if input_string:
            self.input_string = input_string
        else:
            self.input_string = input()

        print(self.greeting)

        print(self.input_string)

        return [self.greeting, self.input_string]


if __name__ == "__main__":  # pragma: no cover

    user_input: Optional[str] = None if sys.argv[1] is None else sys.argv[1]

    challenge = Challenge()

    terminal_output: List[str] = challenge.hello_world(input_string=user_input)
