#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 10 - Binary Numbers

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from abc import ABCMeta, abstractmethod
from typing import Optional

from rich.traceback import install

install()


class Book(metaclass=ABCMeta):
    """Book class consisting of a title and author."""

    def __init__(self, title: str, author: str) -> None:

        self.title = title
        self.author = author

    @staticmethod
    @abstractmethod
    def __str__() -> str:
        """Abstract method."""

    @staticmethod
    @abstractmethod
    def display() -> None:
        """Abstract method."""


class MyBook(Book):
    """MyBook extends Book and adds price."""

    def __init__(self, title: str, author: str, price: int) -> None:

        super().__init__(title, author)
        self.price: int = price

    # https://github.com/python/mypy/issues/1237
    def __str__(self) -> str:  # type: ignore
        """Implements book.__str__()."""

        return (f"Title: {self.title}\n" + f"Author: {self.author}\n" +
                f"Price: {self.price}\n")

    # https://github.com/python/mypy/issues/1237
    def display(self) -> None:  # type: ignore
        """Implements book.display()."""

        print(self)


class Challenge:
    """
    Main challenge class.
    """

    def __init__(self, mybook: Optional[MyBook] = None) -> None:

        self.mybook: Optional[MyBook]

        if mybook is not None:
            self.mybook = mybook
        else:
            self.mybook = None

    def input_book(self) -> None:
        """
        Read inputs without a prompt to keep things interesting.
        """

        if self.mybook is None or None in [
                self.mybook.title,
                self.mybook.author,
                self.mybook.price,
        ]:
            title: str = input().strip()
            author: str = input().strip()
            price = int(input().strip())

            self.mybook = MyBook(title, author, price)
        else:
            pass

    def print_results(self) -> None:
        """Print the results of the challenge."""

        if self.mybook is not None:
            self.mybook.display()
        else:
            pass

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_book()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
