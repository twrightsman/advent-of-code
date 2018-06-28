import sys

total_ribbon = 0

def get_ribbon_length(l, w, h):
    ribbon_length = min((2 * l) + (2 * w), (2 * l) + (2 * h), (2 * w) + (2 * h))
    bow_volume = l * w * h

    return ribbon_length + bow_volume

for line in sys.stdin:
    l, w, h = [int(x) for x in line.split('x')]

    total_ribbon += get_ribbon_length(l, w, h)

print(total_ribbon)