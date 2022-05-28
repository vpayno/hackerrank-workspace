#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import os.path
import subprocess
import sys
from typing import List
from unittest.mock import patch

import pytest

# Our Project
from challenge import main
from challenge.main import Difference

unit_test_data = [
    [3, [1, 2, 5], [4]],
    [5, [8, 8, 8, 8, 8], [0]],
    [5, [8, 19, 3, 2, 7], [17]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_difference_class(quantity: int, numbers: List[int],
                          expected: List[int]):
    """Runs the class methods against all of our test data."""

    code: Difference = Difference(numbers)

    code.compute_difference()

    output_int: int = code.maximum_difference

    output_str: str = str(code)
    expected_str: str = f"Largest difference in {numbers} is {output_int}\n"

    assert quantity == len(code.numbers)
    assert all(e == o for e, o in zip(code.numbers, numbers))
    assert all(e == o for e, o in zip([output_int], expected))

    assert output_str == expected_str


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(quantity: int, numbers: List[int],
                              expected: List[int], capsys):
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(quantity, numbers)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)] + [
            " ".join([str(number) for number in numbers])
        ]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    assert len(code.numbers) == code.quantity
    assert len(code.numbers) == len(numbers)

    code.solve()

    # captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [str(number) for number in expected]

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(quantity: int, numbers: List[int],
                           expected: List[int], capsys):
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)] + [
            " ".join([str(number) for number in numbers])
        ]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    assert len(code.numbers) == code.quantity
    assert len(code.numbers) == len(numbers)

    code.solve()

    # captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [str(number) for number in expected]

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script(quantity: int, numbers: List[int], expected: List[int]):
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
    program_out: List[str] = program_output.split("\n")

    expected_out = [str(number) for number in expected]

    print(f"   quantity = {quantity}")
    print(f"    numbers = {numbers}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
