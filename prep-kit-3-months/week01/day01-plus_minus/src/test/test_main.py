#!/usr/bin/env python3
"""
Author: Victor Payno (https://github.com/vpayno)

Challenge Tests
"""

import builtins
import os.path
import subprocess
import sys
from decimal import Decimal, getcontext
from typing import List, Optional

import mock
import pytest

# Our Project
from challenge import main

unit_test_data = [
    [
        5,
        [-1, 1, 1, 0, -1],
        [0.400000, 0.400000, 0.200000],
    ],
    [
        6,
        [-4, 3, -9, 0, 4, 1],
        [0.500000, 0.333333, 0.166667],
    ],
]

integration_test_data = [
    [
        "5",
        "-1 1 1 0 -1",
        [
            "0.400000",
            "0.400000",
            "0.200000",
        ],
    ],
]


def test_class_str():
    """test for the __str__ method that was added because pylint loves to complain"""

    assert main.Challenge().__str__() == "Challenge"


@pytest.mark.parametrize("size,array,expected", unit_test_data)
def test_method_without_input(size: int, array: List[int],
                              expected: List[float]):
    """Runs the challenge class method against all of our test data."""

    float1: float
    float2: float

    code: main.Challenge = main.Challenge()
    result: List[float] = code.plusMinus(array)

    assert size > 0

    for float1, float2 in zip(result, expected):
        print(f"{float1} == {float2}")
        assert f"{float1:.6f}" == f"{float2:.6f}"


@pytest.mark.parametrize("size,array,expected", unit_test_data)
def test_method_with_input(size: str, array: Optional[List[int]],
                           expected: List[float]):
    """Runs the main class method against all of our test data."""

    getcontext().prec = 6

    float1: float
    float2: float
    decimal1: Decimal
    decimal2: Decimal

    code: main.Challenge = main.Challenge()

    result: List[float]

    assert int(size) > 0

    with mock.patch.object(builtins, "input", lambda: size):
        result = code.plusMinus(array)

    for float1, float2 in zip(result, expected):
        decimal1 = Decimal(float1) / Decimal(1)
        decimal2 = Decimal(float2) / Decimal(1)
        print(f"{decimal1} == {decimal2}")
        assert decimal1 == decimal2


@pytest.mark.parametrize("size,array,expected", integration_test_data)
def test_script(size: int, array: str, expected: List[str]):
    """Runs the main script against all of our test data."""

    process: subprocess.CompletedProcess = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "main.py"),
            str(size),
            array,
        ],
        check=False,
        stdout=subprocess.PIPE,
    )

    print(f"{process.stdout.decode('utf-8')} == {expected}")
    program_output: List[str] = process.stdout.decode("utf-8").split("\n")

    assert expected[0] in program_output
    assert expected[1] in program_output
    assert all(e == o for e, o in zip(expected, program_output))
