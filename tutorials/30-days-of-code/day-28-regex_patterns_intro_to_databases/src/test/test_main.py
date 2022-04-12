#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
from typing import Any, Dict, List
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [
        6,
        [
            "riya riya@gmail.com",
            "julia julia@julia.me",
            "julia sjulia@gmail.com",
            "julia julia@gmail.com",
            "samantha samantha@gmail.com",
            "tanya tanya@gmail.com",
        ],
        ["julia", "julia", "riya", "samantha", "tanya"],
    ],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_method_without_input(quantity: int, data: List[str],
                              expected: List[str],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    line: str = ""
    name: str = ""
    email: str = ""

    database: Dict = {}

    for line in data:
        name, email = line.split(" ")
        database[email] = name

    code: main.Challenge = main.Challenge(quantity, database)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [
            str(quantity),
        ] + data
        code.input_quantity()
        code.input_data()

    assert code.quantity == quantity
    assert code.quantity == len(code.database.keys())
    assert len(data) == len(code.database.keys())

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_method_with_input(quantity: int, data: List[str], expected: List[str],
                           capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [
            str(quantity),
        ] + data
        code.input_quantity()
        code.input_data()

    assert code.quantity == quantity
    assert code.quantity == len(code.database.keys())
    assert len(data) == len(code.database.keys())

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,expected", unit_test_data)
def test_script(quantity: int, data: Dict[str, str],
                expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{quantity}\n", "utf8")
    program_input += bytes("\n".join(data) + "\n", "utf8")

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

    print(f"     quantity = {quantity}")
    print(f"         data = {data}")
    print(f"     expected = {expected}")
    print(f"        input = {program_input!r}")
    print(f"       output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(o == e for o, e in zip(program_out, expected_out))
