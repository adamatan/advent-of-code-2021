# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 3.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

from collections import Counter
from enum import Enum


class Gas(Enum):
    OXYGEN = 0
    CO2 = 1


def get_input():
    """Reads the input file into a list of lines."""
    with open("input/03.txt") as f:
        lines = [l.strip() for l in f.readlines()]
    return lines


def most_and_least_common_digit(lines, position):
    """Returns the most common digit in every position of the input lines.
    For example, ("000", "011", "110", 0) would give ("0", "1") - as the most
    common digit in the first position is "0" (two out of three).
    >>> most_and_least_common_digit(["000", "011", "110"], 0)
    ('0', '1')
    """
    # Assuming that all lines are of the same length
    common_digit = Counter([l[position] for l in lines])
    # If digits are equally common, prefer "1" as the most common
    if common_digit.most_common()[0][1] == common_digit.most_common()[1][1]:
        return "1", "0"
    most_common_digit = common_digit.most_common()[0][0]
    least_common_digit = common_digit.most_common()[-1][0]
    return most_common_digit, least_common_digit


def most_and_least_common_digit_in_every_position(lines):
    """Returns the most common digit in every position of the input lines.
    For example, "000", "011", "110" would give "010" - as the most common first digit
    is "0" (two out of three) and so on.
    >>> most_and_least_common_digit_in_every_position(["000", "011", "110"])
    ('010', '101')
    """
    # Assuming that all lines are of the same length
    number_of_digits = len(lines[0])
    common_digits = [
        most_and_least_common_digit(lines, i) for i in range(number_of_digits)
    ]
    most_common_digits = "".join([c[0] for c in common_digits])
    least_common_digits = "".join([c[1] for c in common_digits])
    return most_common_digits, least_common_digits


def part_1(input_lines) -> int:
    """Part 1 solution.
    Finds two binary numbers, each built from the most common and least common digits
    at every position in the input lines, and multiplies them.

    >>> input_lines = get_input()
    >>> print(part_1(input_lines))
    693486
    """
    most_common, least_common = most_and_least_common_digit_in_every_position(
        input_lines
    )
    most_common, least_common = int(most_common, 2), int(least_common, 2)
    return most_common * least_common


def find_oxygen_and_co2_levels(input_lines, gas: Gas) -> int:
    """Finds the level of oxygen and carbon dioxide in the input lines.
    This is done by iteratively filtering the input lines by keeping only the lines
    whose digit at the n-th position is the most/least (oxygen/co2) common digit at
    that position across all lines, till we're left with a single line.
    >>> input_lines = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    >>> print(find_oxygen_and_co2_levels(input_lines, Gas.OXYGEN))
    23
    >>> print(find_oxygen_and_co2_levels(input_lines, Gas.CO2))
    10
    """
    lines = input_lines.copy()
    position = 0
    while len(lines) > 1:
        most_common, least_common = most_and_least_common_digit(lines, position)
        criteria = most_common if gas == Gas.OXYGEN else least_common
        lines = [l for l in lines if l[position] == criteria]
        position += 1

    numerical_value = int(lines[0], 2)
    return numerical_value


def part_2(input_lines) -> int:
    """Part 2 solution.
    Iteratively filters the input lines by keeping only the lines whose digit
    at the n-th position is the most common digit at that position, till we're left
    with a single line.
    >>> input_lines = ['00100', '11110', '10110', '10111', '10101', '01111', '00111', '11100', '10000', '11001', '00010', '01010']
    >>> print(part_2(input_lines))
    230
    """
    oxygen = find_oxygen_and_co2_levels(input_lines, Gas.OXYGEN)
    co2 = find_oxygen_and_co2_levels(input_lines, Gas.CO2)
    return oxygen * co2


if __name__ == "__main__":
    input_lines = get_input()
    print(part_1(input_lines))
    print(part_2(input_lines))
