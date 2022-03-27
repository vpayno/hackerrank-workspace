#!/usr/bin/env python3
"""
Day 12 - Inheritance
"""

from typing import List


class Person:
    """Person class"""

    def __init__(self, firstName: str, lastName: str, idNumber: str):

        self.firstName: str = firstName
        self.lastName: str = lastName
        self.idNumber: str = idNumber

    def printPerson(self):
        """How info about a person."""

        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    """Inherits Person, adds scores and calculate()"""

    def __init__(self, firstName: str, lastName: str, idNumber: str,
                 scores: List[int]):

        super().__init__(firstName, lastName, idNumber)

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


line: List[str] = input().split()
firstName: str = line[0]
lastName: str = line[1]
idNum: str = line[2]
numScores: int = int(input())  # not needed for Python
scores: List[int] = list(map(int, input().split()))
s: Student = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
