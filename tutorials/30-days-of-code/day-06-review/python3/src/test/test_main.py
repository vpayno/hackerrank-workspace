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
from unittest.mock import patch

import mock
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [-1, [], []],
    [0, [], []],
    [1, ["adbecf"], ["abc def"]],
    [2, ["adbecf", "0123456789"], ["abc def", "02468 13579"]],
    [2, ["Hacker", "Rank"], ["Hce akr", "Rn ak"]],
    [2, ["ab", "12"], ["a b", "1 2"]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("input_lines,lines,expected", unit_test_data)
def test_method_without_input(input_lines: int, lines: List[str],
                              expected: List[str],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(lines)

    with mock.patch.object(builtins, "input", lambda: str(input_lines)):
        code.input_number()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = lines
        code.input_string()

    assert mock_input.call_count == 0
    assert code.input_lines == max(input_lines, 0)

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("input_lines,lines,expected", unit_test_data)
def test_method_with_input(input_lines: int, lines: List[str],
                           expected: List[str], capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(input_lines)):
        code.input_number()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = lines
        code.input_string()

    assert mock_input.call_count == code.input_lines
    assert code.input_lines == max(input_lines, 0)

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = expected

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("input_lines,lines,expected", unit_test_data)
def test_script(input_lines: int, lines: List[str],
                expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{input_lines}\n", "utf8")
    program_input += bytes("\n".join(lines), "utf8")

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

    print(f"input_lines = {input_lines}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_output.split("\n"), expected))
