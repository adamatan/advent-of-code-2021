# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 7.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

import sys
from collections import namedtuple
from loguru import logger
from typing import List

logger.remove()
logger.add(sys.stderr, level="TRACE")

Signal = namedtuple("Signal", ["patterns", "output_values"])


def get_input(input_filename: str) -> List[Signal]:
    """
    Parses the input file into a list of Signal objects.
    >>> len(get_input("input/08.txt"))
    200
    >>> get_input("input/08.txt")[1]
    Signal(patterns=['fgcbed', 'bcedga', 'cafb', 'acgfd', 'cgabd', 'cgf', 'dfaeg', 'dfbcga', 'bceagdf', 'fc'], output_values=['cf', 'gdfea', 'fdagbc', 'dfacg'])
    """
    signals_and_output_values = []
    with open(input_filename) as f:
        for line in f:
            signals_str, output_values_str = line.split("|")
            signals = signals_str.strip().split()
            output_values = output_values_str.strip().split()
            signals_and_output_values.append(Signal(signals, output_values))
    return signals_and_output_values


def solve_one_signal(signal: Signal) -> int:
    """
    Solves a single signal.

    Argument:
        signal -- a Signal object, with patterns and output values

    Returns:
        The numeric values of the output values.

    For example:
    Signal(patterns=['dbfea', 'bcaefdg', 'dcfgeb', 'ag', 'bfceag', 'egfcda', 'becfg', 'fgeba', 'gcab', 'ega'],
            output_values=['agbfecd', 'aedfcgb', 'gcba', 'ga'])

    Each pattern is a string, each representing a single digit from 0 to 9 in the 7-segment system.
    Each pattern is made of segments, represented by a single character. The function maps each pattern
    to a digit, and then creates a four-digit value from the output_values.

    Understanding 1, 7, 4, and 8 is the first step - each have a unique number of segments (e.g. 1 is the only
    one with 2 segments on).

    3 is then deduced as the only superset of 1 with 5 segments.
    9 is then deduced as the only superset of 4 with 6 segments.
    0 is then deduced as the only superset of 7 with 6 segments.
    6 is then deduced as the only 6 segments number left unsolved.
    5 is then deduced as the only subset of 9 with 5 segments.
    2 is then deduced as the only remaining number with 5 segments.
    """

    digits_to_patterns = {}
    remaining_patterns = set(signal.patterns)

    # Maps length of pattern to the number of digits that pattern has.
    # For example, the only digit of length 2 is 1, and the only digit of length 3 is 7.
    unique_digit_sizes = {2: 1, 3: 7, 4: 4, 7: 8}

    for length, digit in unique_digit_sizes.items():
        pattern = {s for s in signal.patterns if len(s) == length}.pop()
        digits_to_patterns[digit] = pattern
        remaining_patterns.remove(pattern)

    three = {
        s
        for s in remaining_patterns
        if len(s) == 5 and set(digits_to_patterns[1]).issubset(set(s))
    }.pop()
    digits_to_patterns[3] = three
    remaining_patterns.remove(three)

    nine = {
        s
        for s in remaining_patterns
        if len(s) == 6 and set(digits_to_patterns[4]).issubset(set(s))
    }.pop()
    digits_to_patterns[9] = nine
    remaining_patterns.remove(nine)

    zero = {
        s
        for s in remaining_patterns
        if len(s) == 6 and set(digits_to_patterns[7]).issubset(set(s))
    }.pop()
    digits_to_patterns[0] = zero
    remaining_patterns.remove(zero)

    six = {
        s for s in remaining_patterns if len(s) == 6 and set().issubset(set(s))
    }.pop()
    digits_to_patterns[6] = six
    remaining_patterns.remove(six)

    five = {
        s
        for s in remaining_patterns
        if len(s) == 5 and set(s).issubset(digits_to_patterns[9])
    }.pop()
    digits_to_patterns[5] = five
    remaining_patterns.remove(five)

    two = {s for s in remaining_patterns if len(s) == 5}.pop()
    digits_to_patterns[2] = two
    remaining_patterns.remove(two)

    # Now let's calculate the output values.
    # We need to sort the segments, because they might come in different order, an "fe" = "ef"
    output_patterns = ["".join(sorted(p)) for p in signal.output_values]
    output_digits = []
    for pattern in output_patterns:
        for digit, digit_pattern in digits_to_patterns.items():
            sorted_digit_pattern = "".join(sorted(digit_pattern))
            if pattern == sorted_digit_pattern:
                output_digits.append(str(digit))
    return int("".join(output_digits))


def part_2(input_filename: str) -> int:
    signals = get_input(input_filename)
    response = [solve_one_signal(signal) for signal in signals]
    return sum(response)


def part_1(input_filename: str) -> int:
    """Solves part 1 of the day 6 puzzle.
    >>> part_1("input/08-small.txt")
    26
    >>> part_1("input/08.txt")
    519
    """
    count = 0
    signals = get_input(input_filename)
    for signal in signals:
        for value in signal.output_values:
            if len(value) in (2, 3, 4, 7):
                count += 1
    return count


if __name__ == "__main__":
    print(part_1("input/08.txt"))
    print(part_2("input/08.txt"))
