#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
from datetime import datetime
from typing import Any, List
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

# [[return_date, due_date], [fine]],
# date = day, month, year
unit_test_data = [
    [["1 6 2022", "5 6 2022"], [0]],
    [["18 7 2022", "1 6 2022"], [500]],
    [["18 8 2022", "1 6 2022"], [1000]],
    [["9 6 2015", "6 6 2015"], [45]],
    [["8 4 12", "1 1 1"], [10_000]],
    [["1 1 1", "8 8 8"], [0]],
    [["24 10 1776", "10 10 1776"], [210]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("dates,expected", unit_test_data)
def test_method_without_input(dates: List[str], expected: List[int],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int] = []
    expected_out: List[int] = []

    date: List[int]

    date = [int(num) for num in dates[0].split(" ")]
    return_date: datetime = datetime(date[2], date[1], date[0])

    date = [int(num) for num in dates[1].split(" ")]
    due_date: datetime = datetime(date[2], date[1], date[0])

    code: main.Challenge = main.Challenge(return_date, due_date)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = dates

        code.input_return_date()
        code.input_due_date()

    assert code.return_date == return_date
    assert code.due_date == due_date

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(int(captured.out.strip()))
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("dates,expected", unit_test_data)
def test_method_with_input(dates: List[str], expected: List[int],
                           capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int] = []
    expected_out: List[int] = []

    date: List[int]

    date = [int(num) for num in dates[0].split(" ")]
    return_date: datetime = datetime(date[2], date[1], date[0])

    date = [int(num) for num in dates[1].split(" ")]
    due_date: datetime = datetime(date[2], date[1], date[0])

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = dates

        code.input_return_date()
        code.input_due_date()

    assert code.return_date == return_date
    assert code.due_date == due_date

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(int(captured.out.strip()))
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("dates,expected", unit_test_data)
def test_script(dates: List[str], expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes("\n".join(dates) + "\n", "utf8")

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

    expected_out: List[str] = [f"{number}" for number in expected]

    print(f"      dates = {dates}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
