#!/usr/bin/env python3

from typing import Dict


class CalculatorError(Exception):

    def __init__(self, key: str = "generic") -> None:
        self.messages: Dict[str, str] = {}
        self.message: str

        self.messages["generic"] = "generic calculator error"
        self.messages["power"] = "n and p should be non-negative"

        self.message = self.messages.get(key, "generic calculator error")

    def __str__(self) -> str:
        return self.message


class Calculator:

    @staticmethod
    def power(number: int, power: int) -> None:
        if number >= 0 and power >= 0:
            result: int = 1
            for _ in range(0, power):
                result = result * number
        else:
            raise CalculatorError("power")

        return result


myCalculator = Calculator()
T = int(input())
for i in range(T):
    n, p = map(int, input().split())
    try:
        ans = myCalculator.power(n, p)
        print(ans)
    except Exception as e:
        print(e)
