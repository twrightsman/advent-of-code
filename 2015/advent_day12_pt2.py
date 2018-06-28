import collections
import json
import sys

def flatten(l):
    '''Credit:
    http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python
    '''
    if isinstance(l, dict):
        l = l.values()

        if 'red' in l:
            return 'red'
                 
    for el in l:
        if isinstance(l, dict):
            for key in el:
                for sub in flatten(el[key]):
                    yield sub
        elif isinstance(el, collections.Iterable) and not isinstance(el, str):
            for sub in flatten(el):
                yield sub
        else:
            yield el

puzzle_input = sys.stdin.read()

decoded_json = json.loads(puzzle_input)

flattened_json = flatten(decoded_json)

sum = 0
for element in flattened_json:
    try:
        operand = int(element)
        sum += operand
    except ValueError:
        continue

print(sum)