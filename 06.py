# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 6.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

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


def count_number_of_lanternfish(fish_array: int, number_of_days: int) -> int:
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
    for j in range(number_of_days):
        for i in range(len(fish_array)):
            if fish_array[i] > 0:
                fish_array[i] -= 1
            else:
                fish_array[i] = 6
                fish_array.append(8)
    return len(fish_array)


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


if __name__ == "__main__":
    print(part_1("input/06.txt"))
