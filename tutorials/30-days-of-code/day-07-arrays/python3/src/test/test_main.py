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
    [4, [1, 4, 3, 2], [2, 3, 4, 1]],
    [6, [1, -1, 3, 7, 4, 1], [1, 4, 7, 3, -1, 1]],
]

integration_test_data = unit_test_data


def test_raise_exception() -> None:
    """Test the custom exception."""
    code: main.Challenge = main.Challenge()

    code.quantity = 1
    code.numbers = [1, 2, 3]

    expected_out: List[str] = [
        f"quantity={code.quantity} != len(numbers)={len(code.numbers)}",
        "Quantity of numbers in 2nd input doesn't match the quantity described in the 1st input.",
    ]

    with pytest.raises(main.InputDoesNotMatchQuantityException) as excinfo:
        # Won't call input since code.numbers is already set, we are just testing
        # the if block after that.
        code.input_numbers()

    captured_out: List[str] = str(excinfo.value).split("\n")

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(quantity: int, numbers: List[int],
                              expected: List[int],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge(numbers)

    with mock.patch.object(builtins, "input", lambda: str(quantity)):
        code.input_quantity()

    assert code.quantity == max(quantity, 0)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [" ".join([str(number) for number in numbers])]
        code.input_numbers()

    assert mock_input.call_count == 0
    assert len(code.numbers) == len(numbers)

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = [int(number) for number in captured.out.strip().split(" ")]
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(quantity: int, numbers: List[int],
                           expected: List[int], capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[int]
    expected_out: List[int]

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(quantity)):
        code.input_quantity()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [" ".join([str(number) for number in numbers])]
        code.input_numbers()

    assert mock_input.call_count == 1
    assert code.quantity == max(quantity, 0)

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


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script(quantity: int, numbers: List[int], expected: List[int]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{quantity}\n", "utf8")
    program_input += bytes(" ".join([str(number) for number in numbers]),
                           "utf8")

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

    print(f"   quantity = {quantity}")
    print(f"    numbers = {numbers}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected))
