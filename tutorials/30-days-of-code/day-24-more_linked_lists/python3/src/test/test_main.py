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
from challenge.main import LinkedList, Node

unit_test_data = [
    [0, [], [""]],
    [1, [1], ["1"]],
    [2, [1, 2], ["1 2"]],
    [2, [1, 1], ["1"]],
    [3, [1, 2, 1], ["1 2"]],
    [6, [1, 2, 2, 3, 3, 4], ["1 2 3 4"]],
    [6, [4, 3, 3, 2, 2, 1], ["4 3 2 1"]],
    [6, [1, 3, 2, 4, 3, 1], ["1 3 2 4"]],
    [7, [1, 1, 1, 2, 2, 2, 1], ["1 2"]],
]

integration_test_data = unit_test_data


def test_node_class() -> None:
    """Runs the class against all of our test data."""

    number: int = 5
    code: Node = Node(number)
    assert number == code.data

    output_int: int = int(code)
    assert isinstance(output_int, int)
    assert number == output_int

    output_str: str = str(code)
    assert isinstance(output_str, str)
    assert str(number) == output_str


def test_print_results_error(capsys: CaptureFixture) -> None:
    """Runs print_results() before the linked list exists."""

    captured_out: List[str] = []
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    # not running input() or solve() yet, we want to get an error from print_results()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(captured.out.strip())
    expected_out = ["ERROR: linked list not defined."]

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_linkedlist_class(quantity: int, numbers: List[int],
                          expected: List[str], capsys: CaptureFixture) -> None:
    """Runs the class against all of our test data."""

    captured_out: List[str] = []
    expected_out: List[str]

    assert quantity == len(numbers)

    code: LinkedList = LinkedList()
    assert code.head is None

    number: int
    for number in numbers:
        code.insert(number)

    print(f"{list(code)} == {numbers}")
    assert all(o == e for o, e in zip(list(code), numbers))

    code.remove_duplicates()

    expected_int: List[int]
    if len(expected[0]) > 0:
        expected_int = [int(number) for number in expected[0].split(" ")]
    else:
        expected_int = []

    print(f"{list(code)} == {expected_int}")
    assert all(o == e for o, e in zip(list(code), expected_int))

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.display()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(captured.out.strip())
    expected_out = expected

    print(f"captured.out={captured.out}")
    print(f"captured_out={captured_out}")
    print(f"    expected={expected}")
    print(f"expected_out={expected_out}")
    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(quantity: int, numbers: List[int],
                              expected: List[str],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str] = []
    expected_out: List[str]

    code: main.Challenge = main.Challenge(quantity, numbers)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)
                                 ] + [str(number) for number in numbers]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    assert len(code.numbers) == code.quantity
    assert len(code.numbers) == len(numbers)

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(captured.out.strip())
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(quantity: int, numbers: List[int],
                           expected: List[str], capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str] = []
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [str(quantity)
                                 ] + [str(number) for number in numbers]
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity
    assert len(code.numbers) == code.quantity
    assert len(code.numbers) == len(numbers)

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out.append(captured.out.strip())
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script(quantity: int, numbers: List[int], expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{quantity}\n", "utf8")
    program_input += bytes("\n".join([str(number) for number in numbers]),
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

    expected_out = expected

    print(f"   quantity = {quantity}")
    print(f"    numbers = {numbers}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
