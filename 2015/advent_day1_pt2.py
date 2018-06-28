import sys

floor = 0

for position, char in enumerate(sys.stdin.read().rstrip()):
    if char == "(":
        floor += 1
    if char == ")":
        floor -= 1
        if floor < 0:
            print(position + 1)
            sys.exit()