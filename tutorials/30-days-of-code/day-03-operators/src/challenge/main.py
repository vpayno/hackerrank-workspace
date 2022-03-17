#!/usr/bin/env python3
"""
HackerRank - 30 Days of Code - Day 03 - Operators
"""


def solve(meal_cost: float, tip_percent: int, tax_percent: int):
    """
    Given the meal price (base cost of a meal), tip percent (the percentage of
    the meal price being added as tip), and tax percent (the percentage of the
    meal price being added as tax) for a meal, find and print the meal's total
    cost. Round the result to the nearest integer.
    """

    tip: float = meal_cost * (tip_percent / 100)
    tax: float = meal_cost * (tax_percent / 100)
    total: float = tip + tax + meal_cost

    # For the challange, solve() prints the total as an integer.
    print(int(round(total, ndigits=0)))


if __name__ == "__main__":
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
