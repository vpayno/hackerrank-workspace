#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import builtins
import os.path
import subprocess
import sys
from typing import Any, List

import mock
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [3, [6]],
    [6, [720]],
    [9, [362880]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_without_input(number: int, expected: List[int],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge(number)

    with mock.patch.object(builtins, "input", lambda: str(number)):
        code.input_number()

    assert code.number == number

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = [int(number) for number in captured.out.strip().split("\n")]
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_with_input(number: int, expected: List[int],
                           capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(number)):
        code.input_number()

    assert code.number == number

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = [int(number) for number in captured.out.strip().split(" ")]
    expected_out = expected

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_script(number: int, expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{number}\n", "utf8")

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

    print(f"     number = {number}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected))
