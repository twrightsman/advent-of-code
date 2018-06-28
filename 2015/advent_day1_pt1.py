import sys

floor = 0

for char in sys.stdin.read():
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1

print(floor)