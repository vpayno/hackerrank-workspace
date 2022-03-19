#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 03 - Operators

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import locale
import sys


class Challenge:
    """
    Day 03 - Operators
    """

    def __init__(self, debug: bool = False):

        self.debug = debug

        # English_United States.1252
        locale.setlocale(locale.LC_ALL, "")

        self.meal_cost: float = 0.0
        self.tip_percent: int = 0
        self.tax_percent: int = 0

        self.tip: float = 0.0
        self.tax: float = 0.0
        self.total: float = 0.0

    def input_meal_cost(self):
        """
        Read a float without a prompt to keep things interesting.
        """
        self.meal_cost = float(input().strip())

    def input_tip_percent(self):
        """
        Read an integer without a prompt to keep things interesting.
        """
        self.tip_percent = int(input().strip())

    def input_tax_percent(self):
        """
        Read a string without a prompt to keep things interesting.
        """
        self.tax_percent = int(input().strip())

    def solve(self):
        """
        Calculates the cost of the meal.
        """

        self.tip = self.meal_cost * (self.tip_percent / 100)
        self.tax = self.meal_cost * (self.tax_percent / 100)
        self.total = self.tip + self.tax + self.meal_cost

        if self.debug:
            self.print_results()
        else:
            # For the challange, solve() prints the total as an integer.
            print(int(round(self.total, ndigits=0)))

    def print_results(self):
        """
        Print the results.
        """
        # print(f"Subtotal: ${self.meal_cost:>7,.2f}")
        # print(f"     Tip: ${self.tip:>7,.2f} ({self.tip_percent:,}%)")
        # print(f"     Tax: ${self.tax:>7,.2f} ({self.tax_percent:,}%)")
        # print(f"   Total: ${self.total:>7,.2f}")
        output: str = f"""
        Subtotal: ${self.meal_cost:>7,.2f}
            Tip: ${self.tip:>7,.2f} {self.tip_percent:,}%
            Tax: ${self.tax:>7,.2f} {self.tax_percent:,}%
        Total: ${self.total:>7,.2f}
        """
        print(output)

    def main(self):
        """
        Read and save an integer, double, and String to your variables.
        """
        self.input_meal_cost()
        self.input_tip_percent()
        self.input_tax_percent()

        self.solve()


if __name__ == "__main__":  # pragma: no cover

    DEBUG: bool
    try:
        DEBUG = sys.argv[1] == "--debug"
    except IndexError:
        DEBUG = False

    challenge = Challenge(DEBUG)

    challenge.main()
