#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
from typing import Any, List
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [[1, 2, 3], [0, 1, 3]],
    [[3, 2, 1], [3, 1, 3]],
    [[3, 1, 2], [2, 1, 3]],
    [[1, 3, 2], [1, 1, 3]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("numbers,expected", unit_test_data)
def test_method_without_input(numbers: List[int], expected: List[int],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    quantity: int = len(numbers)
    expected_swaps: int = expected[0]
    expected_first: int = expected[1]
    expected_last: int = expected[2]

    code: main.Challenge = main.Challenge(quantity, numbers)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [
            str(quantity),
            " ".join([str(number) for number in numbers]),
        ]
        code.input_quantity()
        code.input_numbers()

    assert len(code.numbers) == len(numbers)

    code.solve()

    sorted_numbers = sorted(numbers)
    print(f"{code.numbers} == {sorted_numbers}")
    assert all(o == e for o, e in zip(code.numbers, sorted_numbers))

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [
        f"Array is sorted in {expected_swaps} swaps.",
        f"First Element: {expected_first}",
        f"Last Element: {expected_last}",
    ]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("numbers,expected", unit_test_data)
def test_method_with_input(numbers: List[int], expected: List[int],
                           capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    quantity: int = len(numbers)
    expected_swaps: int = expected[0]
    expected_first: int = expected[1]
    expected_last: int = expected[2]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [
            str(quantity),
            " ".join([str(number) for number in numbers]),
        ]
        code.input_quantity()
        code.input_numbers()

    assert len(code.numbers) == len(numbers)

    code.solve()

    sorted_numbers = sorted(numbers)
    print(f"{code.numbers} == {sorted_numbers}")
    assert all(o == e for o, e in zip(code.numbers, sorted_numbers))

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [
        f"Array is sorted in {expected_swaps} swaps.",
        f"First Element: {expected_first}",
        f"Last Element: {expected_last}",
    ]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("numbers,expected", unit_test_data)
def test_script(numbers: List[int], expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    quantity: int = len(numbers)
    expected_swaps: int = expected[0]
    expected_first: int = expected[1]
    expected_last: int = expected[2]

    program_input: bytes = bytes(f"{quantity}\n", "utf8")
    program_input += bytes(" ".join([str(number) for number in numbers]) + "\n",
                           "utf8")

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
    program_out: List[str] = program_output.split("\n")

    expected_out = [
        f"Array is sorted in {expected_swaps} swaps.",
        f"First Element: {expected_first}",
        f"Last Element: {expected_last}",
    ]

    print(f"      numbers = {numbers}")
    print(f"     expected = {expected}")
    print(f"        input = {program_input!r}")
    print(f"       output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(o == e for o, e in zip(program_out, expected_out))
