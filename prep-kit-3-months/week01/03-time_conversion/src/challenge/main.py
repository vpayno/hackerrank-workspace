#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s: str) -> str:

    hour: int
    minute: int
    second: int
    abbv: str

    morning: bool

    m: re.Match = re.match(r"(\d{2}):(\d{2}):(\d{2})(AM|PM)", s)

    hour, minute, second, abbv = m.groups()

    morning = abbv == "AM"

    if morning:
        if int(hour) == 12:
            hour = "00"
        else:
            pass
    else:
        if int(hour) == 12:
            pass
        else:
            hour = str(int(hour) + 12)

    new_time = f"{hour}:{minute}:{second}"

    return new_time


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
