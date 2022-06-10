#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 25 - Running Time and Complexity

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import Any, Callable, List, Optional

import big_o  # type: ignore
import typer
from rich.traceback import install

install()


def run() -> None:  # pragma: nocover
    """
    Run the app.
    """

    load_commands()
    app()


def load_commands() -> typer.Typer:
    """
    Defines app commands.

    Using this trick since directly using methods will prompt for "self"
    arguments on the command line.
    """

    cli = typer.Typer()

    @cli.command()
    def test(numbers: str = typer.Option(..., prompt_required=False)) -> None:
        """
        Run the challenge tests.
        """

        prog: Challenge

        if numbers in ["", "-"]:
            prog = Challenge()

        else:
            data: List[int] = [int(number) for number in numbers.split(" ")]

            prog = Challenge(numbers=data)

        prog.main()

    @cli.command()
    # pylint: disable=too-many-arguments
    def benchmark(
        quantity: int = 101,
        min_num: int = 1,
        max_num: int = 10001,
        n_measures: int = 23,
        n_repeats: int = 101,
    ) -> None:
        """
        Benchmark the is_prime() function using the big_o library.
        """

        prog: Challenge = Challenge()

        prog.bench_with_bigo(
            quantity=quantity,
            min_num=min_num,
            max_num=max_num,
            n_measures=n_measures,
            n_repeats=n_repeats,
        )

    return cli


app: typer.Typer = load_commands()


class Challenge:
    """
    Solution class.
    """

    def __init__(self,
                 quantity: int = 0,
                 numbers: Optional[List[int]] = None) -> None:

        self.quantity: int = quantity
        self.numbers: List[int]

        self.output: List[str] = []

        if numbers is not None:
            self.numbers = numbers.copy()
        else:
            self.numbers = []
            self.quantity = len(self.numbers)

        # Not sure if we care if len and quantity aren't equal when passed in.
        self.quantity = len(self.numbers)

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity == 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a list of numbers without a prompt to keep things interesting.
        """

        if len(self.numbers) == 0:
            for _ in range(0, self.quantity):
                self.numbers.append(int(input().strip()))
        else:
            pass

    @staticmethod
    def is_prime(number: int) -> bool:
        """
        Checks to see if the passed number is a prime number.

        Using case 8:
        - 1st iteration: 8m 58s
        - 2nd iteration: 4m 27s
        - 3rd iteration: 2m 12s
        - 4th iteration: 1m 45s
        - 5th iteration: 0m 0.6s
        """

        i: int
        result: bool = True

        if number <= 3:
            result = number > 1

        elif number % 2 == 0 or number % 3 == 0:
            result = False

        else:
            limit: int = int(number**0.5) + 1
            for i in range(5, limit, 2):
                if number % i == 0:
                    result = False
                else:
                    pass

        return result

    # pylint: disable=too-many-arguments
    def bench_with_bigo(
        self,
        quantity: int = 1000,
        min_num: int = 1,
        max_num: int = 10001,
        n_measures: int = 23,
        n_repeats: int = 1000,
    ) -> None:
        """
        Benchmark the is_prime() function using the big_o library.
        """

        number_generator: Callable[
            [Any],
            Any] = lambda n: big_o.datagen.integers(quantity, min_num, max_num)

        def bench_is_prime(numbers: List[int]) -> None:
            number: int

            for number in numbers:
                _ = self.is_prime(number)

        best, others = big_o.big_o(bench_is_prime,
                                   number_generator,
                                   n_measures=n_measures,
                                   n_repeats=n_repeats)

        print("Benchmarking the is_prime() function.\n")
        print(f"{best}")
        print()
        for class_, _ in others.items():
            print(class_)

    def solve(self) -> None:
        """
        Solves the challenge.
        """

        number: int

        for number in self.numbers:
            if self.is_prime(number):
                self.output.append("Prime")
            else:
                self.output.append("Not prime")

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        line: str

        for line in self.output:
            print(f"{line}")

    def main(self) -> None:
        """
        Run the challenge steps.
        """

        self.input_quantity()

        self.input_numbers()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge: Challenge = Challenge()

    challenge.main()
