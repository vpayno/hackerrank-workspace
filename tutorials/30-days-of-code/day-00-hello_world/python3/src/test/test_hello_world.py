#!/usr/bin/env python3
"""
https://www.hackerrank.com/challenges/30-hello-world/problem

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
from challenge import hello_world

unit_test_data = [
    [
        "Hello pytest!",
        "Let's run some tests!",
        ["Hello pytest!", "Let's run some tests!"],
    ],
]

integration_test_data = [
    [
        "Let's run some tests!",
        ["Hello, World.", "Let's run some tests!"],
    ],
]


def test_class_init():
    """the things we test for 100% coverage without using nocover"""
    program: hello_world.Challenge = hello_world.Challenge(
        greeting="greeting text")
    expected_output: List[str] = ["greeting text", "user input"]
    program_output: List[str] = program.hello_world(input_string="user input")
    # assert len(expected_output) == len(program_output)
    assert all(e == o for e, o in zip(expected_output, program_output))


def test_class_str():
    """test for the __str__ method that was added because pylint loves to complain"""
    assert hello_world.Challenge().__str__() == "Hello, World."
    assert hello_world.Challenge(
        greeting="Hello pytest!").__str__() == "Hello pytest!"


@pytest.mark.parametrize("greeting,input_string,expected", unit_test_data)
def test_method_without_input(greeting: str, input_string: str,
                              expected: List[str]):
    """Runs the hello_world class method against all of our test data."""
    code: hello_world.Challenge = hello_world.Challenge(greeting)
    result: List[str] = code.hello_world(input_string)
    assert result == expected
    assert code.__str__() == " ".join(expected)


@pytest.mark.parametrize("greeting,input_string,expected", unit_test_data)
def test_method_with_input(greeting: str, input_string: str,
                           expected: List[str]):
    """Runs the hello_world class method against all of our test data."""
    code: hello_world.Challenge = hello_world.Challenge(greeting)
    with mock.patch.object(builtins, "input", lambda: input_string):
        result: List[str] = code.hello_world()
    assert result == expected
    assert code.__str__() == " ".join(expected)


@pytest.mark.parametrize("input_string,expected", integration_test_data)
def test_script(input_string: str, expected: List[str]):
    """Runs the hello_world script against all of our test data."""
    process = subprocess.run(
        [
            sys.executable,
            os.path.join(os.path.dirname("src/challenge/"), "hello_world.py"),
            input_string,
        ],
        check=False,
        stdout=subprocess.PIPE,
    )
    print(f"{process.stdout.decode('utf-8')} == {expected}")
    program_output: str = process.stdout.decode("utf-8")
    assert expected[0] in program_output
    assert expected[1] in program_output
    assert all(e == o for e, o in zip(expected, program_output.split("\n")))
