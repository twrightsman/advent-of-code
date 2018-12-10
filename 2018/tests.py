import unittest

from importlib import import_module
from io import StringIO

class TestDay1Part1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module("adventofcode.day1"), 'solve_part1'))

    def test_positive(self):
        self.assertEqual(self.solver(StringIO("+1\n+1\n+1\n")), 3)

    def test_mixed(self):
        self.assertEqual(self.solver(StringIO("+1\n+1\n-2\n")), 0)

    def test_negative(self):
        self.assertEqual(self.solver(StringIO("-1\n-2\n-3\n")), -6)


class TestDay1Part2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module("adventofcode.day1"), 'solve_part2'))

    def test_1(self):
        self.assertEqual(self.solver(StringIO("+1\n-1\n")), 0)

    def test_2(self):
        self.assertEqual(self.solver(StringIO("+3\n+3\n+4\n-2\n-4\n")), 10)

    def test_3(self):
        self.assertEqual(self.solver(StringIO("-6\n+3\n+8\n+5\n-6\n")), 5)

    def test_4(self):
        self.assertEqual(self.solver(StringIO("+7\n+7\n-2\n-7\n-4\n")), 14)


if __name__ == '__main__':
    unittest.main()
