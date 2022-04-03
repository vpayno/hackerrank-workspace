#!/usr/bin/env python3

from typing import List


class AdvancedArithmetic(object):

    def divisorSum(self, n: int) -> int:
        raise NotImplementedError


class Calculator(AdvancedArithmetic):

    def divisorSum(self, n: int) -> int:

        number: int = n
        multiples: List[int] = []

        for divisor in range(1, number + 1):
            if number % divisor == 0:
                multiples.append(divisor)

        return sum(multiples)


n: int = int(input())
my_calculator: Calculator = Calculator()
s: int = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
