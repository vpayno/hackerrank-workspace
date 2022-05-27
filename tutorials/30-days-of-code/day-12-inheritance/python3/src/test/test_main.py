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
from challenge.main import Person, Student

unit_test_data = [
    [["Heraldo", "Memelli", "8135627"], [100, 80], ["O"]],
    [["First", "Last", "1234567"], [100, 90, 80], ["O"]],
    [["Jane", "Smith", "2345678"], [100, 90, 80, 70], ["E"]],
    [["John", "Smith", "3456789"], [100, 90, 80, 70, 60], ["E"]],
    [["Kelly", "Zane", "4567890"], [100, 90, 80, 70, 60, 50], ["A"]],
    [["Bill", "Zane", "5678901"], [100, 40], ["A"]],
    [["Melissa", "Clarkson", "6789012"], [100, 30], ["P"]],
    [["Valentina", "Kelly", "7890123"], [100, 10], ["P"]],
    [["Jake", "Tesla", "8901234"], [80, 10], ["D"]],
    [["Bill", "Luna", "9012345"], [70, 10], ["D"]],
    [["Brad", "Zaleska", "0123456"], [60, 10], ["T"]],
]

integration_test_data = unit_test_data


@pytest.mark.parametrize("data,scores,expected", unit_test_data)
def test_method_without_input(data: List[str], scores: List[int],
                              expected: List[int], capsys):
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    first_name: str = data[0]
    last_name: str = data[1]
    id_number: str = data[2]

    person: Person = Person(first_name, last_name, id_number)
    student: Student = Student(first_name, last_name, id_number, scores)

    code: main.Challenge = main.Challenge(student, len(scores))

    with mock.patch.object(builtins, "input", lambda: " ".join(data)):
        code.input_user()

    assert person.first_name == first_name
    assert person.last_name == last_name
    assert person.id_number == id_number

    assert student.first_name == first_name
    assert student.last_name == last_name
    assert student.id_number == id_number
    assert len(student.scores) == len(scores)
    assert all(e == o for e, o in zip(student.scores, scores))

    person_str: str = (
        f"Name: {person.last_name}, {person.first_name} ID: {person.id_number}")
    assert person.__str__() == person_str

    with mock.patch.object(builtins, "input", lambda: str(len(scores))):
        code.input_quantity()

    assert code.quantity == len(scores)

    with mock.patch.object(builtins, "input",
                           lambda: " ".join([str(score) for score in scores])):
        code.input_scores()

    assert code.quantity == len(scores)
    assert all(e == o for e, o in zip(student.scores, scores))

    code.solve()

    # captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.strip().split("\n")
    expected_out = [
        f"Name: {data[1]}, {data[0]}",
        f"ID: {data[2]}",
        f"Grade: {expected[0]}",
    ]

    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("data,scores,expected", unit_test_data)
def test_method_with_input(data: List[str], scores: List[int],
                           expected: List[int], capsys):
    """Runs the class method against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    first_name: str = data[0]
    last_name: str = data[1]
    id_number: str = data[2]

    person: Person = Person(first_name, last_name, id_number)
    student: Student = Student(first_name, last_name, id_number, [])

    code: main.Challenge = main.Challenge()

    # These should do nothing right now. (testing the else:pass)
    code.solve()
    code.print_results()

    with mock.patch.object(builtins, "input", lambda: " ".join(data)):
        code.input_user()

    assert student.first_name == first_name
    assert student.last_name == last_name
    assert student.id_number == id_number
    assert len(student.scores) == 0
    assert all(e == o for e, o in zip(student.scores, scores))

    person_str: str = (
        f"Name: {person.last_name}, {person.first_name} ID: {person.id_number}")
    assert person.__str__() == person_str

    with mock.patch.object(builtins, "input", lambda: str(len(scores))):
        code.input_quantity()

    assert code.quantity == len(scores)

    with mock.patch.object(builtins, "input",
                           lambda: " ".join([str(score) for score in scores])):
        code.input_scores()

    assert code.quantity == len(scores)
    assert all(e == o for e, o in zip(student.scores, scores))

    code.solve()

    captured = capsys.readouterr()  # discard previous output
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [
        f"Name: {data[1]}, {data[0]}",
        f"ID: {data[2]}",
        f"Grade: {expected[0]}",
    ]

    print(f"{captured.out}")
    print(f"{captured_out} == {expected_out}")
    assert all(e == o for e, o in zip(captured_out, expected_out))


@pytest.mark.parametrize("data,scores,expected", unit_test_data)
def test_script(data: str, scores: List[int], expected: List[int]):
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(" ".join(data) + "\n", "utf8")
    program_input += bytes(f"{len(scores)}\n", "utf8")
    program_input += bytes(" ".join([str(score) for score in scores]) + "\n",
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

    expected_out = [
        f"Name: {data[1]}, {data[0]}",
        f"ID: {data[2]}",
        f"Grade: {expected[0]}",
    ]

    print(f"       data = {data}")
    print(f"     scores = {scores}")
    print(f"   expected = {expected}")
    print(f"      input = {program_input!r}")
    print(f"     output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(e == o for e, o in zip(program_out, expected_out))
