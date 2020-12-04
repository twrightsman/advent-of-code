from textwrap import dedent
import unittest

from aoc.day1 import day1_part1, day1_part2
from aoc.day2 import day2_part1, day2_part2
from aoc.day3 import day3_part1, day3_part2
from aoc.day4 import day4_part1, is_day2_valid_passport


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
    day4_part1_passport_batch = dedent("""\
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm

        iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884
        hcl:#cfa07d byr:1929

        hcl:#ae17e1 iyr:2013
        eyr:2024
        ecl:brn pid:760753108 byr:1931
        hgt:179cm

        hcl:#cfa07d eyr:2025 pid:166559648
        iyr:2011 ecl:brn hgt:59in
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

    def test_day4_part1_small(self):
        self.assertEqual(day4_part1(self.day4_part1_passport_batch), "2")

    def test_day4_part2_small(self):
        self.assertFalse(is_day2_valid_passport("eyr:1972 cid:100\nhcl:#18171d ecl:amb hgt:170 pid:186cm iyr:2018 byr:1926"))
        self.assertFalse(is_day2_valid_passport("iyr:2019\nhcl:#602927 eyr:1967 hgt:170cm\necl:grn pid:012533040 byr:1946"))
        self.assertFalse(is_day2_valid_passport("hcl:dab227 iyr:2012\necl:brn hgt:182cm pid:021572410 eyr:2020 byr:1992 cid:277"))
        self.assertFalse(is_day2_valid_passport("hgt:59cm ecl:zzz\neyr:2038 hcl:74454a iyr:2023\npid:3556412378 byr:2007"))
        self.assertTrue(is_day2_valid_passport("pid:087499704 hgt:74in ecl:grn iyr:2012 eyr:2030 byr:1980\nhcl:#623a2f"))
        self.assertTrue(is_day2_valid_passport("eyr:2029 ecl:blu cid:129 byr:1989\niyr:2014 pid:896056539 hcl:#a97842 hgt:165cm"))
        self.assertTrue(is_day2_valid_passport("hcl:#888785\nhgt:164cm byr:2001 iyr:2015 cid:88\npid:545766238 ecl:hzl\neyr:2022"))
        self.assertTrue(is_day2_valid_passport("iyr:2010 hgt:158cm hcl:#b6652a ecl:blu byr:1944 eyr:2021 pid:093154719"))

