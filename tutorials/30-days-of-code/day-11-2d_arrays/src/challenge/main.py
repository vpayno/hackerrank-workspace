#!/bin/python3
"""
Day 11 - 2D Arrays
"""

# from pprint import pprint
from typing import Dict, List, Set


def solve(matrix: List[List[int]]):
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

    for row_offset in range(0, 4):

        for column_offset in range(0, 4):
            hg_sum = 0
            hg_coordinates = []

            for row in range(row_offset, row_offset + 3):

                if skip_mid_edge_cell and middle_line:
                    # print(f"        {matrix[row][column]} ", end="")
                    # print(f"({row},{column_offset + 1}) ", end="")
                    hg_coordinates.append([row, column_offset + 1])
                    hg_sum += matrix[row][column_offset + 1]
                else:
                    for column in range(column_offset, column_offset + 3):
                        # print(f"{matrix[row][column]} ", end="")
                        # print(f"({row},{column}) ", end="")
                        hg_coordinates.append([row, column])
                        hg_sum += matrix[row][column]

                # print()
                skip_mid_edge_cell = not skip_mid_edge_cell
                middle_line = not middle_line

            # print()
            middle_line = False
            skip_mid_edge_cell = False

            hg_sums.add(hg_sum)
            hg_collection.update({hg_sum: hg_coordinates})

    # pprint(hg_sums)
    # pprint(hg_collection)
    print(sorted(list(hg_sums))[-1])


if __name__ == "__main__":

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    # pprint(arr)

    solve(arr)
