#!/usr/bin/env python3

import sys


class Node:

    def __init__(self, data):
        self.right = self.left = None
        self.data = data


class Solution:

    def insert(self, root, data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left, data)
                root.left = cur
            else:
                cur = self.insert(root.right, data)
                root.right = cur
        return root

    def levelOrder(self, root):
        results = []
        queue = []

        current = root

        while current is not None:
            results.append(f"{current.data}")
            if current.left is not None:
                queue.append(current.left)
            if current.right is not None:
                queue.append(current.right)
            try:
                current = queue.pop(0)
            except IndexError:
                break

        print(" ".join(results))


T = int(input())
myTree = Solution()
root = None
for i in range(T):
    data = int(input())
    root = myTree.insert(root, data)
myTree.levelOrder(root)
