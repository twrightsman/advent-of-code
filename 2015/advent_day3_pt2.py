import sys
from collections import defaultdict
from itertools import islice

def constant_factory(value):
    return lambda: value

houses = defaultdict(constant_factory(0))
curX, curY = 0, 0
curXrob, curYrob = 0, 0
houses['{},{}'.format(curX, curY)] = 0

input_txt = sys.stdin.read()

for (char1, char2) in zip(islice(input_txt, 0, None, 2), islice(input_txt, 1, None, 2)):
    if char1 == "^":
        curY += 1
    if char1 == ">":
        curX += 1
    if char1 == "<":
        curX -= 1
    if char1 == "v":
        curY -= 1

    houses['{},{}'.format(curX, curY)] += 1

    if char2 == "^":
        curYrob += 1
    if char2 == ">":
        curXrob += 1
    if char2 == "<":
        curXrob -= 1
    if char2 == "v":
        curYrob -= 1

    houses['{},{}'.format(curXrob, curYrob)] += 1    

print(len(list(houses.keys())))

