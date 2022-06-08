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
    [0, [], []],
    [6, [3, 5, 4, 7, 2, 1], ["3 2 5 1 4 7"]],
    [
        13,
        [25, 39, 12, 19, 9, 23, 55, 31, 60, 35, 41, 70, 90],
        ["25 12 39 9 19 31 55 23 35 41 60 70 90"],
    ],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(
    quantity: int,
    numbers: List[int],
    expected: List[str],
    capsys: CaptureFixture,
) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(quantity, numbers)

    input_lines: List[str] = []
    number: int

    input_lines.append(f"{quantity}")
    for number in numbers:
        input_lines.append(f"{number}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(
    quantity: int,
    numbers: List[int],
    expected: List[str],
    capsys: CaptureFixture,
) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    input_lines: List[str] = []
    number: int

    input_lines.append(f"{quantity}")
    for number in numbers:
        input_lines.append(f"{number}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script_with_parametrize(quantity: int, numbers: List[int],
                                 expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    number: int

    program_input: bytes = bytes(f"{quantity}\n", "utf8")

    for number in numbers:
        program_input += bytes(f"{number}\n", "utf8")

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

    expected_out = expected

    print(f"   quantity = {quantity}")
    print(f"    numbers = {numbers}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected_out))
