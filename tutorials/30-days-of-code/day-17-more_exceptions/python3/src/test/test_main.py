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
from challenge.main import Calculator, CalculatorError

unit_test_data = [
    [1, [[2, 4]], ["16"]],
    [
        2,
        [[-1, -2], [-1, 3]],
        ["n and p should be non-negative", "n and p should be non-negative"],
    ],
    [
        3,
        [[3, 5], [-1, -2], [7, 3]],
        ["243", "n and p should be non-negative", "343"],
    ],
    [
        4,
        [[3, 5], [2, 4], [-1, -2], [-1, 3]],
        [
            "243",
            "16",
            "n and p should be non-negative",
            "n and p should be non-negative",
        ],
    ],
]

integration_test_data = unit_test_data


def test_raise_exception() -> None:
    """Test the custom exception."""

    code: main.Calculator = main.Calculator()

    expected_out: List[str] = ["n and p should be non-negative"]

    with pytest.raises(CalculatorError) as excinfo:
        code.power(-1, -1)

    captured_out: List[str] = str(excinfo.value).split("\n")

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


def test_calculator_class() -> None:
    """Runs the Calculator class."""

    code: Calculator = Calculator()

    number: int = 2
    power: int = 4
    expected: int = 16

    result: int

    result = code.power(number, power)

    assert str(result) == str(expected)


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(quantity: int, numbers: List[List[int]],
                              expected: List[str],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(quantity, numbers)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)] + [
            " ".join([str(num) for num in number]) for number in numbers
        ]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    if code.numbers is not None:
        assert len(code.numbers) == code.quantity
        assert len(code.numbers) == len(numbers)
    else:
        pass  # pragma: no cover

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.solve()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(quantity: int, numbers: List[List[int]],
                           expected: List[str], capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)] + [
            " ".join([str(num) for num in number]) for number in numbers
        ]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    if code.numbers is not None:
        assert len(code.numbers) == code.quantity
        assert len(code.numbers) == len(numbers)
    else:
        pass  # pragma: no cover

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.solve()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script(quantity: int, numbers: List[int], expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{quantity}\n", "utf8")

    lines: List[List[str]] = [
        [str(number) for number in line] for line in numbers
    ]

    # this line confuses mypy
    program_input += bytes(
        "\n".join([" ".join(line) for line in lines]) + "\n",
        "utf8",
    )

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
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
