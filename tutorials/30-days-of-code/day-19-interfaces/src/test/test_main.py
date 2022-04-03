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
from challenge.main import AdvancedArithmetic, Calculator

unit_test_data = [
    [6, 12],
    [20, 42],
    [25, 31],
]

integration_test_data = unit_test_data


def test_interface_exception() -> None:
    """Test to see if an implemented method raises an exception."""

    captured_out: List[str]
    expected_out: List[str] = [""]

    class BadCalculator(AdvancedArithmetic):  # pylint: disable=abstract-method,too-few-public-methods
        """intentionally not imlementing divisor_sum()"""

    calculator: BadCalculator = BadCalculator()

    with pytest.raises(NotImplementedError) as excinfo:
        calculator.divisor_sum(123)

    captured_out = str(excinfo.value).split("\n")

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_calculator_class(number: int, expected: int) -> None:
    """Runs the Calculator class."""

    calculator: Calculator = Calculator()

    result: int = calculator.divisor_sum(number)

    assert result == expected


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_without_input(number: int, expected: int,
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(number)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(number)]
        code.input_number()

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = ["I implemented: AdvancedArithmetic"]
    expected_out += [str(expected)]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_method_with_input(number: int, expected: int,
                           capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(number)]
        code.input_number()

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = ["I implemented: AdvancedArithmetic"]
    expected_out += [str(expected)]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("number,expected", unit_test_data)
def test_script(number: int, expected: int) -> None:
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
    program_out: List[str] = program_output.split("\n")

    expected_out = []
    expected_out.append("I implemented: AdvancedArithmetic")
    expected_out.append(str(expected))

    print(f"       number = {number}")
    print(f"     expected = {expected}")
    print(f"        input = {program_input!r}")
    print(f"       output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(o == e for o, e in zip(program_out, expected_out))
