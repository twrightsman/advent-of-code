import re
import sys

instruction_pattern = re.compile(r'Sue ([0-9]+): ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+), ([a-z]+): ([0-9]+)')

ticker_tape = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1
}

sues = []
for line in sys.stdin:
    result = re.match(instruction_pattern, line)

    sue_id = result.group(1)
    key1 = result.group(2)
    value1 = int(result.group(3))
    key2 = result.group(4)
    value2 = int(result.group(5))
    key3 = result.group(6)
    value3 = int(result.group(7))

    sue_dict = {
        key1: value1,
        key2: value2,
        key3: value3
    }

    sues.append(sue_dict)

for index, sue in enumerate(sues):
    matches = 0
    for key in sue:
        if sue[key] == ticker_tape[key]:
            matches += 1
    if matches == 3:
        print('Sue #', index + 1)