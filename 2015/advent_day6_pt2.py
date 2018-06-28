import sys
import re
from PIL import Image

#set up million light grid
#previous solution copied 1000 references to same y list across the x list
#this makes sure a new y list is created for each x value
lights = [[0] * 1000 for n in range(1000)]

def perform_instruction(command, x1, y1, x2, y2):
    if command == 'turn on':
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] += 1

    if command == 'turn off':
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                if lights[x][y] > 0:
                    lights[x][y] -= 1

    if command == 'toggle':
        for x in range(min(x1, x2), max(x1, x2) + 1):
            for y in range(min(y1, y2), max(y1, y2) + 1):
                lights[x][y] += 2

#compile for efficiency
instruction_pattern = re.compile(r'^([a-z ]*) ([1-9][0-9][0-9]|[1-9][0-9]|[0-9]),([1-9][0-9][0-9]|[1-9][0-9]|[0-9]) through ([1-9][0-9][0-9]|[1-9][0-9]|[0-9]),([1-9][0-9][0-9]|[1-9][0-9]|[0-9])')

for instruction in sys.stdin:
    result = re.match(instruction_pattern, instruction)

    command = result.group(1)
    x1 = int(result.group(2))
    y1 = int(result.group(3))
    x2 = int(result.group(4))
    y2 = int(result.group(5))

    perform_instruction(command, x1, y1, x2, y2)

total_brightness = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        total_brightness += lights[x][y]

print(total_brightness)

outimg = Image.new('L', (len(lights), len(lights[0])))
outimg.putdata([x for column in lights for x in column])
outimg.save('advent_day6_pt2.png')
