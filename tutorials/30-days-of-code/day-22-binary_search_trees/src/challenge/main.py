#!/usr/bin/env python3
"""
Day 22: Binary Search Trees
"""

from typing import Optional


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
    def getHeight(root: Optional[Node]) -> int:
        """
        Write your code here
        """

        height: int

        if root is not None:

            node: Optional[Node]

            node = root
            height_left: int = 0

            while node.left is not None:
                height_left += 1
                node = node.left

            node = root
            height_right: int = 0

            while node.right is not None:
                height_right += 1
                node = node.right

            height = max(height_left, height_right)

        else:

            height = -1

        return height


T: int = int(input())

myTree: Solution = Solution()
root: Optional[Node] = None
data: int

i: int
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)

height: int = myTree.getHeight(root)
print(height)
