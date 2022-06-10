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
from typer.testing import CliRunner

# Our Project
from challenge import main

app = main.app

unit_test_data = [
    [1, [1], ["Not prime"]],
    [2, [1, 2], ["Not prime", "Prime"]],
    [3, [1, 2, 3], ["Not prime", "Prime", "Prime"]],
    [5, [1, 2, 3, 4, 5], ["Not prime", "Prime", "Prime", "Not prime", "Prime"]],
]

integration_test_data = unit_test_data


def test_typer_cli_benchmark() -> None:
    """Test the Typer cli related code. (command => benchmark)"""

    runner: CliRunner = CliRunner()

    result = runner.invoke(app, ["benchmark"])

    assert result.exit_code == 0
    assert "Polynomial: time" in result.output


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_typer_cli_test_with_arguments(
    quantity: int,
    numbers: List[int],
    expected: List[str],
) -> None:
    """Test the Typer cli related code. (command => test)"""

    assert quantity == len(numbers)

    runner: CliRunner = CliRunner()

    number_string: str = " ".join([f"{number}" for number in numbers])

    result = runner.invoke(app, ["test", "--numbers", number_string])

    captured_out: List[str] = result.output.strip().split("\n")
    expected_out: List[str] = expected

    print(f"{result.output}")
    assert 0 == result.exit_code
    assert quantity == len(captured_out)
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_typer_cli_test_with_stdin(
    quantity: int,
    numbers: List[int],
    expected: List[str],
) -> None:
    """Test the Typer cli related code. (command => test)"""

    assert quantity == len(numbers)

    std_input: str = f"{quantity}\n"
    std_input += "\n".join([f"{number}" for number in numbers]) + "\n"

    print(f"std_input={std_input}")

    runner: CliRunner = CliRunner()

    # result = runner.invoke(app, ["test"], input="1\n7\n")
    result = runner.invoke(app, ["test", "--numbers", "-"], input=std_input)

    captured_out: List[str] = result.output.strip().split("\n")
    expected_out: List[str] = expected

    print(f"result.output={result.output}")
    print(f"{captured_out} == {expected_out}")
    assert 0 == result.exit_code
    assert quantity == len(captured_out)
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_without_input(
    quantity: int,
    numbers: List[int],
    expected: List[str],
    capsys: CaptureFixture,
) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(quantity, numbers)

    input_lines: List[str] = []
    number: int

    input_lines.append(f"{quantity}")
    for number in numbers:
        input_lines.append(f"{number}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_method_with_input(
    quantity: int,
    numbers: List[int],
    expected: List[str],
    capsys: CaptureFixture,
) -> None:
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    input_lines: List[str] = []
    number: int

    input_lines.append(f"{quantity}")
    for number in numbers:
        input_lines.append(f"{number}")

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = input_lines
        code.input_quantity()
        code.input_numbers()

    assert code.quantity == quantity

    code.solve()

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    print(f"captured.out == {captured.out}")
    captured_out = captured.out.strip().split("\n")
    expected_out = expected

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.fixture
def expected_data_from_file() -> List[str]:
    """Returns expected data from a file."""

    with open("resources/test-data/test-data-01-expected.txt",
              "r",
              encoding="utf-8") as file:
        expected_data: List[str] = file.readlines()

    return expected_data


@pytest.fixture
def input_data_from_file() -> List[str]:
    """Returns input data from a file."""

    with open("resources/test-data/test-data-01-inputs.txt",
              "r",
              encoding="utf-8") as file:
        input_data: List[str] = file.readlines()

    return input_data


# pylint is complaining about the figure names in the function signature.
# pylint: disable=redefined-outer-name
def test_script_with_file_fixtures(input_data_from_file: List[str],
                                   expected_data_from_file: List[str]) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes()

    line: str
    for line in input_data_from_file:
        program_input += bytes(f"{line}", "utf8")

    assert program_input != b""

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

    # Remove new lines from file input since our captured -> List[str] input losses them.
    expected_out = [number.strip() for number in expected_data_from_file]

    print(f"   quantity = {input_data_from_file[0]}")
    print(f"    numbers = {input_data_from_file[1:3]}...")
    print(f"   expected = {expected_data_from_file[0:3]}...")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))


@pytest.mark.parametrize("quantity,numbers,expected", unit_test_data)
def test_script_with_parametrize(quantity: int, numbers: List[int],
                                 expected: List[str]) -> None:
    """Runs the main script against all of our test data."""

    number: int

    program_input: bytes = bytes(f"{quantity}\n", "utf8")

    for number in numbers:
        program_input += bytes(f"{number}\n", "utf8")

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
    print(f"{program_out} == {expected}")

    assert all(e == o for e, o in zip(program_out, expected_out))
