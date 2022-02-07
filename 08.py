# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 7.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

import sys
from collections import Counter
from loguru import logger
from typing import List, Callable


def get_input(input_filename: str) -> List[str]:
    """
    >>> len(get_input("input/08.txt"))
    800
    """
    signals = []
    with open(input_filename) as f:
        for line in f:
            signals += line.split("|")[1].split()
    return signals


def part_1(input_filename: str) -> int:
    """Solves part 1 of the day 6 puzzle.
    >>> part_1("input/08-small.txt")
    26
    >>> part_1("input/08.txt")
    519
    """
    signals = get_input(input_filename)
    distinct_signals = [s for s in signals if len(s) in (2, 3, 4, 7)]
    return len(distinct_signals)


if __name__ == "__main__":
    print(part_1("input/08.txt"))
