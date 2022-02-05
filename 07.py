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


def get_input(input_filename: str) -> List[int]:
    """Same as day 6 - let's move to a shared function."""
    with open(input_filename) as f:
        return [int(x) for x in f.read().split(",")]


def gauss_sum(a, b: int):
    """Returns the sum of the Gauss numbers up to a given distance.
    >>> gauss_sum(1, 0)
    1
    >>> gauss_sum(11, 22)
    66
    """
    distance = abs(a - b)
    return distance * (distance + 1) // 2


def calculate_minimal_cost(
    crab_positions: List[int], distance_function: Callable[[int, int], int]
) -> int:
    """Calculates the minimal cost of a set of crabs, given a distance function."""
    minimal_cost: int = sys.maxsize
    for i in range(min(crab_positions), max(crab_positions) + 1):
        cost = sum([distance_function(i, x) for x in crab_positions])
        if cost < minimal_cost:
            minimal_cost = cost
    return minimal_cost


def part_1(input_filename: str) -> int:
    """Solves part 1 of the day 6 puzzle.

    Args:
        input_filename: The input file to read.

    Returns:
        The cheapest fuel cost of the crabs.

    >>> part_1("input/07-small.txt")
    37

    A less readable version is:
        costs = {
        i: sum([abs(i - x) for x in crab_positions])
        for i in range(min(crab_positions), max(crab_positions) + 1)
    }
    return min(costs.values())
    """
    crab_positions = get_input(input_filename)
    return calculate_minimal_cost(crab_positions, lambda a, b: abs(a - b))


def part_2(input_filename: str) -> int:
    """Solves part 2 of the day 6 puzzle.

    Args:
        input_filename: The input file to read.

    Returns:
        The cheapest fuel cost of the crabs.

    >> part_2("input/07.txt")
    99540554
    """
    crab_positions = get_input(input_filename)
    return calculate_minimal_cost(crab_positions, gauss_sum)


if __name__ == "__main__":
    print(part_1("input/07.txt"))
    print(part_2("input/07.txt"))
