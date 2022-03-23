#!/usr/bin/env python
"""
Day 08: Dictionaries and Maps
"""

from typing import Dict, List

input_quantity: int = 0
input_dict: Dict[str, str] = {}
input_names: List[str] = []

input_quantity = int(input())
# print(f"{input_quantity}")

name: str
value: str

for _ in range(0, input_quantity):
    name, value = input().strip().split(" ")
    input_dict[name] = value.strip()

# print(f"{input_dict}")

while True:
    try:
        name = input().strip()
        input_names.append(name)
    except EOFError:
        break

# print(f"{input_names}")

for name in input_names:
    try:
        value = input_dict[name]
        print(f"{name}={value}")
    except KeyError:
        print("Not found")
