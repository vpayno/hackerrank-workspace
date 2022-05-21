#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import builtins
import os.path
import subprocess
import sys
from typing import Any, Dict, List
from unittest.mock import patch

import mock
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data = [
    [
        1,
        ["sam 99912222"],
        ["edward", "sam", "harry"],
        ["Not found", "sam=99912222", "Not found"],
    ],
    [
        3,
        ["sam 99912222", "tom 11122222", "harry 12299933"],
        ["sam", "edward", "harry"],
        ["sam=99912222", "Not found", "harry=12299933"],
    ],
    [
        5,
        [
            "sam 99912222",
            "edward 12244433",
            "jane 11122222",
            "harry 12299933",
            "kelly 99913333",
        ],
        ["sam", "tom", "jane", "kelly", "sally", "harry", "john"],
        [
            "sam=99912222",
            "Not found",
            "jane=11122222",
            "kelly=99913333",
            "Not found",
            "harry=12299933",
            "Not found",
        ],
    ],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("quantity,data,names,expected", unit_test_data)
def test_method_with_input(
    quantity: int,
    data: Dict[str, str],
    names: List[str],
    expected: List[str],
    capsys: CaptureFixture,
) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(quantity)):
        code.input_quantity()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = data
        code.input_data()

    with patch("builtins.input") as mock_input:
        names.append("EOF")
        mock_input.side_effect = names
        code.input_names()

    assert code.quantity == max(quantity, 0)

    code.solve()

    assert len(code.output) == len(names) - 1

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"code.output == {code.output}")
    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,data,names,expected", unit_test_data)
def test_script(quantity: int, data: Dict[str, str], names: List[str],
                expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{quantity}\n", "utf8")
    program_input += bytes("\n".join([str(line) for line in data]), "utf8")
    program_input += b"\n"
    program_input += bytes("\n".join([str(line) for line in names]), "utf8")

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

    print(f"   quantity = {quantity}")
    print(f"       data = {data}")
    print(f"      names = {names}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected))
