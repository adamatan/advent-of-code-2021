# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 9.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

import sys
from typing import List
from loguru import logger

logger.remove()
logger.add(sys.stderr, level="ERROR")


class MapPoint:
    """
    Represent a single point in a height map.
    Calculates the numeric values of the immediate neighbors.

    >>> heightmap = get_input("input/09-small.txt")
    >>> MapPoint(heightmap, x=0, y=0).neighbours
    [1, 3]
    >>> MapPoint(heightmap, x=9, y=0).neighbours
    [1, 1]
    >>> MapPoint(heightmap, x=2, y=2).neighbours
    [8, 6, 8, 6]
    >>> MapPoint(heightmap, x=6, y=4).neighbours
    [6, 6, 6]
    """

    def __init__(self, heighmap: List[List[int]], x: int, y: int) -> None:
        self.height = heighmap[y][x]
        self.neighbours = []
        x_size = len(heighmap[y])
        y_size = len(heighmap)
        logger.trace(f"x_size: {x_size}, y_size: {y_size}, x: {x}, y: {y}")
        if x > 0:
            self.neighbours.append(heighmap[y][x - 1])
        if x < x_size - 1:
            self.neighbours.append(heighmap[y][x + 1])
        if y > 0:
            self.neighbours.append(heighmap[y - 1][x])
        if y < y_size - 1:
            self.neighbours.append(heighmap[y + 1][x])

    @property
    def neighbors(self) -> List[int]:
        return self.neighbours

    def is_low_point(self) -> bool:
        """"""
        return min(self.neighbours) > self.height


def get_input(input_filename: str) -> List[List[int]]:
    """Read a 2-day array of single-digit ints from a file.
    >>> get_input("input/09-small.txt")[0]
    [2, 1, 9, 9, 9, 4, 3, 2, 1, 0]"""
    with open(input_filename) as f:
        return [[int(x) for x in line.strip()] for line in f.readlines()]


def part_1(input_filename: str) -> int:
    """
    >>> part_1("input/09-small.txt")
    15
    >>> part_1("input/09.txt")
    524"""
    heightmap: List[List[int]] = get_input(input_filename)
    sum_of_low_points: int = 0
    for y in range(len(heightmap)):
        for x in range(len(heightmap[y])):
            mp = MapPoint(heightmap, x, y)
            if mp.is_low_point():
                logger.debug(f"{x:<3}, {y:<3} is a low point")
                sum_of_low_points += mp.height + 1
            else:
                logger.debug(f"{x:<3}, {y:<3} is not a low point")
    return sum_of_low_points


if __name__ == "__main__":
    print(part_1("input/09.txt"))
