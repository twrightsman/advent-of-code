from collections import defaultdict
from itertools import repeat

message = ''

with open("day6_input.txt") as message_file:
    char_freq = [defaultdict(lambda: 0) for i in range(8)]
    for line in message_file:
        for index, char in enumerate(line.rstrip()):
            char_freq[index][char] += 1

    for char_freq_dict in char_freq:
        message += sorted(char_freq_dict.keys(), key=lambda k: char_freq_dict[k])[0]

print(message)
