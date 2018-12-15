from collections import Counter

def solve_part1(input_file):
    ID_2mers = 0
    ID_3mers = 0
    for line in input_file:
        c = Counter(line.rstrip())
        ID_2mers += 1 if (2 in c.values()) else 0
        ID_3mers += 1 if (3 in c.values()) else 0

    return ID_2mers * ID_3mers

def solve_part2(input_file):
    return None
