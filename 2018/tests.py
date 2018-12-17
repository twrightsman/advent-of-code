import unittest

from importlib import import_module
from io import StringIO
import logging
import sys


class TestDay1Part1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module('adventofcode.day1'), 'solve_part1'))

    def test_positive(self):
        self.assertEqual(self.solver(StringIO("+1\n+1\n+1\n")), 3)

    def test_mixed(self):
        self.assertEqual(self.solver(StringIO("+1\n+1\n-2\n")), 0)

    def test_negative(self):
        self.assertEqual(self.solver(StringIO("-1\n-2\n-3\n")), -6)


class TestDay1Part2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module('adventofcode.day1'), 'solve_part2'))

    def test_1(self):
        self.assertEqual(self.solver(StringIO("+1\n-1\n")), 0)

    def test_2(self):
        self.assertEqual(self.solver(StringIO("+3\n+3\n+4\n-2\n-4\n")), 10)

    def test_3(self):
        self.assertEqual(self.solver(StringIO("-6\n+3\n+8\n+5\n-6\n")), 5)

    def test_4(self):
        self.assertEqual(self.solver(StringIO("+7\n+7\n-2\n-7\n-4\n")), 14)


class TestDay2Part1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module('adventofcode.day2'), 'solve_part1'))

    def test_1(self):
        self.assertEqual(self.solver(StringIO(
            "\n".join(
                ['abcdef',
                 'bababc',
                 'abbcde',
                 'abcccd',
                 'aabcdd',
                 'abcdee',
                 'ababab'])
            )), 12
        )


class TestDay2Part2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module('adventofcode.day2'), 'solve_part2'))

    def test_1(self):
        self.assertEqual(self.solver(StringIO(
            "\n".join(
                ['abcde',
                 'fghij',
                 'klmno',
                 'pqrst',
                 'fguij',
                 'axcye',
                 'wvxyz'])
            )), 'fgij'
        )


class TestDay3Part1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.solver = staticmethod(getattr(import_module('adventofcode.day3'), 'solve_part1'))

    def test_1(self):
        self.assertEqual(self.solver(StringIO(
                "\n".join(
                    ['#1 @ 1,3: 4x4',
                     '#2 @ 3,1: 4x4',
                     '#3 @ 5,5: 2x2'])
            )), 4
        )

if __name__ == '__main__':
    # set up logging to stderr
    root = logging.getLogger()
    root.setLevel(logging.DEBUG)
    stderr_log_handler = logging.StreamHandler(sys.stderr)
    stderr_log_handler.setLevel(logging.DEBUG)
    stderr_log_formatter = logging.Formatter("{asctime} [{module}:{levelname}] {message}", style='{')
    stderr_log_handler.setFormatter(stderr_log_formatter)
    root.addHandler(stderr_log_handler)

    unittest.main()
