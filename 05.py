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
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])


def coordinates_to_points(p1: Point, p2: Point, with_diagonals=False) -> Set[Point]:
    """Converts a list of coordinates that define a horizontal or vertical line
    into a tuple of points.
    # Horizontal line
    >>> coordinates_to_points( Point(0, 9), Point(5, 9) ) == { Point(0, 9), Point(1, 9), Point(2, 9), Point(3, 9), Point(4, 9), Point(5, 9) }
    True

    # Horizontal line, point with higher x first
    >>> coordinates_to_points( Point(3, 4), Point(1, 4) ) ==  {Point(1, 4), Point(2, 4), Point(3, 4)}
    True

    # Diagonal lines
    >>> coordinates_to_points( Point(0, 0), Point(3, 3), with_diagonals=False)
    set()
    >>> points = coordinates_to_points(Point(0, 0), Point(3, 3), with_diagonals=True)
    >>> points == {Point(0, 0), Point(1, 1), Point(2, 2), Point(3, 3)}
    True

    >>> p1 = coordinates_to_points(Point(0, 0), Point(3, 3), with_diagonals=True)
    >>> p2 = coordinates_to_points(Point(3, 3), Point(0, 0), with_diagonals=True)
    >>> p1 == p2
    True

    # Neither horizontal, vertical, or diagonal
    >>> coordinates_to_points( Point(0, 0), Point(1, 10), with_diagonals=False)
    set()
    >>> coordinates_to_points( Point(0, 0), Point(1, 10), with_diagonals=True)
    set()
    """
    # Vertical line
    if p1.x == p2.x:
        dx = 0
        dy = 1 if p1.y < p2.y else -1
    # Horizontal line
    elif p1.y == p2.y:
        dy = 0
        dx = 1 if p1.x < p2.x else -1
    # Diagonal line
    elif with_diagonals and abs(p1.x - p2.x) == abs(p1.y - p2.y):
        dx = 1 if p1.x < p2.x else -1
        dy = 1 if p1.y < p2.y else -1
    # Neither horizontal, vertical nor diagonal
    else:
        return set()
    points = set()
    p = Point(p1.x, p1.y)
    while p != Point(p2.x, p2.y):
        points.add(p)
        p = Point(p.x + dx, p.y + dy)
    points.add(p)
    return points


def get_input(input_filename: str) -> List[Tuple[Point, Point]]:
    """Reads and parses the input file into a list of tuples, each containing
    two coordinates.
    >>> lines = get_input("input/05-small.txt")
    >>> lines[0]
    (Point(x=0, y=9), Point(x=5, y=9))
    """
    with open(input_filename) as f:
        return [parse_line(line) for line in f]


def parse_line(line: str) -> Tuple[Point, Point]:
    """Parses a line of input into two coordinate tuples.
    >>> parse_line("0,9 -> 5,9")
    (Point(x=0, y=9), Point(x=5, y=9))
    >>> parse_line("1,2 -> 1,10")
    (Point(x=1, y=2), Point(x=1, y=10))"""
    coords = re.findall(r"\d+", line)
    coords = [int(coordinate) for coordinate in coords]
    return (Point(coords[0], coords[1]), Point(coords[2], coords[3]))


def count_points_that_appear_more_than_once(
    input_filename: str, with_diagonal: bool
) -> int:
    """Counts the number of points that appear more than once in the input file.
    with_diagonal: consider diagonal lines as well (for part 2).

    >>> count_points_that_appear_more_than_once("input/05-small.txt", with_diagonal=False)
    5
    >>> count_points_that_appear_more_than_once("input/05.txt", with_diagonal=False)
    6311
    >>> count_points_that_appear_more_than_once("input/05-small.txt", with_diagonal=True)
    12
    >>> count_points_that_appear_more_than_once("input/05.txt", with_diagonal=True)
    19929
    """
    lines = get_input(input_filename)
    points: List[Point] = []
    for line in lines:
        new_points = coordinates_to_points(line[0], line[1], with_diagonal)
        points += new_points
    counter = Counter(points)

    # All the points that appears more than once in the list
    duplicate_points = [i for i in counter.items() if i[1] > 1]
    return len(duplicate_points)


def part_1(input_filename: str) -> int:
    """Solves part 1 of the problem.
    Finds all the coordinates that are touched by more than one line in the input file,
    and returns their count.
    >>> part_1("input/05-small.txt")
    5
    >>> part_1("input/05.txt")
    6311
    """
    return count_points_that_appear_more_than_once(input_filename, with_diagonal=False)


def part_2(input_filename: str) -> int:
    """Solves part 2 of the problem.
    Finds all the coordinates that are touched by more than one line in the input file,
    and returns their count, this time with diagonal lines considered.
    >>> part_2("input/05-small.txt")
    12
    >>> part_2("input/05.txt")
    19929
    """
    return count_points_that_appear_more_than_once(input_filename, with_diagonal=True)


if __name__ == "__main__":
    print(part_1("input/05.txt"))
    print(part_2("input/05.txt"))
