#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 26 - Nested Logic

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from datetime import datetime
from typing import List, Optional

from rich.traceback import install

install()


class Challenge:
    """
    Solution class.
    """

    def __init__(
        self,
        return_date: Optional[datetime] = None,
        due_date: Optional[datetime] = None,
    ) -> None:

        self.return_date: Optional[datetime] = return_date
        self.due_date: Optional[datetime] = due_date

        self.output: int = 0

    def input_return_date(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.return_date is None:
            date: List[int] = [int(num) for num in input().strip().split(" ")]
            self.return_date = datetime(date[2], date[1], date[0])
        else:
            pass

    def input_due_date(self) -> None:
        """
        Read a date without a prompt to keep things interesting.
        """
        if self.due_date is None:
            date: List[int] = [int(num) for num in input().strip().split(" ")]
            self.due_date = datetime(date[2], date[1], date[0])
        else:
            pass

    def get_fine(self) -> int:
        """
        Returns the fine for a book given the return and due date.

        1. Returned before due date. => 0

        2. If the book is returned after the expected return day but still
           within the same calendar month and year as the expected return date.
           => 15 * days late

        3. If the book is returned after the expected return month but still
           within the same calendar year as the expected return date.
           => 500 * months late

        4. If the book is returned after the calendar year in which it was
           expected, there is a fixed fine of 10,000.
        """

        fine: int = 0

        if self.return_date is not None and self.due_date is not None:
            if self.return_date <= self.due_date:
                fine = 0

            elif self.return_date.year <= self.due_date.year:

                if self.return_date.month == self.due_date.month:
                    fine = 15 * abs(self.due_date.day - self.return_date.day)

                elif self.return_date.month > self.due_date.month:
                    fine = 500 * abs(self.due_date.month -
                                     self.return_date.month)

                else:
                    # Added to keep coverage from reporting lines 82-90 as untested.
                    pass  # pragma: nocover

            else:
                fine = 10_000
        else:
            pass  # pragma: nocover

        return fine

    def solve(self) -> None:
        """Solves the challenge."""

        self.output = self.get_fine()

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print(f"{self.output}")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_return_date()

        self.input_due_date()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
