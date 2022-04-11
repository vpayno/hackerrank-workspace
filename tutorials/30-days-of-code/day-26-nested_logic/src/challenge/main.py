#!/usr/bin/env python3

from datetime import datetime, timedelta
from typing import List


class Challenge:

    def __init__(self) -> None:
        self.return_date: datetime
        self.due_date: datetime

    def input_return_date(self) -> None:
        date: List = [int(num) for num in input().strip().split(" ")]
        self.return_date = datetime(date[2], date[1], date[0])

    def input_due_date(self) -> None:
        date: List = [int(num) for num in input().strip().split(" ")]
        self.due_date = datetime(date[2], date[1], date[0])

    def get_fine(self) -> int:
        """
        1. before due date = 0

        2. If the book is returned after the expected return day but still within the same calendar month and year as the expected return date. => 15 * days late

        3. If the book is returned after the expected return month but still within the same calendar year as the expected return date. => 500 * months late

        4. If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10,000
        """

        fine: int = 0

        print(f"return date: {self.return_date}")
        print(f"   due date: {self.due_date}")

        if self.return_date <= self.due_date:
            print(f"on time: {self.return_date} <= {self.due_date}")
            fine = 0

        elif self.return_date.year <= self.due_date.year:
            print(
                f"late same year: {self.return_date.year} <= {self.due_date.year}"
            )

            if self.return_date.month == self.due_date.month:
                print(
                    f"late same month: {self.return_date.month} == {self.due_date.month}"
                )
                fine = 15 * abs(self.due_date.day - self.return_date.day)

            elif self.return_date.month > self.due_date.month:
                print(
                    f"late later month: {self.return_date.month} > {self.due_date.month}"
                )
                fine = 500 * abs(self.due_date.month - self.return_date.month)
        else:
            print(
                f"late later year: {self.return_date.year} > {self.due_date.year}"
            )
            fine = 10_000

        return fine


if __name__ == "__main__":
    challenge: Challenge = Challenge()

    challenge.input_return_date()
    challenge.input_due_date()

    print(challenge.get_fine())
