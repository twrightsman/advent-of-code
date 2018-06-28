directions = input("Directions: ").split(', ')

coords = [0, 0]
compass = ('N', 'E', 'S', 'W')
facing = 'N'

for direction in directions:
    rotation, steps = direction[0], int(direction[1:])
    
    # rotate (R = clockwise, L = counterclockwise)
    if rotation == 'R':
        # credit: https://stackoverflow.com/questions/8951020/
        facing = compass[(compass.index(facing) + 1) % 4]
    if rotation == 'L':
        facing = compass[compass.index(facing) - 1]

    # teleport (not walk)
    if facing == 'N':
        coords[1] += steps
    if facing == 'E':
        coords[0] += steps
    if facing == 'S':
        coords[1] -= steps
    if facing == 'W':
        coords[0] -= steps

# calculate blocks away
print(sum([abs(x) for x in coords]))
