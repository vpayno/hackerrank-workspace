#!/usr/bin/env python3
"""
HackerRank - Tutorials - 30 Days of Code - Day 11 - 2D Arrays

Author: Victor Payno (https://github.com/vpayno/hackerrank-workspace)
"""

import sys
from pprint import pprint

# from pprint import pprint
from typing import Any, Dict, List, Optional, Set

from rich.traceback import install

install()


class Challenge:
    """
    Main challenge class.
    """

    def __init__(self,
                 matrix: Optional[List[List[int]]] = None,
                 debug: Optional[bool] = None) -> None:

        self.matrix: List[List[int]]

        self.output: int = 0

        self.debug: bool

        if matrix is not None:
            self.matrix = matrix.copy()
        else:
            self.matrix = []

        if debug is not None:
            self.debug = debug
        else:
            self.debug = False

    def debug_print(self, message: str = "", end: str = "\n") -> None:
        """debug print function"""

        if self.debug:
            print(message, end=end)
        else:
            pass

    def debug_pprint(self, message: Any) -> None:
        """debug prety print function"""

        if self.debug:
            pprint(message)
        else:
            pass

    def input_matrix(self) -> None:
        """
        Read an int matrix without a prompt to keep things interesting.
        """

        if len(self.matrix) <= 0:
            self.debug_print("Enter 6x6 integer matrix:")
            for _ in range(6):
                self.matrix.append(list(map(int, input().rstrip().split())))
            self.debug_print()
        else:
            pass

    def solve(self) -> None:
        """
        Calculate the hourglass sum for every hourglass in matrix,
        then print the maximum hourglass sum.
        """

        hg_sums: Set = set()
        hg_sum: int = 0

        skip_mid_edge_cell: bool = False
        middle_line: bool = False

        hg_collection: Dict[int, List[List[int]]] = {}
        hg_coordinates: List[List[int]] = []

        row_offset: int = 0
        column_offset: int = 0
        row: int = 0
        column: int = 0

        self.debug_print("Found hourglasses:\n")

        for row_offset in range(0, 4):

            for column_offset in range(0, 4):
                hg_sum = 0
                hg_coordinates = []

                for row in range(row_offset, row_offset + 3):

                    if skip_mid_edge_cell and middle_line:
                        self.debug_print(f"        {self.matrix[row][column]} ",
                                         end="")
                        self.debug_print(f"({row},{column_offset + 1}) ",
                                         end="")
                        hg_coordinates.append([row, column_offset + 1])
                        hg_sum += self.matrix[row][column_offset + 1]
                    else:
                        for column in range(column_offset, column_offset + 3):
                            self.debug_print(f"{self.matrix[row][column]} ",
                                             end="")
                            self.debug_print(f"({row},{column}) ", end="")
                            hg_coordinates.append([row, column])
                            hg_sum += self.matrix[row][column]

                    self.debug_print()
                    skip_mid_edge_cell = not skip_mid_edge_cell
                    middle_line = not middle_line

                self.debug_print()
                middle_line = False
                skip_mid_edge_cell = False

                hg_sums.add(hg_sum)
                hg_collection.update({hg_sum: hg_coordinates})

        self.debug_print("hg_sums: ", end="")
        self.debug_pprint(hg_sums)
        self.debug_print()
        self.debug_print("hg_collection:")
        self.debug_pprint(hg_collection)

        self.debug_print()
        self.debug_print("largest sum: ", end="")
        self.output = sorted(list(hg_sums))[-1]

    def print_results(self) -> None:
        """Print the results of the challenge."""

        print(self.output)

    def main(self) -> None:
        """
        Challenge steps.
        """

        self.debug_print("Debuging enabled.\n")

        self.input_matrix()

        self.solve()

        self.print_results()


if __name__ == "__main__":  # pragma: no cover

    DEBUG: bool
    try:
        DEBUG = sys.argv[1] == "--debug"
    except IndexError:
        DEBUG = False

    challenge = Challenge(debug=DEBUG)

    challenge.main()
