#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 18 - Queues and Stacks

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import sys
from typing import List

from rich.traceback import install

install()


class Stack:
    """
    Implement a simple stack.
    """

    def __init__(self) -> None:

        self.stack: List[str] = []

    def push_character(self, char: str) -> None:
        """
        Pushes a character onto a stack.

        Read last to first.
        """

        self.stack.append(char)

    def pop_character(self) -> str:
        """
        pops and returns the character at the top of the stack.

        Read last to first.
        """

        return self.stack.pop()


class Queue:
    """
    Implement a simple queue.
    """

    def __init__(self) -> None:

        self.queue: List[str] = []

    def enqueue_character(self, char: str) -> None:
        """
        Enqueues a character in the queue.

        Read first to last.
        """

        self.queue.append(char)

    def dequeue_character(self) -> str:
        """
        Dequeues and returns the first character in the queue.

        Read first to last.
        """

        return self.queue.pop(0)


class Challenge:
    """
    Solution class.
    """

    def __init__(self, word: str = "") -> None:

        self.stack: Stack = Stack()
        self.queue: Queue = Queue()

        self.word: str = word

        self.is_palindrome: bool = True

    def input_word(self) -> None:
        """
        Read an str without a prompt to keep things interesting.
        """

        if self.word == "":
            self.word = input().strip()
        else:
            pass

    def solve(self) -> None:
        """
        Solves the challenge.

        1. push/enqueue all the characters of word to stack
        2. pop the top character from stack
        3. dequeue the first character from queue
        4. compare both the characters
        """

        char: str

        for char in self.word.lower():
            self.stack.push_character(char)
            self.queue.enqueue_character(char)

        for _ in range(len(self.word) // 2):
            if self.stack.pop_character() != self.queue.dequeue_character():
                self.is_palindrome = False
                break

    def print_results(self) -> None:
        """
        Print the challenge results.
        """

        # finally print whether string word is palindrome or not.
        if self.is_palindrome:
            print("The word, " + self.word + ", is a palindrome.")
        else:
            print("The word, " + self.word + ", is not a palindrome.")

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.input_word()

        self.solve()

        self.print_results()

        sys.exit(not self.is_palindrome)


if __name__ == "__main__":  # pragma: no cover

    challenge = Challenge()

    challenge.main()
