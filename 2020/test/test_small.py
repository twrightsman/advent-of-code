import unittest

from aoc.day1 import day1_part1, day1_part2
from aoc.day2 import day2_part1, day2_part2


class SmallTest(unittest.TestCase):
    def test_day1_part1_small1(self):
        report = "1721\n979\n366\n299\n675\n1456"
        self.assertEqual(day1_part1(report), "514579")

    def test_day1_part2_small1(self):
        report = "1721\n979\n366\n299\n675\n1456"
        self.assertEqual(day1_part2(report), "241861950")

    def test_day2_part1_small1(self):
        database = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
        self.assertEqual(day2_part1(database), "2")

    def test_day2_part2_small1(self):
        database = "1-3 a: abcde\n1-3 b: cdefg\n2-9 c: ccccccccc"
        self.assertEqual(day2_part2(database), "1")

