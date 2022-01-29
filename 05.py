# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 5.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

import re
from collections import Counter
from typing import List, Tuple, Set
from loguru import logger

def coordinates_to_points(coords: Tuple[Tuple[int]]) -> Tuple[Tuple[int]]:
    """Converts a list of coordinates that define a horizontal or vertical line
    into a tuple of points.
    >>> coordinates_to_points( ((0, 9), (5, 9)) )
    [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
    >>> coordinates_to_points( ((3, 4), (1, 4)) )
    [(1, 4), (2, 4), (3, 4)]
    """
    x1, y1 = coords[0]
    x2, y2 = coords[1]
    x1, x2 = sorted([x1, x2])
    y1, y2 = sorted([y1, y2])
    if x1 == x2:
        return [(x1, y) for y in range(y1, y2 + 1)]
    elif y1 == y2:
        return [(x, y1) for x in range(x1, x2 + 1)]
    else:
        return []


def get_input(input_filename: str) -> List[Tuple[int]]:
    """Reads and parses the input file into a list of tuples, each containing
    two coordinates.
    >>> lines = get_input("input/05-small.txt")
    >>> lines[0]
    ((0, 9), (5, 9))
    """
    with open(input_filename) as f:
        return [parse_line(line) for line in f]


def parse_line(line: str) -> Tuple[Tuple[int]]:
    """Parses a line of input into two coordinate tuples.
    >>> parse_line("0,9 -> 5,9")
    ((0, 9), (5, 9))
    >>> parse_line("1,2 -> 1,10")
    ((1, 2), (1, 10))"""
    coords = re.findall(r"\d+", line)
    coords = [int(coordinate) for coordinate in coords]
    return ((coords[0], coords[1]), (coords[2], coords[3]))

def part_1(input_filename: str) -> int:
    """Solves part 1 of the problem.
    Finds all the coordinates that are touched by more than one line in the input file,
    and returns their count.
    >>> part_1("input/05-small.txt")
    5
    >>> part_1("input/05.txt")
    6311
    """
    # Generate a list of points that are touched by a line
    lines = get_input(input_filename)
    points = []
    for line in lines:
        new_points = coordinates_to_points(line)
        points += new_points
    counter = Counter(points)

    # All the points that appears more than once in the list
    duplicate_points = [i for i in counter.items() if i[1] > 1]
    return(len(duplicate_points))

if __name__ == "__main__":
    print(part_1("input/05.txt"))
