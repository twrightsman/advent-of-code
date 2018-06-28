import sys
import re

molecule = str()
replacements = {}

for line in sys.stdin:
    if line == "\n":
        molecule = sys.stdin.read().rstrip()
        break

    initial_atom, final_atom = line.rstrip().split(' => ')

    if not initial_atom in replacements:
        replacements[initial_atom] = []

    replacements[initial_atom].append(final_atom)

distinct_molecules = set()
for key in replacements:
    indecies = [m.start() for m in re.finditer(key, molecule)]
    for index in indecies:
        for value in replacements[key]:
            distinct_molecules.add(molecule[:index] + molecule[index:].replace(key, value, 1))

print(len(distinct_molecules))
