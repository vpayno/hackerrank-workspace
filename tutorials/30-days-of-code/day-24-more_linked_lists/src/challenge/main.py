#!/usr/bin/env python3
"""
Day 24: More Linked Lists
"""


class Node:  # pylint: disable=too-few-public-methods
    """
    Node class
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    """
    Challenge solution
    """

    @staticmethod
    def insert(head, data):
        """
        Inserts a node into a linked list.
        """

        p = Node(data)

        if head == None:
            head = p
        elif head.next == None:
            head.next = p
        else:
            start = head
            while start.next != None:
                start = start.next
            start.next = p

        return head

    @staticmethod
    def display(head):
        """
        Print the linked list.
        """

        current = head

        while current:
            print(current.data, end=" ")
            current = current.next

    @staticmethod
    def removeDuplicates(head):
        """
        Remove duplicates from a node list.
        """

        items = []

        current = head
        previous = None

        while current:
            # print(f"examinig {current.data}")

            if current.data in items:
                # print("removing duplicate")
                previous.next = current.next
            else:
                # print("adding number to items")
                items.append(current.data)
                previous = current

            current = current.next

        return head


mylist = Solution()
T = int(input())
head = None

for i in range(T):
    data = int(input())
    head = mylist.insert(head, data)

head = mylist.removeDuplicates(head)
mylist.display(head)
