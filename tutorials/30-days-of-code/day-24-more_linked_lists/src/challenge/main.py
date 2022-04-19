#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 24 - More Linked Lists

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import Iterator, List, Optional

from rich.traceback import install

install()


class Node:
    """
    Node of a linked-list.
    """

    def __init__(self, data: int) -> None:

        self.data: int = data
        self.next: Optional[Node] = None

    def __str__(self) -> str:
        """
        String representation of the Node's data.
        """

        return str(self.data)

    def __int__(self) -> int:
        """
        Int representation of the Node's data.
        """

        return self.data


class LinkedList:
    """
    LinkedList of Node[int].
    """

    def __init__(self) -> None:

        self.head: Optional[Node] = None

        self.iter: Optional[Node] = None

    def insert(self, data: int) -> None:
        """
        Inserts a node into a linked list.
        """

        start: Node
        previous: Node = Node(data)

        if self.head is None:
            self.head = previous

        elif self.head.next is None:
            self.head.next = previous

        else:
            start = self.head

            while start.next is not None:
                start = start.next

            start.next = previous

    def display(self) -> None:
        """
        Print the linked-list.
        """

        current: Optional[Node] = self.head
        output: str = ""

        while current:
            output += f"{current.data} "
            current = current.next

        print(output.strip())

    def remove_duplicates(self) -> None:
        """
        Remove duplicates from a node list.
        """

        items: List[int] = []

        current: Optional[Node] = self.head
        previous: Optional[Node] = None

        while current is not None:

            if current.data in items:
                if previous is not None:
                    previous.next = current.next
                else:
                    pass  # pragma: nocover

            else:
                items.append(current.data)
                previous = current

            current = current.next

    def __iter__(self) -> Iterator:
        """
        Returns the class as the iterator.
        """

        self.iter = self.head

        return self

    def __next__(self) -> int:
        """
        Returns the next int.
        """

        current: Optional[Node] = self.iter
        number: int

        if current:
            number = current.data
            self.iter = current.next
        else:
            raise StopIteration

        return number


class Challenge:
    """
    Solution class.
    """

    def __init__(self,
                 quantity: int = 0,
                 numbers: Optional[List[int]] = None) -> None:

        self.quantity: int = quantity
        self.numbers: List[int]

        self.linked_list: Optional[LinkedList] = None

        if numbers is None:
            self.numbers = []
        else:
            self.numbers = numbers.copy()

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = max(int(input().strip()), 0)
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a list of ints without a prompt to keep things interesting.
        """

        if len(self.numbers) <= 0:
            for _ in range(0, self.quantity):
                number = int(input().strip())
                self.numbers.append(number)
        else:
            pass

    def solve(self) -> None:
        """Solves the challenge."""

        self.linked_list = LinkedList()
        data: int

        for data in self.numbers:
            self.linked_list.insert(data)

        self.linked_list.remove_duplicates()

    def print_results(self) -> None:
        """Print the results of the challenge."""

        # I tried using an try/except block but mypy didn't like that.
        if self.linked_list:
            self.linked_list.display()
        else:
            print("ERROR: linked list not defined.")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_quantity()

        self.input_numbers()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
