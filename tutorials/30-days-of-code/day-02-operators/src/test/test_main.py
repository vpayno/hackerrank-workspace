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
from typing import List

import mock
import pytest

# Our Project
from challenge import main

unit_test_data = [
    [12.0, 20, 8, 15],
    [15.50, 15, 10, 19],
    [1234.56, 17, 11, 1580],
    [123.45, 13, 7, 148],
]

integration_test_data = [
    [["12.00", "20", "8"], "15"],
    [["15.50", "15", "10"], "19"],
]


@pytest.mark.parametrize("meal_cost,tip_percent,tax_percent,expected",
                         unit_test_data)
def test_method_with_input(meal_cost: float, tip_percent: int, tax_percent: str,
                           expected: int, capsys):
    """Runs the main class method against all of our test data."""

    getcontext().prec = 2

    decimal1: Decimal
    decimal2: Decimal

    code: main.Challenge = main.Challenge(debug=True)

    with mock.patch.object(builtins, "input", lambda: str(meal_cost)):
        code.input_meal_cost()

    with mock.patch.object(builtins, "input", lambda: str(tip_percent)):
        code.input_tip_percent()

    with mock.patch.object(builtins, "input", lambda: str(tax_percent)):
        code.input_tax_percent()

    decimal1 = Decimal(code.meal_cost) / Decimal(1)
    decimal2 = Decimal(meal_cost) / Decimal(1)
    print(f"{decimal1} == {decimal2}")
    assert decimal1 == decimal2

    print(f"{code.tip_percent} == {tip_percent}")
    assert code.tip_percent == tip_percent

    print(f"{code.tax_percent} == {tax_percent}")
    assert code.tax_percent == tax_percent

    captured = capsys.readouterr()  # discard previous output
    code.debug = False
    code.solve()
    captured = capsys.readouterr()  # capture code.solve()
    print(f"{captured.out.strip()} == {expected}")
    assert captured.out.strip() == str(expected)

    expected_tip: float = (code.tip_percent / 100) * code.meal_cost
    print(f"{code.tip:.2f} == {expected_tip:.2f}")
    assert f"{code.tip:.2f}" == f"{expected_tip:.2f}"

    decimal1 = Decimal(code.tax) / Decimal(1)
    decimal2 = Decimal((code.tax_percent / 100) * code.meal_cost) / Decimal(1)
    print(f"{decimal1} == {decimal2}")
    assert decimal1 == decimal2

    decimal1 = Decimal(code.total) / Decimal(1)
    decimal2 = Decimal(code.tip + code.tax + code.meal_cost) / Decimal(1)
    print(f"{decimal1} == {decimal2}")
    assert decimal1 == decimal2

    code.debug = True

    expected_out: List[str]
    captured_out: List[str]

    captured = capsys.readouterr()  # discard previous output
    code.solve()
    captured = capsys.readouterr()  # capture code.solve()
    expected_out = f"""
    Subtotal: ${code.meal_cost:>7,.2f}
         Tip: ${code.tip:>7,.2f} {code.tip_percent:,}%
         Tax: ${code.tax:>7,.2f} {code.tax_percent:,}%
       Total: ${code.total:>7,.2f}
    """.split("\n")
    expected_out = list(filter(str.strip, expected_out))
    captured_out = captured.out.split("\n")
    captured_out = list(filter(str.strip, captured_out))
    print(f"{captured_out} == {expected_out}")
    print(list(zip(expected_out, captured_out)))
    assert all(
        e.strip() == o.strip() for e, o in zip(expected_out, captured_out))


@pytest.mark.parametrize("input_data,expected", integration_test_data)
def test_script(input_data: List[str], expected: str):
    """Runs the main script against all of our test data."""

    print(f"input_data = {input_data}")
    print(f"expected = {expected}")

    process: subprocess.CompletedProcess = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "main.py"),
        ],
        check=False,
        input=bytes("\n".join(input_data), "utf8"),
        stdout=subprocess.PIPE,
    )

    program_output: str = process.stdout.decode("utf-8").strip()
    print(f"{program_output} == {expected}")

    assert program_output == expected
