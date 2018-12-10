#!/usr/bin/env python3
"""
Advent of Code 2018
"""

__author__ = 'Travis Wrightsman'
__version__ = '0.1'
__license__ = 'GPLv3'

import argparse
from importlib import import_module
import logging
from pathlib import Path
import sys


def main(args):
    logging.info(args)

    with open(args.input_path) as input_file:
        solving_module = import_module("adventofcode.day{}".format(args.day))
        solver = getattr(solving_module, "solve_part{}".format(args.part))
        solution = solver(input_file)

    print(solution)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog = "python3 advent2018.py")

    # Required positional argument
    parser.add_argument(
        'day',
        help = 'day of December to solve',
        type = int,
        metavar = 'DAY',
        choices = range(1, 26))

    parser.add_argument(
        'part',
        help = 'part of day\'s puzzle (1 or 2) to solve',
        type = int,
        metavar = 'PART',
        choices = [1, 2]
    )

    parser.add_argument(
        '-i', '--input',
        help = 'path to input file (Default: input/dayN.txt, where N is the' +
               ' day to solve)',
        dest = 'input_path',
        metavar = 'PATH',
        type = Path)

    parser.add_argument(
        '--version',
        action = 'version',
        version = "%(prog)s (version {version})".format(version=__version__))

    parser.add_argument(
        '-d', '--debug',
        help = 'Output detailed debugging messages',
        action = 'store_const',
        dest = 'logLevel',
        const = logging.DEBUG,
        default = logging.WARNING)

    parser.add_argument(
        '-v', '--verbose',
        help = 'Output progress and other informative messages',
        action = 'store_const',
        dest = 'logLevel',
        const = logging.INFO)

    args = parser.parse_args()

    # argument validation
    if args.input_path is None:
        args.input_path = Path("input/day{}.txt".format(args.day))

    # set up logging to stderr
    root = logging.getLogger()
    root.setLevel(args.logLevel)
    stderr_log_handler = logging.StreamHandler(sys.stderr)
    stderr_log_handler.setLevel(args.logLevel)
    stderr_log_formatter = logging.Formatter("{asctime} [{module}:{levelname}] {message}", style='{')
    stderr_log_handler.setFormatter(stderr_log_formatter)
    root.addHandler(stderr_log_handler)

    main(args)
