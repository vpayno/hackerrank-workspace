"""
HackerRank - 30 Days of Code - Day 01 - HelloWorld

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import sys


class Challenge:
    """
    Day 01 - HelloWorld
    """

    def __init__(self, greeting="Hello, World."):
        """
        The things we do to make pylink happy.
        """

        self.greeting: str = greeting
        self.input_string: str = None

    def __str__(self):
        """
        String representation of the class.
        """

        output: str = None

        if self.input_string:
            output = self.greeting + " " + self.input_string
        else:
            output = self.greeting

        return output

    def hello_world(self, input_string=None):
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

    user_input: str = None if sys.argv[1] is None else sys.argv[1]

    challenge = Challenge()

    challenge.hello_world(input_string=user_input)
