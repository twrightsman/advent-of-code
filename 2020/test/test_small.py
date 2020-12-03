from textwrap import dedent
import unittest

from aoc.day1 import day1_part1, day1_part2
from aoc.day2 import day2_part1, day2_part2
from aoc.day3 import day3_part1, day3_part2


class SmallTest(unittest.TestCase):

    day1_expense_report = "1721\n979\n366\n299\n675\n1456"
    day2_password_database = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
    day3_map = dedent("""\
        ..##.......
        #...#...#..
        .#....#..#.
        ..#.#...#.#
        .#...##..#.
        ..#.##.....
        .#.#.#....#
        .#........#
        #.##...#...
        #...##....#
        .#..#...#.#
        """)

    def test_day1_part1_small(self):
        self.assertEqual(day1_part1(self.day1_expense_report), "514579")

    def test_day1_part2_small(self):
        self.assertEqual(day1_part2(self.day1_expense_report), "241861950")

    def test_day2_part1_small(self):
        self.assertEqual(day2_part1(self.day2_password_database), "2")

    def test_day2_part2_small(self):
        self.assertEqual(day2_part2(self.day2_password_database), "1")

    def test_day3_part1_small(self):
        self.assertEqual(day3_part1(self.day3_map), "7")

    def test_day3_part2_small(self):
        self.assertEqual(day3_part2(self.day3_map), "336")

