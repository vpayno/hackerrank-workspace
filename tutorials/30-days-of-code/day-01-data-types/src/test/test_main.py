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
from typing import List, Union

import mock
import pytest

# Our Project
from challenge import main

unit_test_data = [
    [
        5,
        5.0,
        "is a learning and testing site.",
        [9, 9.0, "HackerRank is a learning and testing site."],
    ],
    [
        12,
        4.0,
        "is the best place to learn and practice coding!",
        [16, 8.0, "HackerRank is the best place to learn and practice coding!"],
    ],
]

integration_test_data = [
    [
        b"12\n4.0\nis the best place to learn and practice coding!",
        [
            "16", "8.0",
            "HackerRank is the best place to learn and practice coding!"
        ],
    ],
]


def test_class_str():
    """Runs tests against __str__()"""

    assert main.Challenge().__str__() == "4 4.0 HackerRank "


@pytest.mark.parametrize("int2,double2,str2,expected", unit_test_data)
def test_method_with_input(int2: int, double2: float, str2: str,
                           expected: List[Union[int, float, str]]):
    """Runs the main class method against all of our test data."""

    getcontext().prec = 6

    decimal1: Decimal
    decimal2: Decimal

    code: main.Challenge = main.Challenge()

    with mock.patch.object(builtins, "input", lambda: str(int2)):
        code.input_int()

    with mock.patch.object(builtins, "input", lambda: str(double2)):
        code.input_float()

    with mock.patch.object(builtins, "input", lambda: str(str2)):
        code.input_str()

    print(f"{code.int1 + code.int2} == {expected[0]}")
    assert (code.int1 + code.int2) == expected[0]

    decimal1 = Decimal(code.double1 + code.double2) / Decimal(1)
    decimal2 = Decimal(expected[1]) / Decimal(1)
    print(f"{decimal1} == {decimal2}")
    assert decimal1 == decimal2

    print(f"{code.str1 + code.str2} == {expected[2]}")
    assert (code.str1 + code.str2) == expected[2]


@pytest.mark.parametrize("input_data,expected", integration_test_data)
def test_script(input_data: bytes, expected: List[str]):
    """Runs the main script against all of our test data."""

    process: subprocess = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "main.py"),
        ],
        check=False,
        input=input_data,
        stdout=subprocess.PIPE,
    )

    print(f"{process.stdout.decode('utf-8')} == {expected}")
    program_output: List[str] = process.stdout.decode("utf-8")

    assert expected[0] in program_output
    assert expected[1] in program_output
    assert expected[2] in program_output

    assert all(e == o for e, o in zip(expected, program_output.split("\n")))
