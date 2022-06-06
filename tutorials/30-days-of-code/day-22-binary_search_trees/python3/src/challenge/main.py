#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 22 - Binary Search Trees

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

from typing import List, Optional

from rich.traceback import install

install()


class Node:  # pylint: disable=too-few-public-methods
    """
    Binary tree node.
    """

    def __init__(self, data: int) -> None:
        self.right: Optional[Node] = None
        self.left: Optional[Node] = None
        self.data: int = data


class Solution:
    """
    Solution class.
    """

    def insert(self, root: Optional[Node], data: int) -> Node:
        """
        Insert node.
        """

        cur: Node
        node: Node

        if root is None:
            node = Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur

            node = root

        return node

    def get_height(self, root: Optional[Node]) -> int:
        """
        Write your code here
        """

        if root is None:
            return -1

        height_left: int = self.get_height(root.left)
        height_right: int = self.get_height(root.right)

        result: int

        if height_left > height_right:
            result = 1 + height_left
        else:
            result = 1 + height_right

        return result


class Challenge:
    """
    Challenge Solution
    """

    def __init__(
        self,
        quantity: int = 0,
        numbers: Optional[List[int]] = None,
    ) -> None:

        self.quantity: int = quantity

        self.numbers: List[int]

        self.output: int = 0

        if numbers is not None:
            self.numbers = numbers
        else:
            self.numbers = []

        self.tree: Solution = Solution()

    def input_quantity(self) -> None:
        """
        Read an int without a prompt to keep things interesting.
        """

        if self.quantity <= 0:
            self.quantity = int(input().strip())
        else:
            pass

    def input_numbers(self) -> None:
        """
        Read a list of ints without a prompt to keep things interesting.
        """

        number: int = 0

        if len(self.numbers) <= 0:
            for _ in range(self.quantity):
                number = int(input().strip())
                self.numbers.append(number)

            self.quantity = len(self.numbers)
        else:
            pass

    def solve(self) -> None:
        """Solves the challenge."""

        root: Optional[Node] = None
        data: int

        for data in self.numbers:
            root = self.tree.insert(root, data)

        self.output = self.tree.get_height(root)

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print(self.output)

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
