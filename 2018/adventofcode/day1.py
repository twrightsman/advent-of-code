from itertools import cycle


def solve_part1(input_file):
    current_freq = 0
    for line in input_file:
        current_freq += int(line.rstrip())

    return current_freq

def solve_part2(input_file):
    input_file = cycle(input_file)
    current_freq = 0
    # set is much faster for lookup operations than list
    observed_freqs = {current_freq}
    for line in input_file:
        current_freq += int(line.rstrip())
        if current_freq in observed_freqs:
            return current_freq
        else:
            observed_freqs.add(current_freq)
