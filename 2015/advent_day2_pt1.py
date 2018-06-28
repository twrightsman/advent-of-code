import sys

total_paper = 0

def get_surface_area(l, w, h):
    surface_area = (2 * l * w) + (2 * w * h) + (2 * h * l)
    extra = min(l * w, w * h, h * l)

    return surface_area + extra

for line in sys.stdin:
    l, w, h = [int(x) for x in line.split('x')]

    total_paper += get_surface_area(l, w, h)

print(total_paper)