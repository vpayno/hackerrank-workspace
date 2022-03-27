#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 10 - Binary Numbers

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional

from rich.traceback import install

install()


class Person:
    """Person class"""

    def __init__(self, first_name: str, last_name: str, id_number: str):

        self.first_name: str = first_name.strip()
        self.last_name: str = last_name.strip()
        self.id_number: str = id_number.strip()

    def __str__(self) -> str:
        """String representation of class."""

        string: str = f"Name: {self.last_name}, {self.first_name}"
        string += f" ID: {self.id_number}"

        return string

    def print_person(self):
        """Show info about a person."""

        print(f"Name: {self.last_name}, {self.first_name}")
        print(f"ID: {self.id_number}")


class Student(Person):
    """Inherits Person, adds scores and calculate()"""

    def __init__(self, first_name: str, last_name: str, id_number: str,
                 scores: List[int]):

        super().__init__(first_name, last_name, id_number)

        self.scores: List[int] = scores.copy()

    def calculate(self) -> str:
        """Calculate a student's average and return the grade."""
        average: float
        grade: str

        average = sum(self.scores) / len(self.scores)

        if average >= 90:
            grade = "O"
        elif average >= 80:
            grade = "E"
        elif average >= 70:
            grade = "A"
        elif average >= 55:
            grade = "P"
        elif average >= 40:
            grade = "D"
        else:
            grade = "T"

        return grade


class Challenge:
    """
    Main challenge class.
    """

    def __init__(self,
                 student: Optional[Student] = None,
                 quantity: Optional[int] = None):

        self.student: Optional[Student]
        self.quantity: int

        self.output: str = ""

        if student is not None:
            self.student = student
        else:
            self.student = None

        if quantity is not None:
            self.quantity = quantity
        else:
            self.quantity = 0

    def input_user(self):
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.student is None or None in [
                self.student.first_name,
                self.student.last_name,
                self.student.id_number,
        ]:
            line: List[str] = input().split()

            first_name: str = line[0]
            last_name: str = line[1]
            id_number: str = line[2]
            scores: List[int] = []

            self.student = Student(first_name, last_name, id_number, scores)
        else:
            pass

    def input_quantity(self):
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = max(int(input().strip()), 0)
        else:
            pass

    def input_scores(self):
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.student is not None and len(self.student.scores) <= 0:
            self.student.scores = list(map(int, input().split()))
        else:
            pass

    def solve(self):
        """Solves the challenge."""

        if self.student is not None:
            self.output = self.student.calculate()
        else:
            pass

    def print_results(self):
        """Print the results of the challenge."""

        if self.student is not None and self.output != "":
            self.student.print_person()
            print(f"Grade: {self.output}")
        else:
            pass

    def main(self):
        """
        Challenge steps.
        """

        self.input_user()

        self.input_quantity()

        self.input_scores()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
