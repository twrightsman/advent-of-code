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
        self.assertEqual(self.solver(StringIO("+1\n+1\n-2")), 0)

    def test_negative(self):
        self.assertEqual(self.solver(StringIO("-1\n-2\n-3\n")), -6)

if __name__ == '__main__':
    unittest.main()
