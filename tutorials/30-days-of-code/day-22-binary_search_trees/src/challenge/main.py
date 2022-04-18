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

    def getHeight(self, root: Optional[Node]) -> int:
        """
        Write your code here
        """

        if root is None:
            return -1

        height_left: int = self.getHeight(root.left)
        height_right: int = self.getHeight(root.right)

        result: int

        if height_left > height_right:
            result = 1 + height_left
        else:
            result = 1 + height_right

        return result


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
