#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 04 - Class vs Instance

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""


class Person:
    """
    Person with an age.
    """

    def __init__(self, age: int) -> None:

        # The problem description says the age can be -5 <= age <= 30; But,
        # that's not tested in the 3 test cases and it gets reset to 0 here if
        # it's negative.
        if age >= 0:
            self.age: int = age
        else:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def am_i_old(self) -> None:
        """
        Checks the person's age to determine how old they are.
        """

        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age < 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self) -> None:
        """
        Increment the person's age by one.
        """

        self.age += 1


class Challenge:
    """
    Day 04 - Class vs Instance
    """

    def __init__(self) -> None:

        self.age: int = 0
        self.test_cases: int = 0

    def input_test_cases(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        # The problem page says the number of test cases is contrainted to
        # 1 <= T < 4 but it's not enforced in the stub code they provide.
        self.test_cases = int(input().strip())

    def input_age(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        self.age = int(input().strip())

    def solve(self) -> None:
        """
        Calculates if the user is old.
        """

        for _ in range(0, self.test_cases):
            self.input_age()
            person: Person = Person(self.age)
            person.am_i_old()

            for _ in range(0, 3):
                person.year_passes()

            person.am_i_old()
            print("")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_test_cases()

        self.solve()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
