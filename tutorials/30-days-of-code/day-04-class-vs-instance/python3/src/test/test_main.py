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

import mock
import pytest
from _pytest.capture import CaptureFixture, CaptureResult

# Our Project
from challenge import main

unit_test_data_person = [
    [-1, "Age is not valid, setting age to 0.\nYou are young."],
    [0, "You are young."],
    [7, "You are young."],
    [11, "You are young."],
    [12, "You are young."],
    [13, "You are a teenager."],
    [14, "You are a teenager."],
    [17, "You are a teenager."],
    [18, "You are old."],
    [19, "You are old."],
    [29, "You are old."],
]

unit_test_data = [
    [1, -1, "Age is not valid, setting age to 0.\nYou are young."],
    [1, 0, "You are young."],
    [1, 7, "You are young."],
    [1, 11, "You are young."],
    [1, 12, "You are young."],
    [1, 13, "You are a teenager."],
    [1, 14, "You are a teenager."],
    [1, 17, "You are a teenager."],
    [1, 18, "You are old."],
    [1, 19, "You are old."],
    [1, 29, "You are old."],
]

integration_test_data = [[
    4,
    [-1, 10, 16, 18],
    [
        "Age is not valid, setting age to 0.",
        "You are young.",
        "You are young.",
        "",
        "You are young.",
        "You are a teenager.",
        "",
        "You are a teenager.",
        "You are old.",
        "",
        "You are old.",
        "You are old.",
        "",
    ],
]]


@pytest.mark.parametrize("age,expected", unit_test_data_person)
def test_class_person(age: int, expected: str, capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()

    code: main.Person = main.Person(age)

    expected_out: List[str]
    captured_out: List[str]

    code.am_i_old()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected.split("\n")

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))

    age = max(age, 0)

    assert code.age == age

    for _ in range(0, 5):
        code.year_passes()
        age += 1
        assert code.age == age


@pytest.mark.parametrize("test_cases,age,expected", unit_test_data)
def test_method_with_input(test_cases: int, age: int, expected: str,
                           capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()

    code: main.Challenge = main.Challenge()
    person: main.Person = main.Person(age)

    expected_out: List[str]
    captured_out: List[str]

    with mock.patch.object(builtins, "input", lambda: str(test_cases)):
        code.input_test_cases()

    with mock.patch.object(builtins, "input", lambda: str(age)):
        code.input_age()

    person.am_i_old()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected.split("\n")

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))

    assert code.test_cases == test_cases

    assert code.age == age


@pytest.mark.parametrize("test_cases,ages,expected", integration_test_data)
def test_script(test_cases: int, ages: List[int], expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(
        f"{test_cases}\n" + "\n".join([str(number) for number in ages]), "utf8")

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

    print(f"test_cases = {test_cases}")
    print("ages = " + ",".join([str(number) for number in ages]))
    print(f"expected = {expected}")
    print(f"   input = {program_input!r}")
    print(f"  output = {program_output}")
    print(f"{program_output} == {expected}")

    assert all(e == o for e, o in zip(program_output.split("\n"), expected))
