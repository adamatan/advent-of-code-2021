# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 2.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""


def get_input():
    """Reads the input file into a list of lines."""
    with open("input/02.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def parse_command(line):
    """Parses a single line of the input file into a (horizontal, depth) tuple,
    signifying the submarine's movement."""
    direction, distance = line.split()
    distance = int(distance)
    match direction:
        case "up":
            return (0, -distance)
        case "down":
            return (0, distance)
        case "forward":
            return (distance, 0)
        case _:
            raise ValueError(f"Unknown command: {direction}")


def part_1(input_lines):
    """Calculates the total submarine displacement as a a (horizontal, depth),
    and returns the multiplication of both axis requested by the puzzle."""
    location = (0, 0)
    for line in input_lines:
        command = parse_command(line)
        location = (location[0] + command[0], location[1] + command[1])
    return location[0] * location[1]


if __name__ == "__main__":
    input_lines = get_input()
    print(part_1(input_lines))
