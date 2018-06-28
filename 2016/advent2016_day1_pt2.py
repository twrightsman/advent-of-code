from sys import exit

directions = input("Directions: ").split(', ')

coords = [0, 0]
coord_history = [[0, 0]]
compass = ('N', 'E', 'S', 'W')
facing = 'N'

def calculate_distance(c):
    return sum([abs(i) for i in c])

def check_and_add(c):
    if c in coord_history:
        print(calculate_distance(c))
        exit()
    else:
        # "proper" list copy from:
        # https://stackoverflow.com/questions/2612802/
        coord_history.append(list(c))

for direction in directions:
    rotation, steps = direction[0], int(direction[1:])

    # rotate (R = clockwise, L = counterclockwise)
    if rotation == 'R':
        # credit: https://stackoverflow.com/questions/8951020/
        facing = compass[(compass.index(facing) + 1) % 4]
    if rotation == 'L':
        facing = compass[compass.index(facing) - 1]

    # walk
    if facing == 'N':
        for y in range(coords[1] + 1, coords[1] + steps + 1):
            coords[1] = y
            check_and_add(coords)
    if facing == 'E':
        for x in range(coords[0] + 1, coords[0] + steps + 1):
            coords[0] = x
            check_and_add(coords)
    if facing == 'S':
        for y in range(coords[1] - 1, coords[1] - steps - 1, -1):
            coords[1] = y
            check_and_add(coords)
    if facing == 'W':
        for x in range(coords[0] - 1, coords[0] - steps - 1, -1):
            coords[0] = x
            check_and_add(coords)
