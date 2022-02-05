# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 6.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

from collections import Counter
from loguru import logger
from typing import List


def get_input(input_filename: str) -> List[int]:
    """Reads and parses the input file into a list of integers
    >>> get_input("input/06-small.txt")
    [3, 4, 3, 1, 2]
    >>> l = get_input("input/06.txt")
    >>> sum(l)
    769
    >>> len(l)
    300
    """
    with open(input_filename) as f:
        return [int(x) for x in f.read().split(",")]


def count_number_of_lanternfish(fish_array: List[int], number_of_days: int) -> int:
    """Counts the number of lanternfish after a given number of days,
    according given breeding rules.

    Args:
        fish_array: An int array, each representing the internal counter of a lanternfish.
        number_of_days: For how long to run the simulatiom

    Returns:
        The number of lanternfish after the given number of days.

    >>> count_number_of_lanternfish([3,4,3,1,2], 18)
    26
    >>> count_number_of_lanternfish([3,4,3,1,2], 80)
    5934
    """
    c = Counter(fish_array)
    for i in range(number_of_days):
        next_day: Counter[int] = Counter()
        for key in c:
            if key == 0:
                next_day[8] = c[key]
            else:
                next_day[key - 1] = c[key]
            next_day[6] = c[0] + c[7]
        c = next_day
    return sum(c.values())


def part_1(input_filename: str) -> int:
    """Solves part 1 of the day 6 puzzle.

    Args:
        input_filename: The input file to read.

    Returns:
        The number of lanternfish after the given number of days.

    >>> part_1("input/06-small.txt")
    5934
    >>> part_1("input/06.txt")
    360268
    """
    return count_number_of_lanternfish(get_input(input_filename), 80)


def part_2(input_filename: str) -> int:
    """Solves part 2 of the day 6 puzzle.
    Similar to part 1 with more days.
    >>> part_2("input/06.txt")
    1632146183902
    """
    return count_number_of_lanternfish(get_input(input_filename), 256)


if __name__ == "__main__":
    print(part_1("input/06.txt"))
    print(part_2("input/06.txt"))
