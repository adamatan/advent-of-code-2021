# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 1.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""


def get_input():
    with open("input/01.txt") as f:
        lines = [int(l) for l in f.readlines()]
    return lines


def part_1_soliution_1(lines):
    """Simple iteration and counter solution.
    That's the way I like it. It can be done with smarter list comprehension,
    but the price paid is the readability.
    Counts the number of times a depth measurement increases."""
    increase_counter = 0
    for i in range(1, len(lines)):
        if lines[i] > lines[i - 1]:
            increase_counter += 1
    return increase_counter


def part_1_solution_2(lines):
    """Shorter, but not very readable.
    A good example of "clever programming" that saves a few lines of code, while
    making it unbearably ugly.
    Counts the number of times a depth measurement increases."""
    return len([i for i in range(1, len(lines)) if lines[i] > lines[i - 1]])


def part_2_solution_1(lines):
    """Checks how many times the sum of a three-measurement sliding window has
    increased, by converting the list to a list of triplets sums and reusing
    the part_1_solution_1 function.
    """
    triplets = [lines[i - 3 : i] for i in range(3, len(lines) + 1)]
    triplets_sums = [sum(triplet) for triplet in triplets]
    return part_1_soliution_1(triplets_sums)


if __name__ == "__main__":
    sonar_reads = get_input()
    part_1_solutions = part_1_soliution_1(sonar_reads), part_1_solution_2(sonar_reads)
    assert part_1_solutions[0] == part_1_solutions[1]
    print(part_1_solutions[0])
    print(part_2_solution_1(sonar_reads))
