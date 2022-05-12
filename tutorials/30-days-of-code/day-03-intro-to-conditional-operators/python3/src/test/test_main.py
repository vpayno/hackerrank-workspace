#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import builtins
import os.path
import subprocess
import sys
from typing import Any

import mock
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [3, "Weird"],
    [4, "Not Weird"],
    [7, "Weird"],
    [8, "Weird"],
    [21, "Weird"],
    [22, "Not Weird"],
]

integration_test_data = [
    ["3", "Weird"],
    ["4", "Not Weird"],
    ["7", "Weird"],
    ["8", "Weird"],
    ["21", "Weird"],
    ["22", "Not Weird"],
]


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_with_input(number: int, expected: str,
                           capsys: CaptureFixture) -> None:
    """Runs the main class method against all of our test data."""

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(number)):
        code.input_number()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.solve()
    captured = capsys.readouterr()  # capture code.solve()

    assert code.number == number
    assert code.result == expected

    expected_out: str
    captured_out: str

    expected_out = f"{expected}"

    captured_out = captured.out.strip()

    print(f"{captured_out} == {expected_out}")

    assert captured_out == expected_out


@pytest.mark.parametrize("number,expected", integration_test_data)
def test_script(number: str, expected: str) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{number}", "utf8")

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

    print(f"  number = {number}")
    print(f"expected = {expected}")
    print(f"   input = {program_input!r}")
    print(f"  output = {program_output}")
    print(f"{program_output} == {expected}")

    assert program_output == expected
