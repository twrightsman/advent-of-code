from collections import Counter
from itertools import combinations


def solve_part1(input_file):
    ID_2mers = 0
    ID_3mers = 0
    for line in input_file:
        c = Counter(line.rstrip())
        ID_2mers += 1 if (2 in c.values()) else 0
        ID_3mers += 1 if (3 in c.values()) else 0

    return ID_2mers * ID_3mers

def solve_part2(input_file):
    lines = [line.rstrip() for line in input_file]

    for cmb in combinations(lines, 2):
        cmp_vec = [c1 == c2 for c1, c2 in zip(cmb[0], cmb[1])]
        if sum(cmp_vec) == (len(cmb[0]) - 1):
            return ''.join(
                [c for i, c in enumerate(cmb[0]) if cmp_vec[i]]
            )

    return None
