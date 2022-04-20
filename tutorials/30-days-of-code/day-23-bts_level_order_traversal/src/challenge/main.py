#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 23 - BST Level-Order Traversal

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

    @staticmethod
    def level_order(root: Optional[Node]) -> List[str]:
        """
        A level-order traversal, also known as a breadth-first search, visits
        each level of a tree's nodes from left to right, top to bottom. You are
        given a pointer, root, pointing to the root of a binary search tree.
        Complete the levelOrder function provided in your editor so that it
        prints the level-order traversal of the binary search tree.
        """

        results: List[str] = []
        queue: List[Node] = []

        current: Optional[Node]

        if root is not None:
            current = root
        else:
            current = None
            results = []

        while current is not None:
            results.append(f"{current.data}")

            if current.left is not None:
                queue.append(current.left)
            else:
                pass

            if current.right is not None:
                queue.append(current.right)
            else:
                pass

            try:
                current = queue.pop(0)
            except IndexError:
                break
        else:
            results = []

        return results


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

        self.output: List[str] = []

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

        self.output = self.tree.level_order(root)

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print(" ".join(self.output))

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
