#!/bin/python3
"""
https://www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import collections
import sys
from typing import List, Optional, OrderedDict


class Challenge:
    """
    Week 1 - Plus Minus
    """

    def __init__(self):
        """
        Set the precision to 6.
        """

    def __str__(self) -> str:
        """
        String representation of the class.
        """

        return self.__class__.__name__

    def plusMinus(self, arr: Optional[List[int]]) -> List[float]:
        """
        Given an array of integers, calculate the ratios of its elements
        that are positive, negative, and zero. Print the decimal value of
        each fraction on a new line with 6 places after the decimal.
        """
        # pylint: disable=invalid-name,no-self-use

        # added in-line if to fix:
        # error: Argument 1 to "len" has incompatible type "Optional[List[int]]"; expected "Sized"
        size: int = len(arr) if arr is not None else 0

        counter: OrderedDict[str, int] = collections.OrderedDict({
            "positive": 0,
            "negative": 0,
            "zero": 0
        })

        result: List[float] = []

        number: float = 0.0

        # added or [] to fix:
        # error: Item "None" of "Optional[List[int]]" has no attribute "__iter__" (not iterable)
        for number in arr or []:
            if number > 0:
                counter["positive"] += 1
            elif number < 0:
                counter["negative"] += 1
            else:
                counter["zero"] += 1

        for _, value in counter.items():
            result.append(value / size)

        for number in result:
            print(f"{number:.6f}")

        return result


if __name__ == "__main__":  # pragma: nocover
    input_size: Optional[int] = None if sys.argv[1] is None else int(
        sys.argv[1])
    user_input: Optional[List[int]] = (None if sys.argv[2] is None else
                                       [int(_) for _ in sys.argv[2].split(" ")])

    length: Optional[int] = 0
    array: Optional[List[int]] = []

    if not input_size and not user_input:
        length = int(input().strip())
        array = list(map(int, input().rstrip().split()))
    else:
        length = input_size
        array = user_input

    program = Challenge()

    output: List[float] = program.plusMinus(array)
