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
from challenge.main import MyBook

unit_test_data = [
    [
        ["The Alchemist", "Paulo Coelho", "248"],
        ["Title: The Alchemist", "Author: Paulo Coelho", "Price: 248"],
    ],
    [
        ["The Book", "First Last", "123"],
        ["Title: The Book", "Author: First Last", "Price: 123"],
    ],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("data,expected", unit_test_data)
def test_method_without_input(data: List[str], expected: List[str],
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    title: str = data[0]
    author: str = data[1]
    price: int = int(data[2])

    mybook: MyBook = MyBook(title, author, price)

    code: main.Challenge = main.Challenge(mybook)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = data
        code.input_book()

    assert mybook.title == title
    assert mybook.author == author
    assert mybook.price == price

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("data,expected", unit_test_data)
def test_method_with_input(data: List[str], expected: List[str],
                           capsys: CaptureFixture) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    title: str = data[0]
    author: str = data[1]
    price: int = int(data[2])

    mybook: MyBook = MyBook(title, author, price)

    code: main.Challenge = main.Challenge()

    # shouldn't do anything (testing else:pass)
    code.print_results()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = data
        code.input_book()

    assert mybook.title == title
    assert mybook.author == author
    assert mybook.price == price

    captured: CaptureResult = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("data,expected", unit_test_data)
def test_script(data: List[str], expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes("\n".join(data), "utf8")

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

    print(f"       data = {data}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
