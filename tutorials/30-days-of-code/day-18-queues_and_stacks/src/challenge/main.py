#!/usr/bin/env python3

import sys
from typing import List


class Solution:

    def __init__(self) -> None:
        self.stack: List[str] = []
        self.queue: List[str] = []

    def pushCharacter(self, char: str) -> None:
        """
        Pushes a character onto a stack.

        Read last to first.
        """

        self.stack.append(char)

    def enqueueCharacter(self, char: str) -> None:
        """
        Enqueues a character in the queue.

        Read first to last.
        """

        self.queue.append(char)

    def popCharacter(self) -> str:
        """
        pops and returns the character at the top of the stack.

        Read last to first.
        """

        return self.stack.pop()

    def dequeueCharacter(self) -> str:
        """
        Dequeues and returns the first character in the queue.

        Read first to last.
        """

        return self.queue.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
"""
pop the top character from stack
dequeue the first character from queue
compare both the characters
"""
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
