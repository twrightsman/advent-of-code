import sys
import re

pat = re.compile(r'(\\")')

newcode_chars = 0
code_chars = 0

for line in sys.stdin:
    stripped_line = line.rstrip()
    code_chars += len(stripped_line)
    #+2 for the new surrounding double quotes on each line
    newcode_chars += (len(re.escape(stripped_line)) + 2)
    print(re.escape(stripped_line))

print(newcode_chars - code_chars)