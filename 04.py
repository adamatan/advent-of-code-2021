# -*- coding: utf-8 -*-

"""
Advent of Code sulution for day 4.

I'm using it to learn some basic NumPy.

Repo and README: https://github.com/adamatan/advent-of-code-2021

Copyright (c) 2021 Adam Matan and distributed under the MIT License.
"""

import sys
from typing import List, Tuple, Set
import numpy as np


class BingoBoard:
    """A representation of a bingo board.
    The board keeps its numbers as its state, and can check whether the board
    wins any given lottery numbers."""

    def __init__(self, numbers: List[int]) -> None:
        """Converts a flat list of integers into a 5x5 board"""
        self.board = np.reshape(numbers, (5, 5))

    def is_winning(self, lottery_numbers):
        """Returns true if the board wins the given lottery numbers."""
        numbers_as_set = set(lottery_numbers)
        for row_or_column in self._get_rows_and_columns_as_sets():
            if row_or_column.issubset(numbers_as_set):
                return True
        return False

    def _get_rows_and_columns_as_sets(self) -> List[Set[int]]:
        """Returns a list of all rows and columns as a list of sets."""
        rows_and_columns = []
        for row in self.board:
            rows_and_columns.append(set(row))
        for column in self.board.T:
            rows_and_columns.append(set(column))
        return rows_and_columns

    def calculate_score(self, lottery_numbers: List[int]) -> int:
        """Returns the score of the board for the given lottery numbers."""
        if not self.is_winning(lottery_numbers):
            raise ValueError("The board does not win the given lottery numbers.")
        lottery_numbers_set = set(lottery_numbers)
        board_numbers_set = set(self.board.flatten())
        unmarked_numbers = board_numbers_set - lottery_numbers_set
        score = sum(unmarked_numbers) * lottery_numbers[-1]
        return score

    def to_str_with_lottery_numbers_marked(self, lottery_numbers):
        """Debug function.
        Returns a string representation of the board with the lottery numbers marked with a *"""
        s = ""
        for row in self.board:
            for number in row:
                s += f"{'*' if number in lottery_numbers else ' '}{number:<4}"
            s += "\n"
        return s

    def __repr__(self) -> str:
        return str(f"<Bingo Board: {self.board.flatten()}>")

    def __str__(self) -> str:
        return str(f"Bingo board:\n{self.board}")


def get_input(input_filename) -> Tuple[List[int], List[BingoBoard]]:
    """Reads and parses the input file into:
    1. A list of lottery numbers
    2. A List of Bingo boards
    """
    with open(input_filename) as f:
        raw_input = f.read()
    parts = raw_input.split("\n\n")
    # The lottery numbes drawn by the bingo team
    lottery_numbers = [int(n) for n in parts[0].split(",")]

    # The boards, as BingoBoard objects
    bingo_boards = []
    for part in parts[1:]:
        bingo_board_numbers = [int(n) for n in part.split()]
        bingo_boards.append(BingoBoard(bingo_board_numbers))
    return lottery_numbers, bingo_boards


def part_1(input_filename):
    """
    Solves part 1 of the puzzle.
    Tries each board with

    >>> part_1("input/04.txt")
    41668
    >>> part_1("input/04-small.txt")
    4512
    """
    lottery_numbers, bingo_boards = get_input(input_filename)
    for i in range(5, len(lottery_numbers)):
        current_lottery_numbers = lottery_numbers[: i + 1]
        for board in bingo_boards:
            if board.is_winning(current_lottery_numbers):
                score = board.calculate_score(current_lottery_numbers)
                return score


def part_2(input_filename):
    """
    Solves part 2 of the puzzle.
    Draws numbers till we have a single non-winning board, then draw numbers
    till that board wins to calculate its score.

    >>> part_2("input/04-small.txt")
    1924
    >>> part_2("input/04.txt")
    10478
    """
    lottery_numbers, bingo_boards = get_input(input_filename)
    remaining_boards = set(bingo_boards)
    winning_boards = set()
    i = 5

    # Draw numbers until we have a single non-winning board
    for i in range(5, len(lottery_numbers)):
        current_lottery_numbers = lottery_numbers[: i + 1]
        winning_boards = winning_boards | {
            b for b in remaining_boards if b.is_winning(current_lottery_numbers)
        }
        remaining_boards = remaining_boards - winning_boards
        if len(winning_boards) == len(bingo_boards) - 1:
            break
    assert len(remaining_boards) == 1
    last_board = remaining_boards.pop()

    # Draw numbers until the last board wins
    while not last_board.is_winning(current_lottery_numbers):
        i += 1
        current_lottery_numbers = lottery_numbers[: i + 1]

    score = last_board.calculate_score(current_lottery_numbers)
    return score


if __name__ == "__main__":
    print(part_1("input/04.txt"))
    print(part_2("input/04.txt"))
