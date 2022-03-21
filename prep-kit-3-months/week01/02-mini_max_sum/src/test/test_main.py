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
    [[], [0, 0]],
    [[-7, -5, -3, -1], [(-7 + -5 + -3), (-5 + -3 + -1)]],
    [[-3, -2, -1, 0, 1, 2, 3],
     [(-3 + -2 + -1 + 0 + 1 + 2), (-2 + -1 + 0 + 1 + 2 + 3)]],
    [[-1, 1, 3, 5, 7, 11, 17],
     [(-1 + 1 + 3 + 5 + 7 + 11), (1 + 3 + 5 + 7 + 11 + 17)]],
    [
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [(0 + 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8),
         (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)],
    ],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("numbers,expected", unit_test_data)
def test_method_without_input(numbers: List[int], expected: List[int]):
    """Runs the challenge class method against all of our test data."""

    number1: int
    number2: int

    code: main.Challenge = main.Challenge(numbers)

    for number1, number2 in zip(code.numbers, numbers):
        print(f"{number1} == {number2}")
        assert number1 == number2

    print(f"{code.slice_size} == {len(numbers) - 1}")
    assert code.slice_size == max(len(numbers) - 1, 0)

    with mock.patch.object(
            builtins, "input",
            lambda: " ".join([str(number) for number in numbers or []])):
        code.input_numbers()

    for number1, number2 in zip(code.numbers, numbers):
        print(f"{number1} == {number2}")
        assert number1 == number2

    print(f"{code.slice_size} == {len(numbers) - 1}")
    assert code.slice_size == max(len(numbers) - 1, 0)

    code.min_max_sum()

    for number1, number2 in zip([*code.results], expected):
        print(f"{number1} == {number2}")
        assert number1 == number2


@pytest.mark.parametrize("numbers,expected", unit_test_data)
def test_method_with_input(numbers: List[int], expected: List[int]):
    """Runs the main class method against all of our test data."""

    number1: int
    number2: int

    code: main.Challenge = main.Challenge()

    print(f"{code.numbers} == []")
    assert len(code.numbers) == len([])

    print(f"{code.slice_size} == 0")
    assert code.slice_size == 0

    # It should not do anything since we already have the numbers list.
    with mock.patch.object(
            builtins, "input",
            lambda: " ".join([str(number) for number in numbers or []])):
        code.input_numbers()

    for number1, number2 in zip(code.numbers, numbers):
        print(f"{number1} == {number2}")
        assert number1 == number2

    print(f"{code.slice_size} == {len(numbers) - 1}")
    assert code.slice_size == max(len(numbers) - 1, 0)

    code.min_max_sum()

    for number1, number2 in zip(code.results, expected):
        print(f"{number1} == {number2}")


def test_script_arguments():
    """Test script command line argument input."""

    number1: int
    number1: int

    sys.argv = ["script", "0", "1", "2", "3"]

    numbers: List[int] = main.get_cmdline_arguments()
    expected: List[int] = [int(number) for number in sys.argv[1:]]

    for number1, number2 in zip(numbers, expected):
        print(f"{number1} == {number2}")
        assert number1 == number2


@pytest.mark.parametrize("numbers,expected", integration_test_data)
def test_script(numbers: List[int], expected: List[int]):
    """Runs the main script against all of our test data."""

    input_data: bytes = bytes(" ".join([str(number) for number in numbers]),
                              "utf8")

    if input_data == b"":
        input_data = b"\n"

    print(f"input={input_data!r}")

    process: subprocess.CompletedProcess = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "main.py"),
        ],
        input=input_data,
        check=False,
        stdout=subprocess.PIPE,
    )

    program_out: str = process.stdout.decode("utf-8").strip()
    expected_out: str = " ".join([str(number) for number in expected])

    print(f"{program_out} == {expected_out}")
    assert program_out == expected_out
