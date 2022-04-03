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
from challenge.main import Queue, Stack

unit_test_data = [
    ["racecar", True, "The word, racecar, is a palindrome."],
    ["TacoCat", True, "The word, TacoCat, is a palindrome."],
    ["apple", False, "The word, apple, is not a palindrome."],
    ["orange", False, "The word, orange, is not a palindrome."],
    ["Madam", True, "The word, Madam, is a palindrome."],
]

integration_test_data = unit_test_data


def test_stack_class() -> None:
    """Runs the Stack class."""

    stack: Stack = Stack()

    word: List[str] = list(map(chr, range(ord("a"), ord("z") + 1)))
    letter: str

    for letter in word:
        stack.push_character(letter)

    assert len(stack.stack) == len(word)

    print(f"{stack.stack} == {word}")
    assert all(o == e for o, e in zip(stack.stack, word))

    expected: str
    value: str

    # we pop the word backwards so we need 1 extra step to verify pop
    for expected in word[::-1]:
        value = stack.pop_character()
        print(f"{value} == {expected}")
        assert value == expected

    assert len(stack.stack) == 0


def test_queue_class() -> None:
    """Runs the Queue class."""

    queue: Queue = Queue()

    word: List[str] = list(map(chr, range(ord("a"), ord("z") + 1)))
    letter: str

    for letter in word:
        queue.enqueue_character(letter)

    assert len(queue.queue) == len(word)

    print(f"{queue.queue} == {word}")
    assert all(o == e for o, e in zip(queue.queue, word))

    value: str

    for letter in word:
        value = queue.dequeue_character()
        print(f"{value} == {letter}")
        assert value == letter

    assert len(queue.queue) == 0


@pytest.mark.parametrize("word,expected_bool,expected_str", unit_test_data)
def test_method_without_input(word: str, expected_bool: bool, expected_str: str,
                              capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge(word)

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [word]
        code.input_word()

    assert len(code.word) == len(word)

    code.solve()

    print(f"{code.is_palindrome} == {expected_bool}")
    assert code.is_palindrome == expected_bool

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [expected_str]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("word,expected_bool,expected_str", unit_test_data)
def test_method_with_input(word: str, expected_bool: bool, expected_str: str,
                           capsys: CaptureFixture) -> None:
    """Runs the class methods against all of our test data."""

    captured_out: List[str]
    expected_out: List[str]

    code: main.Challenge = main.Challenge()

    with patch("builtins.input") as mock_input:
        mock_input.side_effect = [word]
        code.input_word()

    assert len(code.word) == len(word)

    code.solve()

    print(f"{code.is_palindrome} == {expected_bool}")
    assert code.is_palindrome == expected_bool

    # discard previous output
    captured: CaptureResult[Any] = capsys.readouterr()
    code.print_results()
    captured = capsys.readouterr()  # capture new output

    captured_out = captured.out.split("\n")
    expected_out = [expected_str]

    print(f"{captured_out} == {expected_out}")
    assert all(o == e for o, e in zip(captured_out, expected_out))


@pytest.mark.parametrize("word,expected_bool,expected_str", unit_test_data)
def test_script(word: List[str], expected_bool: bool,
                expected_str: str) -> None:
    """Runs the main script against all of our test data."""

    program_input: bytes = bytes(f"{word}\n", "utf8")

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

    expected_out = [expected_str]

    # 0 == False, 1 == True
    assert process.returncode == (not expected_bool)

    print(f"         word = {word}")
    print(f"expected_bool = {expected_bool}")
    print(f" expected_str = {expected_str}")
    print(f"        input = {program_input!r}")
    print(f"       output = {program_output}")
    print(f"{program_out} == {expected_out}")

    assert all(o == e for o, e in zip(program_out, expected_out))
