# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 2.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

from typing import NamedTuple

class Line(NamedTuple):
    """A line is a (direction, distance) tuple."""
    direction: str
    distance: int

    @staticmethod
    def from_string(raw_line):
        direction, distance = raw_line.split()
        return Line(direction, int(distance))

class Sub(NamedTuple):
    """A named tuple representing a submarine position and aim for part 2."""

    horizontal: int
    depth: int
    aim: int


def get_input():
    """Reads the input file into a list of lines."""
    with open("input/02.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def parse_command_part_1(line):
    """Takes a submarine status and a command, and creates a new sub position
    object."""
    direction, distance = line.split()
    distance = int(distance)
    match direction:
        case "up":
            return (0, distance)
        case "down":
            return (0, distance)
        case "forward":
            return (distance, 0)
        case _:
            raise ValueError(f"Unknown command: {direction}")

def parse_command_part_2(line: Line, sub: Sub):
    """Parses a single line of the input file into a (horizontal, depth) tuple,
    signifying the submarine's movement."""
    match line.direction:
        case "up":
            return Sub(sub.horizontal, sub.depth, sub.aim - line.distance)
        case "down":
            return Sub(sub.horizontal, sub.depth, sub.aim + line.distance)
        case "forward":
            return Sub(sub.horizontal + line.distance, sub.depth + line.distance * sub.aim, sub.aim)


def part_1(input_lines) -> int:
    """Calculates the total submarine displacement as a a (horizontal, depth),
    and returns the multiplication of both axis requested by the puzzle."""
    location = (0, 0)
    for line in input_lines:
        command = parse_command_part_1(line)
        location = (location[0] + command[0], location[1] + command[1])
    return location[0] * location[1]

def part_2(input_lines) -> int:
    sub = Sub(0, 0, 0)
    for raw_line in input_lines:
        line = Line.from_string(raw_line)
        sub = parse_command_part_2(line, sub)
    return sub.horizontal * sub.depth

if __name__ == "__main__":
    input_lines = get_input()
    print(part_1(input_lines))
    print(part_2(input_lines))
