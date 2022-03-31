#!/bin/python3

import math
import os
import random
import re
import sys

# LOL, they include this line that breaks tests because conditionals aren't allowed.
# With every passing day, I'm less impressed with HackerRank.
# i f __name__ == "__main__":

# Not going to bother with pytests for this one.

# Also, why do they keep insisting on importing math, os, random, re, and sys into
# projects?

# Its rediculous that most of their challenges don't promote good coding or
# doing things things the way they should be for a language.

S = input()

try:
    print(int(S))
except ValueError:
    print("Bad String")
