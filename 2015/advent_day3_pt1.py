import sys
from collections import defaultdict

def constant_factory(value):
    return lambda: value

houses = defaultdict(constant_factory(0))
curX, curY = 0, 0
curXrob, curYrob = 0, 0
houses['{},{}'.format(curX, curY)] = 0

for char in sys.stdin.read():
    if char == "^":
        curY += 1
    if char == ">":
        curX += 1
    if char == "<":
        curX -= 1
    if char == "v":
        curY -= 1

    houses['{},{}'.format(curX, curY)] += 1

print(len(list(houses.keys())))

