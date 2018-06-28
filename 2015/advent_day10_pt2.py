import sys
from itertools import islice

#Credit goes to Python Docs
def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

def LookAndSay(seed):
    sequence = seed

    while sequence:
        output = ''
        consecutive_digits = []
        for digit in sequence:
            # Account for first digit
            if consecutive_digits:
                if digit in consecutive_digits:
                    consecutive_digits.append(digit)
                else:
                    output += '{}{}'.format(len(consecutive_digits),consecutive_digits[0])
                    consecutive_digits = [digit]
            else:
                consecutive_digits = [digit]

        # Add the final digit
        output += '{}{}'.format(len(consecutive_digits),consecutive_digits[0])
        yield output
        sequence = output

puzzle_input = sys.stdin.read().rstrip()

partOneGenerator = LookAndSay(puzzle_input)

print(len(nth(partOneGenerator, 49)))
