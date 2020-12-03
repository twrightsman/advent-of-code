from functools import reduce
from operator import mul
from typing import List

def sum_tree_collisions(map_array: List[str], run: int, rise: int) -> int:
    x, y = 0, 0

    trees_encountered = 0
    while y < len(map_array):
        trees_encountered += int(map_array[y][x] == '#')
        y += rise
        # wrap x around if too long
        x += run
        if x >= len(map_array[0]):
            x -= len(map_array[0])

    return trees_encountered


def day3_part1(submap: str) -> str:
    map_array = [line.rstrip() for line in submap.split("\n") if line.rstrip()]
    return str(sum_tree_collisions(map_array, 3, 1))


def day3_part2(submap: str) -> str:
    map_array = [line.rstrip() for line in submap.split("\n") if line.rstrip()]
    parameter_space = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    tree_collisions = (sum_tree_collisions(map_array, run, rise) for run, rise in parameter_space)
    return str(reduce(mul, tree_collisions))

