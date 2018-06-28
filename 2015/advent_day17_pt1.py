import sys
from itertools import chain, combinations

def all_subsets(ss):
    return chain(*map(lambda x: combinations(ss, x), range(1, len(ss) + 1)))

containers = []

for line in sys.stdin:
    containers.append(int(line.rstrip()))

subset150 = []

for subset in all_subsets(containers):
    if sum(subset) == 150:
        subset150.append(subset)

print(len(subset150))
