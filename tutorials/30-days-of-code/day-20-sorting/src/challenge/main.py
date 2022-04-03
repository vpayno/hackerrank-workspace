#!/usr/bin/env python3
"""
Day 20 - Bubble Sort
"""

from typing import List

if __name__ == "__main__":
    quantity: int = int(input().strip())
    numbers: List[int] = list(map(int, input().rstrip().split(" ")))

    i: int
    j: int

    num_swaps: int = 0
    first_element: int
    last_element: int

    for i in range(0, len(numbers)):

        for j in range(0, len(numbers) - i - 1):

            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                num_swaps += 1

        if num_swaps == 0:
            break

    first_element = numbers[0]
    last_element = numbers[-1]

    print(f"sorted numbers={numbers}")

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {first_element}")
    print(f"Last Element: {last_element}")
