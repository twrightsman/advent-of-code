from pathlib import Path
import unittest

from aoc.day1 import day1_part1, day1_part2
from aoc.day2 import day2_part1, day2_part2
from aoc.day3 import day3_part1, day3_part2
from aoc.day4 import day4_part1, day4_part2


def get_input_file(filename: str) -> str:
    input_path = Path(__file__).parent / 'inputs' / filename
    with open(input_path) as input_file:
        input_text = input_file.read()
    return input_text


class PuzzleTest(unittest.TestCase):
    def test_day1_part1(self):
        expense_report = get_input_file("day1.txt")
        self.assertEqual(day1_part1(expense_report), "806656")

    def test_day1_part2(self):
        expense_report = get_input_file("day1.txt")
        self.assertEqual(day1_part2(expense_report), "230608320")

    def test_day2_part1(self):
        password_database = get_input_file("day2.txt")
        self.assertEqual(day2_part1(password_database), "458")

    def test_day2_part2(self):
        password_database = get_input_file("day2.txt")
        self.assertEqual(day2_part2(password_database), "342")

    def test_day3_part1(self):
        submap = get_input_file("day3.txt")
        self.assertEqual(day3_part1(submap), "240")

    def test_day3_part2(self):
        submap = get_input_file("day3.txt")
        self.assertEqual(day3_part2(submap), "2832009600")

    def test_day4_part1(self):
        passport_batch = get_input_file("day4.txt")
        self.assertEqual(day4_part1(passport_batch), "219")

    def test_day4_part2(self):
        passport_batch = get_input_file("day4.txt")
        self.assertEqual(day4_part2(passport_batch), "127")

