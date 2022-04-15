#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
import tempfile
from typing import Any, List
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [3, [(5, 2), (8, 5), (2, 2)], [1, 4, 0]],
]

integration_test_data = unit_test_data


def test_write_output_file() -> None:
    """Tests print_file() output to a temporary file."""

    code: main.Challenge = main.Challenge()

    expected = [1, 2, 3]
    code.output = [1, 2, 3]

    with tempfile.NamedTemporaryFile() as output_file:
        with patch.dict("os.environ", {"OUTPUT_PATH": output_file.name},
                        clear=True):
            code.print_results()

        with open(output_file.name, "r", encoding="utf-8") as reader:
            captured_lines = reader.readlines()

    print(f"captured_lines == {captured_lines}")
    captured_out = [int(number) for number in captured_lines]
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_method_without_input(
    quantity: int,
    data: List[tuple[int, int]],
    expected: List[int],
    capsys: CaptureFixture,
) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge(quantity, data)

    input_lines: List[str] = []
    number: int
    limit: int

    input_lines.append(f"{quantity}")
    for number, limit in data:
        input_lines.append(f"{number} {limit}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_data()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = [int(number) for number in captured.out.strip().split("\n")]
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_method_with_input(
    quantity: int,
    data: List[tuple[int, int]],
    expected: List[int],
    capsys: CaptureFixture,
) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge()

    input_lines: List[str] = []
    number: int
    limit: int

    input_lines.append(f"{quantity}")
    for number, limit in data:
        input_lines.append(f"{number} {limit}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_data()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = [int(number) for number in captured.out.strip().split("\n")]
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_script(quantity: int, data: List[tuple[int, int]],
                expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    number: int
    limit: int

    program_input: bytes = bytes(f"{quantity}\n", "utf8")

    for number, limit in data:
        program_input += bytes(f"{number} {limit}\n", "utf8")

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
        int(number) for number in program_output.split("\n")
    ]

    expected_out = expected

    print(f"   quantity = {quantity}")
    print(f"       data = {data}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected_out))
