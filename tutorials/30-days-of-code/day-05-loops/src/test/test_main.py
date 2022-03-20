#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import builtins
import os.path
import subprocess
import sys
from typing import List

import mock
import pytest

# Our Project
from challenge import main

unit_test_data = [
    [-2, [f"-2 * {i} = {-2 * i}" for i in range(1, 11)]],
    [-1, [f"-1 * {i} = {-1 * i}" for i in range(1, 11)]],
    [0, [f"0 * {i} = {0 * i}" for i in range(1, 11)]],
    [1, [f"1 * {i} = {1 * i}" for i in range(1, 11)]],
    [2, [f"2 * {i} = {2 * i}" for i in range(1, 11)]],
    [3, [f"3 * {i} = {3 * i}" for i in range(1, 11)]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_class_person(number: int, expected: List[str], capsys):
    """Runs the class methods against all of our test data."""

    captured = capsys.readouterr()  # discard previous output

    code: main.Challenge = main.Challenge(number)

    captured_out: List[str]
    expected_out: List[str]

    code.solve()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))

    assert code.number == number


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_with_input(number: int, expected: List[str], capsys):
    """Runs the class method against all of our test data."""

    code: main.Challenge = main.Challenge()

    captured_out: List[str]
    expected_out: List[str]

    with mock.patch.object(builtins, "input", lambda: str(number)):
        code.input_number()

    captured = capsys.readouterr()  # discard previous output
    code.solve()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))

    assert code.number == number


@pytest.mark.parametrize("number,expected", integration_test_data)
def test_script(number: int, expected: List[str]):
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

    print(f"   number = {number}")
    print(f"expected = {expected}")
    print(f"   input = {program_input!r}")
    print(f"  output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_output.split("\n"), expected))
