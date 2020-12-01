from pathlib import Path
import unittest

from aoc.day1 import day1_part1


def get_input_file(filename: str) -> str:
    input_path = Path(__file__).parent / 'inputs' / filename
    with open(input_path) as input_file:
        input_text = input_file.read()
    return input_text


class PuzzleTest(unittest.TestCase):
    def test_day1_part1(self):
        expense_report = get_input_file("day1.txt")
        self.assertEqual(day1_part1(expense_report), "806656")

