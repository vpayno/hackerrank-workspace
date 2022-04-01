#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
from typing import List
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

# Our Project
from challenge import main

unit_test_data = [
    [
        [
            [1, 1, 1, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0],
        ],
        [19],
    ],
    [
        [
            [7, 6, 8, 2, 4, 3],
            [7, 3, 3, 0, 6, 1],
            [3, 8, 7, 7, 2, 2],
            [0, 8, 6, 8, 6, 1],
            [7, 1, 6, 0, 2, 4],
            [2, 7, 8, 1, 7, 4],
        ],
        [44],
    ],
]

integration_test_data = unit_test_data


def test_debug_print(capsys: CaptureFixture) -> None:
    """Tests the debug_print() method."""

    captured_out: List[str]
    expected_out: List[str] = ["debug output"]
    input_data: str = "debug output"

    code: main.Challenge = main.Challenge(debug=True)

    assert code.debug == True

    # captured = capsys.readouterr()  # discard previous output
    code.debug_print(input_data)
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


def test_debug_pprint(capsys: CaptureFixture) -> None:
    """Tests the debug_print() method."""

    captured_out: List[str]
    expected_out: List[str] = ["'debug output'"]
    input_data: str = "debug output"

    code: main.Challenge = main.Challenge(debug=True)

    assert code.debug == True

    # captured = capsys.readouterr()  # discard previous output
    code.debug_pprint(input_data)
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("matrix,expected", unit_test_data)
def test_method_without_input(matrix: List[List[int]], expected: List[int],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge(matrix=matrix, debug=True)

    assert code.debug == True

    str_matrix: List[List[str]] = [
        [str(number) for number in line] for line in matrix
    ]
    str_list: List[str] = [" ".join(line) for line in str_matrix]

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = str_list
        code.input_matrix()

    assert mock_input.call_count == 0
    assert len(code.matrix) == len(matrix)

    code.solve()

    # compare input and output matricies
    assert all([o == e
                for o, e in zip(line_out, line_exp)]
               for line_out, line_exp in zip(code.matrix, matrix))

    # captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    # we want the int from the last line "largest sum: int\n"
    captured_out = [int(captured.out.strip().split("\n")[-1].split(" ")[-1])]
    expected_out = expected

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("matrix,expected", unit_test_data)
def test_method_with_input(matrix: List[List[int]], expected: List[int],
                           capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge()

    assert code.debug == False

    str_matrix: List[List[str]] = [
        [str(number) for number in line] for line in matrix
    ]
    str_list: List[str] = [" ".join(line) for line in str_matrix]

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = str_list
        code.input_matrix()

    assert mock_input.call_count == 6
    assert len(code.matrix) == len(matrix)

    code.solve()

    # compare input and output matricies
    assert all([o == e
                for o, e in zip(line_out, line_exp)]
               for line_out, line_exp in zip(code.matrix, matrix))

    # captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = [int(number) for number in captured.out.strip().split("\n")]
    expected_out = expected

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("matrix,expected", unit_test_data)
def test_script(matrix: List[List[int]], expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    str_matrix: List[List[str]] = [
        [str(number) for number in line] for line in matrix
    ]
    str_list: List[str] = [" ".join(line) for line in str_matrix]

    program_input: bytes = bytes("\n".join(str_list), "utf8")

    process: subprocess.CompletedProcess = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "main.py"),
        ],
        check=False,
        input=program_input,
        stdout=subprocess.PIPE,
    )

    program_output: str = process.stdout.decode("utf-8").strip()
    program_out: List[int] = [
        int(number) for number in program_output.split(" ")
    ]

    print(f"     matrix = {matrix}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(o == e for o, e in zip(program_out, expected))
