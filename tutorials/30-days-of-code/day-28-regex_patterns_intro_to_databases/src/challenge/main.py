#!/usr/bin/env python3

import re

if __name__ == "__main__":
    N = int(input().strip())

    database = {}

    names = []

    reo = re.compile(r"^.*@gmail.com$")

    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]

        database[emailID] = firstName

    for email, name in database.items():
        if reo.match(email):
            names.append(name)

    names.sort()

    for name in names:
        print(f"{name}")
