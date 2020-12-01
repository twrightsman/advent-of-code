import unittest

from aoc.day1 import day1_part1


class SmallTest(unittest.TestCase):
    def test_day1_part1_small1(self):
        report = "1721\n979\n366\n299\n675\n1456"
        self.assertEqual(day1_part1(report), "514579")
